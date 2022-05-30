
from loguru import logger
from chatbot import register_call
import util.GlobalVariables as GLOBALS
import yaml
import random
import os

@register_call("stop")
def stop(session_id = "general", dummy=0):
	cfg = None	
	config_path = os.path.join('intents','functions','stop','config_stop.yml')
	with open(config_path, "r", encoding='utf8') as ymlfile:
		cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
	
	LANGUAGE = GLOBALS.voice_assistant.cfg['assistant']['language']
	
	if cfg:
		result = random.choice(cfg['intent']['stop'][LANGUAGE]['not_saying_anything'])
		
		if GLOBALS.voice_assistant.tts.is_busy():
			GLOBALS.voice_assistant.tts.stop()
			result = random.choice(cfg['intent']['stop'][LANGUAGE]['be_silent'])
						
		return result
	else:
		logger.error("Konnte Konfigurationsdatei für Intent 'stop' nicht laden.")
		return ""
