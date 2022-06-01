from loguru import logger
from chatbot import register_call
import global_variables
import random
import os
import yaml

import text2numde
from fuzzywuzzy import fuzz

def musicstream(station=None):

	config_path = os.path.join('intents','functions','musicstream','config_musicstream.yml')
	cfg = None
	
	with open(config_path, "r", encoding='utf8') as ymlfile:
		cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
	
	if not cfg:
		logger.error("Konnte Konfigurationsdatei für das Musikstreaming nicht lesen.")
		return ""
		
	LANGUAGE = global_variables.voice_assistant.cfg['assistant']['language']
	
	UNKNOWN_STATION = random.choice(cfg['intent']['musicstream'][LANGUAGE]['unknown_station'])
	
	station = text2numde.sentence2num(station)
	
	station = "".join(station.split())
	
	station_stream = None
	for key, value in cfg['intent']['musicstream']['stations'].items():
	
		ratio = fuzz.ratio(station.lower(), key.lower())
		logger.info("Übereinstimmung von {} und {} ist {}%", station, key, ratio)
		if ratio > 70:
			station_stream = value
			break

	if station_stream is None:
		return UNKNOWN_STATION
		
	#if mixer.music.get_busy():
		#mixer.music.stop()
	#sound=mixer.Sound(station_stream)
	#sound.play()
	#mixer.music.load(station_stream)
	#mixer.music.play()
	#global_variables.voice_assistant.play_audio(station_stream)
	global_variables.voice_assistant.audio_player.play_stream(station_stream)
		
	return ""	