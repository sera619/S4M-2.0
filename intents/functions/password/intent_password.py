from loguru import logger
from chatbot import register_call
import global_variables
import yaml
import random
import os
from pykeepass import PyKeePass
from pynput.keyboard import Key, Listener, Controller as keyboard_controller
from fuzzywuzzy import fuzz
import json
import numpy as np

@register_call("getPassword")
def getPassword(session_id = "general", entry="none"):
	cfg = None
	
	config_path = os.path.join('intents','functions','password','config_password.yml')
	with open(config_path, "r", encoding='utf-8') as ymlfile:
		cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
	
	LANGUAGE = global_variables.voice_assistant.cfg['assistant']['language']
	
	db_file = cfg['intent']['password']['db_file']
	key_file = cfg['intent']['password']['key_file']
	typed_pw = cfg['intent']['password'][LANGUAGE]['typed_pw']
	
	db_file = os.path.join('intents','functions','password',db_file)
	key_file = os.path.join('intents','functions','password',key_file)
	
	if not os.path.exists(db_file):
		return cfg['intent']['password'][LANGUAGE]['db_not_found']
		
	if not os.path.exists(key_file):
		return cfg['intent']['password'][LANGUAGE]['key_not_found']

	UNKNOWN_ENTRY = random.choice(cfg['intent']['password'][LANGUAGE]['unknown_entry'])
	UNKNOWN_ENTRY = UNKNOWN_ENTRY.format(entry)
	
	NO_VOICE_MATCH = cfg['intent']['password'][LANGUAGE]['no_voice_match']
	
	if cfg:
		try:
			kp = PyKeePass(os.path.abspath(db_file), keyfile=os.path.abspath(key_file))
		except Exception as e:
			return cfg['intent']['password'][LANGUAGE]['could_not_access_keystore']

		fp_entry = kp.find_entries(title='_fingerprint', first=True)
		if fp_entry:
			a = json.loads(fp_entry.notes)
			b = global_variables.voice_assistant.current_speaker_fingerprint			
			nx = np.array(a)
			ny = np.array(b)
			cosDist = 1 - np.dot(nx, ny) / np.linalg.norm(nx) / np.linalg.norm(ny)
			if (cosDist >= 0.3):
				return NO_VOICE_MATCH
				
		entries = kp.entries
		
		for title in entries:
			ratio = fuzz.ratio(title.title.lower(), entry.lower())
			logger.info("Übereinstimmung von {} und {} ist {}%", title.title, entry, ratio)
			if ratio > 70:
		
				if (title):
					keyboard = keyboard_controller()
					keyboard.type(title.password)
					return typed_pw.format(title.title)

		return UNKNOWN_ENTRY
	else:
		logger.error("Konnte Konfigurationsdatei für Intent 'password' nicht laden.")
		return 
		
		
@register_call("getUsername")
def getUsername(session_id = "general", entry="none"):
	cfg = None

	config_path = os.path.join('intents','functions','password','config_password.yml')
	with open(config_path, "r", encoding='utf-8') as ymlfile:
		cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
	
	LANGUAGE = global_variables.voice_assistant.cfg['assistant']['language']
	
	db_file = cfg['intent']['password']['db_file']
	key_file = cfg['intent']['password']['key_file']
	
	db_file = os.path.join('intents','functions','password',db_file)
	key_file = os.path.join('intents','functions','password',key_file)
	
	if not os.path.exists(db_file):
		return cfg['intent']['password'][LANGUAGE]['db_not_found']
		
	if not os.path.exists(key_file):
		return cfg['intent']['password'][LANGUAGE]['key_not_found']

	UNKNOWN_ENTRY = random.choice(cfg['intent']['password'][LANGUAGE]['unknown_entry'])
	UNKNOWN_ENTRY = UNKNOWN_ENTRY.format(entry)
	
	NO_VOICE_MATCH = cfg['intent']['password'][LANGUAGE]['no_voice_match']
	
	if cfg:
		try:
			kp = PyKeePass(os.path.abspath(db_file), keyfile=os.path.abspath(key_file))
		except Exception as e:
			return cfg['intent']['password'][LANGUAGE]['could_not_access_keystore']
		
		fp_entry = kp.find_entries(title='_fingerprint', first=True)
		if fp_entry:
			a = json.loads(fp_entry.notes)
			b = global_variables.voice_assistant.current_speaker_fingerprint			
			nx = np.array(a)
			ny = np.array(b)
			cosDist = 1 - np.dot(nx, ny) / np.linalg.norm(nx) / np.linalg.norm(ny)
			if (cosDist >= 0.3):
				return NO_VOICE_MATCH

				
		entries = kp.entries
		
		for title in entries:
			ratio = fuzz.ratio(title.title.lower(), entry.lower())
			logger.info("Übereinstimmung von {} und {} ist {}%", title.title, entry, ratio)
			if ratio > 70:
		
				if (title):
					return title.username

		return UNKNOWN_ENTRY
	else:
		logger.error("Konnte Konfigurationsdatei für Intent 'password' nicht laden.")
		return ""		