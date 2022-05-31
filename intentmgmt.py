from loguru import logger
import pip
import importlib
import importlib.util
import glob
import os
import sys
from pathlib import Path
from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_DE
from snips_nlu.dataset import Dataset
from chatbot import Chat, register_call, mapper
import json
import random
import global_variables

# Erweitere die Klasse Chat durch die Funktion get_intend_name
class Chat(Chat):
    def get_intend_name(self, text, session_id="general"):
        session = mapper.Session(self, session_id)
		
        text = self.__normalize(text)
        try:
            previous_text = self.__normalize(session.conversation.get_bot_message(-1))
        except IndexError:
            previous_text = ""		
        text_correction = self.spell_checker.correction(text)
        current_topic = session.topic
			
        match = self.__intend_selection(text, previous_text, current_topic) or self.__intend_selection(text_correction, previous_text, current_topic)
		
        if match:
            match, parent_match, response, learn = match
            resp = random.choice(response)
            response, condition = resp
            action_start = response.find("{% call ")
            action_end = response.find("%}")
            if action_start >= 0 and action_end >= 0:
                action_corpus = response[action_start + len("{% call "):action_end - 1]
                if action_corpus.find(":") > 0:
                    action_name = action_corpus.split(':')[0]
                    return action_name
        return ""

def get_snips_nlu_intent(text):
	parsing = global_variables.voice_assistant.intent_management.nlu_engine.parse(text)
		
	for intent in global_variables.voice_assistant.intent_management.dynamic_intents:
		
		# Wurde überhaupt ein Intent erkannt?
		if parsing["intent"]["intentName"]:
		
			# Die Wahrscheinlichkeit wird geprüft, um sicherzustellen, dass nicht irgendein Intent angewendet wird,
			# der garnicht gemeint war
			if (parsing["intent"]["intentName"].lower() == intent.lower()) and (parsing["intent"]["probability"] > 0.5):
				return parsing["intent"]["intentName"]
	return ""
			
@register_call("default_snips_nlu_handler")
def default_snips_nlu_handler(session, text):
	parsing = global_variables.voice_assistant.intent_management.nlu_engine.parse(text)
	output = "Ich verstehe deine Frage nicht. Kannst du sie umformulieren?"
	
	# Schaue, ob es einen Intent gibt, der zu dem NLU intent passt
	intent_found = False
	
	# Lese die Sprache des Assistenten aus der Konfigurationsdatei
	ASSISTANT_LANGUAGE = global_variables.voice_assistant.cfg['assistant']['language']
	
	# Hole die Liste aller Antworten, die darauf hindeuten, dass kein Intent detektiert wurde
	if ASSISTANT_LANGUAGE:
		NO_INTENT_RECOGNIZED = global_variables.voice_assistant.cfg['defaults'][ASSISTANT_LANGUAGE]['no_intent_recognized']
	else:
		NO_INTENT_RECOGNIZED = ['I did not understand']
	
	# Wähle ein zufälliges Item, das erstmal aussagt, dass kein Intent gefunden wurde.
	# WIRD ein Intent gefunden, dann wird output durch eine vernünftige Antwort ersetzt.
	output = random.choice(NO_INTENT_RECOGNIZED)
	
	for intent in global_variables.voice_assistant.intent_management.dynamic_intents:
		
		# Wurde überhaupt ein Intent erkannt?
		if parsing["intent"]["intentName"]:
		
			# Die Wahrscheinlichkeit wird geprüft, um sicherzustellen, dass nicht irgendein Intent angewendet wird,
			# der garnicht gemeint war
			if (parsing["intent"]["intentName"].lower() == intent.lower()) and (parsing["intent"]["probability"] > 0.5):
				intent_found = True
								
				# Parse alle Parameter
				arguments = dict()
				for slot in parsing["slots"]:
					arguments[slot["slotName"]] = slot["value"]["value"]
					
				# Rufe Methode dynamich mit der Parameterliste auf
				argument_string = json.dumps(arguments)
				logger.debug("Rufe {} auf mit den Argumenten {}.", intent, argument_string)
				output = getattr(globals()[intent], intent)(**arguments)
				
				# Suche nicht weiter
				break
	
	return output
		
class IntentMgmt:

	intent_count = 0

	def install(self, package):
		if hasattr(pip, 'main'):
			pip.main(['install', package])
		else:
			pip._internal.main(['install', package])
			
	def install_requirements(self, filename):
		retcode = 0
		with open(filename, 'r') as f:
			for line in f:
				pipcode = pip.main(['install', line.strip()])
				retcode = retcode or pipcode
		return retcode
		
	def get_count(self):
		return self.intent_count

	def __init__(self):
	
		# 1. Registriere Funktionen, die von snips-nlu und chatbotai aufgerufen werden
		self.functions_folders = [os.path.abspath(name) for name in glob.glob("./intents/functions/*/")]
		self.dynamic_intents = []
		
		self.intent_count = 0
		for ff in self.functions_folders:
			logger.debug("Suche nach Funktionen in {}...", ff)
			req_file = os.path.join(ff, 'requirements.txt')
			if os.path.exists(req_file):
				install_result = self.install_requirements(req_file)
				if install_result == 0:
					logger.debug("Abhängigkeiten für {} erfolgreich installiert oder bereits vorhanden.", ff)
			
			# Finde Python-Dateien, die mit Intent beginnen
			intent_files = glob.glob(os.path.join(ff, 'intent_*.py'))
			for infi in intent_files:
				logger.debug("Lade Intent-Datei {}...", infi)
								
				name = infi.strip('.py')
				name = "intents.functions." + Path(ff).name + ".intent_" + Path(ff).name
				name = name.replace(os.path.sep, ".")
				
				logger.debug("Importiere modul {}...", name)
				globals()[Path(ff).name] = importlib.import_module(name)
				logger.debug("Modul {} geladen.", str(Path(ff).name))
				self.dynamic_intents.append(str(Path(ff).name))
				self.intent_count +=1
				
		# 2. Finde alle Dialoge, die über snips nlu abgehandelt werden
		logger.info("Initialisiere snips nlu...")
		snips_files = glob.glob(os.path.join("./intents/snips-nlu", '*.yaml'))
		self.snips_nlu_engine = SnipsNLUEngine(Config=CONFIG_DE)
		dataset = Dataset.from_yaml_files("de", snips_files)
		nlu_engine = SnipsNLUEngine(config=CONFIG_DE)
		self.nlu_engine = nlu_engine.fit(dataset)
		logger.info("{} Snips NLU files gefunden.", len(snips_files))
		if not self.nlu_engine:
			logger.error("Konnte Dialog-Engine nicht laden.")
		else:
			logger.debug("Dialog Metadaten: {}.", self.nlu_engine.dataset_metadata)
	
		logger.debug("Snips NLU Training abgeschlossen")
		
		# 3. Finde alle Dialoge, die über ChatbotAI abgehandelt werden
		logger.info("Initialisiere ChatbotAI...")
		
		chatbotai_files = glob.glob(os.path.join("./intents/chatbotai", '*.template'))
		WILDCARD_FILE = './intents/chatbotai/wildcard.template'
		MERGED_FILE = './intents/chatbotai/_merger.template'
		
		# Füge alle Dateien zusammen
		with open(MERGED_FILE, 'w') as outfile:
			for caf in chatbotai_files:
				# Das Wildcard-Template darf erst am Ende geladen werden
				# Das Merger-Template darf garnicht geladen werden (das ist eine Zusammenführung aller einzelnen Template Dateien)
				if (not Path(caf).name == Path(WILDCARD_FILE).name) and (not Path(caf).name == Path(MERGED_FILE).name):
					logger.debug("Verarbeite chatbotai Template {}...", Path(caf).name)
					with open(caf) as infile:
						outfile.write(infile.read())
							
			# Hänge den Wildcard Intent ans Ende
			if os.path.exists(WILDCARD_FILE):
				logger.debug("Prozessiere letzendlich Chatbotai Wildcard Template...")
				with open(WILDCARD_FILE) as infile:
						outfile.write(infile.read())
			else:
				logger.warning("Wildcard-Datei {} konnte nicht gefunden werden. Snips NLU ist damit nicht nutzbar.", WILDCARD_FILE)		
		
		if os.path.isfile(MERGED_FILE):
			# Wir müssen hier kein Default template setzen, da dieses durch den Wildcard Intent nie aufgerufen wird.
			# Vorher wird snips nlu aufgerufen.
			self.chat = Chat(MERGED_FILE)
		else:
			logger.error('Dialogdatei konnte nicht in {} gefunden werden.', MERGED_FILE)
						
		logger.info('Chatbot aus {} initialisiert.', MERGED_FILE)
		
	def register_callbacks(self):
		# Registriere alle Callback Funktionen
		logger.info("Registriere Callbacks...")
		callbacks = []
		for ff in self.functions_folders:
			module_name = "intents.functions." + Path(ff).name + ".intent_" + Path(ff).name
			module_obj = sys.modules[module_name]
			logger.debug("Verarbeite Modul {}...", module_name)
			if hasattr(module_obj, 'callback'):
				logger.debug("Callback in {} gefunden.", module_name)
				logger.info('Registriere Callback für {}.', module_name)
				callbacks.append(getattr(module_obj, 'callback'))
			else:
				logger.debug("{} hat kein Callback.", module_name)
		return callbacks
	
	def process(self, text, speaker):
	
		# Evaluiere ChatbotAI, wenn keines der strikten Intents greift, wird die Eingabe über die dialogs.template
		# automatisch an snips nlu umgeleitet.
		intent_name = self.chat.get_intend_name(text)
		if intent_name == "default_snips_nlu_handler":
			intent_name = get_snips_nlu_intent(text)
			
		# Überprüfe, ob der Benutzer diesen Intent ausführen darf
		if global_variables.voice_assistant.user_management.authenticate_intent(speaker, intent_name):
		
			old_context = global_variables.context
			
			
			response = self.chat.respond(text)
			
			if not old_context is None:
				return global_variables.context(text)
			else:
				return response
		else:
			# In diesem Beispiel lassen wir den Assistenten antworten. In Zukunft wird er einfach nicht
			# reagieren, um das Abspielen gar nicht erst zu unterbrechen
			response = speaker + " darf den Befehl " + intent_name + " nicht ausführen."

		return response