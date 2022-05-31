from loguru import logger
from chatbot import register_call
import global_variables
import yaml
import random
import os
import wikipedia

@register_call("wiki")
def wiki(session_id = "general", query="none"):
	cfg = None
	
	config_path = os.path.join('intents','functions','wiki','config_wiki.yml')
	with open(config_path, "r", encoding='utf8') as ymlfile:
		cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
	
	LANGUAGE = global_variables.voice_assistant.cfg['assistant']['language']
	
	if LANGUAGE:
		wikipedia.set_lang(LANGUAGE)

	UNKNOWN_ENTITY = random.choice(cfg['intent']['wiki'][LANGUAGE]['unknown_entity'])
	UNKNOWN_ENTITY = UNKNOWN_ENTITY.format(query)
	
	if cfg:
		query = query.strip()
		try:
			return wikipedia.summary(query, sentences=1)
		except Exception:
			for new_query in wikipedia.search(query):
				try:
					return wikipedia.summary(new_query)
				except Exception:
					pass
		return UNKNOWN_ENTITY
	else:
		logger.error("Konnte Konfigurationsdatei für Intent 'wikipedia' nicht laden.")
		return ""