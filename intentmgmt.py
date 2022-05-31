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
from chatbot import Chat, register_call
import json
import global_variables
import random

@register_call("default_snips_nlu_handler")
def default_snips_nlu_handler(session, text):
	parsing = global_variables.voice_assistant.intent_management.nlu_engine.parse(text)
	print(parsing)
	output = "Ich verstehe deine Frage nicht. Kannst du sie umformulieren?"
	
	intent_found = False
	
	ASSISTANT_LANGUAGE = global_variables.voice_assistant.cfg['assistant']['language']
	
	if ASSISTANT_LANGUAGE:
		NO_INTENT_RECOGNIZED = global_variables.voice_assistant.cfg['defaults'][ASSISTANT_LANGUAGE]['no_intent_recognized']
	else:
		NO_INTENT_RECOGNIZED = ['I did not understand']
	
	output = random.choice(NO_INTENT_RECOGNIZED)
	
	for intent in global_variables.voice_assistant.intent_management.dynamic_intents:
		
		if parsing["intent"]["intentName"]:
		
			if (parsing["intent"]["intentName"].lower() == intent.lower()) and (parsing["intent"]["probability"] > 0.7):
				intent_found = True
				
				arguments = dict()
				for slot in parsing["slots"]:
					arguments[slot["slotName"]] = slot["value"]["value"]
					
				argument_string = json.dumps(arguments)
				logger.debug("\nRufe {} auf mit den Argumenten {}.", intent, argument_string)
				output = getattr(globals()[intent], intent)(**arguments)
				logger.debug('\n>>> Sprachausgabe: {}',output)
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
	
		self.functions_folders = [os.path.abspath(name) for name in glob.glob("./intents/functions/*/")]
		self.dynamic_intents = []
		
		self.intent_count = 0
		for ff in self.functions_folders:
			logger.debug("\nSuche nach Funktionen in {}...", ff)
			req_file = os.path.join(ff, 'requirements.txt')
			if os.path.exists(req_file):
				install_result = self.install_requirements(req_file)
				if install_result == 0:
					logger.debug("\nAbhängigkeiten für {} erfolgreich installiert oder bereits vorhanden.", ff)
			
			intent_files = glob.glob(os.path.join(ff, 'intent_*.py'))
			for infi in intent_files:
				logger.debug("\nLade Intent-Datei {}...", infi)
								
				name = infi.strip('.py')
				name = "intents.functions." + Path(ff).name + ".intent_" + Path(ff).name
				name = name.replace(os.path.sep, ".")
				
				logger.debug("\nImportiere modul {}...", name)
				globals()[Path(ff).name] = importlib.import_module(name)
				logger.debug("\nModul {} geladen.", str(Path(ff).name))
				self.dynamic_intents.append(str(Path(ff).name))
				self.intent_count +=1
				
		logger.info("\nInitialisiere snips nlu...")
		snips_files = glob.glob(os.path.join("./intents/snips-nlu", '*.yaml'))
		self.snips_nlu_engine = SnipsNLUEngine(Config=CONFIG_DE)
		dataset = Dataset.from_yaml_files("de", snips_files)
		nlu_engine = SnipsNLUEngine(config=CONFIG_DE)
		self.nlu_engine = nlu_engine.fit(dataset)
		logger.info("\n{} Snips NLU files gefunden.", len(snips_files))
		if not self.nlu_engine:
			logger.error("\nKonnte Dialog-Engine nicht laden.")
		else:
			logger.debug("\nDialog Metadaten: {}.", self.nlu_engine.dataset_metadata)
	
		logger.debug("\nSnips NLU Training abgeschlossen")
		
		logger.info("\nInitialisiere ChatbotAI...")
		
		chatbotai_files = glob.glob(os.path.join("./intents/chatbotai", '*.template'))
		WILDCARD_FILE = './intents/chatbotai/wildcard.template'
		MERGED_FILE = './intents/chatbotai/_merger.template'
		
		with open(MERGED_FILE, 'w') as outfile:
			for caf in chatbotai_files:
				if (not Path(caf).name == Path(WILDCARD_FILE).name) and (not Path(caf).name == Path(MERGED_FILE).name):
					logger.debug("\nVerarbeite chatbotai Template {}...", Path(caf).name)
					with open(caf) as infile:
							outfile.write(infile.read())
							
			if os.path.exists(WILDCARD_FILE):
				logger.debug("\nEvaluiere Wildcard...")
				with open(WILDCARD_FILE) as infile:
						outfile.write(infile.read())
			else:
				logger.warning("\nWildcard-Datei {} konnte nicht gefunden werden. Snips NLU ist damit nicht nutzbar.", WILDCARD_FILE)		
		
		if os.path.isfile(MERGED_FILE):
			self.chat = Chat(MERGED_FILE)
		else:
			logger.error('\nDialogdatei konnte nicht in {} gefunden werden.', MERGED_FILE)
		logger.info('\nChatbot aus {} initialisiert.', MERGED_FILE)
	
	def process(self, text, speaker):
		return self.chat.respond(text)