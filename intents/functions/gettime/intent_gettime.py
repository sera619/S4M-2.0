from datetime import datetime
from loguru import logger
import pytz, global_variables, os, random, yaml

def gettime(place="default"):

	
	config_path = os.path.join('intents','functions','gettime','config_gettime.yml')
	cfg = None
	with open(config_path, "r", encoding='utf8') as ymlfile:
		cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
	
	if not cfg:
		logger.error("Konnte Konfigurationsdatei für gettime nicht lesen.")
		return ""
		
	LANGUAGE = global_variables.voice_assistant.cfg['assistant']['language']
	
	PLACE_UNKNOWN = random.choice(cfg['intent']['gettime'][LANGUAGE]['place_not_found'])
	
	PLACE_UNKNOWN = PLACE_UNKNOWN.format(place)

	country_timezone_map = {}
	for key, value in cfg['intent']['gettime']['timezones'].items():
		country_timezone_map[key] = value

	timezone = None
	now = datetime.now()
	for c in country_timezone_map:
		if place.strip().lower() in country_timezone_map[c]:
			timezone = pytz.timezone(c)
			break
	
	if timezone:
		now = datetime.now(timezone)
		TIME_AT_PLACE = random.choice(cfg['intent']['gettime'][LANGUAGE]['time_in_place'])
		TIME_AT_PLACE = TIME_AT_PLACE.format(str(now.hour), str(now.minute), place.capitalize())
		return TIME_AT_PLACE
	else:
		if place == "default":
			TIME_HERE = random.choice(cfg['intent']['gettime'][LANGUAGE]['time_here'])
			TIME_HERE = TIME_HERE.format(str(now.hour), str(now.minute))
			return TIME_HERE
	
	return PLACE_UNKNOWN