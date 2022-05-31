from loguru import logger
from chatbot import register_call
import global_variables
import random
import os
import yaml
import geocoder

@register_call("location")
def location(session_id = "general", dummy=0):

	config_path = os.path.join('intents','functions','location','config_location.yml')
	cfg = None
	
	with open(config_path, "r", encoding='utf8') as ymlfile:
		cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
	
	if not cfg:
		logger.error("Konnte Konfigurationsdatei für die Lokalisierung nicht lesen.")
		return ""
		
	# Holen der Sprache aus der globalen Konfigurationsdatei
	LANGUAGE = global_variables.voice_assistant.cfg['assistant']['language']
	
	YOU_ARE_HERE = random.choice(cfg['intent']['location'][LANGUAGE]['youarehere'])
	
	# Ermittle den Standort mittels IP
	loc = geocoder.ip('me')
	return random.choice(YOU_ARE_HERE).format(loc.city)