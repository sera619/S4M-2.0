import sys, json, random, importlib.util, importlib, pip, glob, os
from loguru import logger
from pathlib import Path
from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_DE
from snips_nlu.dataset import Dataset
import util.GlobalVariables as GLOBALS
from chatbot import Chat, register_call


@register_call("default_snips_nlu_handler")
def default_snips_nlu_handler(session, text):
    parsing = GLOBALS.voice_assistant.intent_management.nlu_engine.parse(text)




class IntentManagement:
    intent_count = 0
    def __init__(self):
        self.functions_folders =[os.path.abspath(name) for name in glob.glob("./intents/functions/*/")]
        self.dynamic_intents = []

        self.intent_count = 0
        for ff in self.functions_folders:
            logger.debug('\nSuche nach Funktionen in {}', ff)
            req_file = os.path.join(ff, 'requirements.txt')
            if os.path.exists(req_file):
                intall_result = self.install_requirements(req_file)
                if intall_result == 0:
                    logger.debug('\nAbhängigkeiten für {} erfolgreich installiert oder bereits vorhanden.', ff)

            intent_files = glob.glob(os.path.join(ff, 'intent_*.py'))
            for infi in intent_files:
                logger.debug('\nLade Intent-Datei {}...', infi)
                name = infi.strip('.py')
                name = "intents.functions." + Path(ff).name +".intent_" +Path(ff).name
                name = name.replace(os.path.sep, '.')
                
                logger.debug('\nImportiere Modul {}...', name)
                globals()[Path(ff).name] = importlib.import_module(name)
                logger.debug('\nModul {} erfolgreich importiert.', str(Path(ff).name))
                self.dynamic_intents.append(str(Path(ff).name))
                self.intent_count += 1
            
        
        #get all handled snips-nlu intents
        logger.info("Initialisiere Snips-NLU-Engine...")
        snips_files = glob.glob(os.path.join('.data/intents/snips-nlu', '*.yaml'))
        self.snips_nlu_engine = SnipsNLUEngine(config=CONFIG_DE)
        dataset = Dataset.from_yaml_files("de", snips_files)
        nlu_engine = SnipsNLUEngine(config=CONFIG_DE)
        self.nlu_egnine = nlu_engine.fit(dataset)
        logger.debug("\n{} Snips NLU Datein gefunden.", len(snips_files))
        if not self.nlu_egnine:
            logger.error("\nKonnte Dialog-Engine nicht initialisieren.")
        else:
            logger.debug("\nDialog Metadaten: {}.", self.nlu_egnine.metadata)

        logger.debug("\nSnips NLU Engine Training abgeschlossen.")

        logger.debug("\nInitialisiere Chatbot-AI...")
        
        chatbotai_files = glob.glob(os.path.join('.data/intents/chatbot-ai', '*.template'))
        WILDCARD_FILE = './data/intents/chatbot-ai/wildcard.template'
        MERGED_FILE = './data/intents/chatbot-ai/_merger.template'
    
        with open(MERGED_FILE, 'w') as outfile:
            for caf in chatbotai_files:
                if (not Path(caf).name == Path(WILDCARD_FILE).name) and (not Path(caf).name == Path(MERGED_FILE).name):
                    logger.debug("\nVerarbeite Chatbot AI Template {}...")
                    with open(caf) as infile:
                        outfile.write(infile.read())
            
            if os.path.exists(WILDCARD_FILE):
                logger.debug('\nVerarbeite Wildcard Template ...')
                with open(WILDCARD_FILE) as infile:
                    outfile.write(infile.read())
            else:
                logger.warning("Wildcard Datei  {} wurde nicht gefunden. Snips NLU inaktiv!", WILDCARD_FILE)

        if os.path.isfile(MERGED_FILE):
            logger.debug("\nChatbot-AI Template erfolgreich erstellt.")
            self.chatbot = Chat(MERGED_FILE)
        else:
            logger.error("\nChatbot-AI Template in {} konnte nicht gefunden werden!", MERGED_FILE)
        logger.debug('Chatbot aus {} initialisiert.', MERGED_FILE)
    
    def process(self, text, speaker):
        return self.chat.respond(text)
    
    
    
    
    

    def install(self, package):
        if hasattr(pip, 'main'):
            pip.main(['intall', package])
        else:
            pip._internal.main(['intall', package])
    
    def install_requirements(self, filename):
        retcode = 0
        with open(filename, 'r') as f:
            for line in f:
                pipcode = pip.main(['install', line.strip()])
                retcode = retcode or pipcode
        
        return retcode
    
    def get_count(self):
        return self.intent_count
    