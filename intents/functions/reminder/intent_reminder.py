from datetime import datetime
import pytz
import global_variables
import os
import random
import yaml
from loguru import logger

from dateutil.parser import parse
from num2words import num2words
from tinydb import TinyDB, Query

reminder_db_path = os.path.join('intents','functions','reminder','reminder_db.json')
reminder_db = TinyDB(reminder_db_path)
reminder_table = reminder_db.table('reminder')

CONFIG_PATH = os.path.join('intents','functions','reminder','config_reminder.yml')

def callback(processed=False):
	LANGUAGE = global_variables.voice_assistant.cfg['assistant']['language']
	cfg = None
	with open(CONFIG_PATH, "r", encoding='utf8') as ymlfile:
		cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
	
	if not cfg:
		logger.error("Konnte Callback nicht aufrufen, Konfiguration ist nicht lesbar.")
		return None
	
	all_reminders = reminder_table.all()
	for r in all_reminders:
		
		parsed_time = parse(r['time'])
		now = datetime.now(parsed_time.tzinfo)
		if parsed_time <= now:
			res = ''
			
			if r['speaker']:
				res += r['speaker'] + ' '
			
			if r['kind'] == 'inf':
				REMINDER_TEXT = random.choice(cfg['intent']['reminder'][LANGUAGE]['execute_reminder_infinitive'])
				REMINDER_TEXT = REMINDER_TEXT.format(r['msg'])
				res += REMINDER_TEXT
			elif r['kind'] == 'to':
				REMINDER_TEXT = random.choice(cfg['intent']['reminder'][LANGUAGE]['execute_reminder_to'])
				REMINDER_TEXT = REMINDER_TEXT.format(r['msg'])
				res += REMINDER_TEXT			
			else:
				REMINDER_TEXT = random.choice(cfg['intent']['reminder'][LANGUAGE]['execute_reminder'])
				res += REMINDER_TEXT
				
			if processed:
				logger.info('Der Reminder für {} am {} mit Inhalt {} wird nun gelöscht.', r['speaker'], r['time'], r['msg'])
				Reminder_Query = Query()
				reminder_table.remove(Reminder_Query.speaker == r['speaker'] and Reminder_Query.timt == r['time'] and Reminder_Query.msg == r['msg'] and Reminder_Query.kind == r['kind'])
				return None
			else:
				return res
			
	return None

def spoken_date(datetime, lang):
	hours = str(datetime.hour)
	minutes = "" if datetime.minute == 0 else str(datetime.minute)
	day = num2words(datetime.day, lang=lang, to="ordinal")
	month = num2words(datetime.month, lang=lang, to="ordinal")
	year = "" if datetime.year == datetime.now().year else str(datetime.year)
	
	if lang == 'de':
		day += 'n'
		month += 'n'
		
	return hours, minutes, day, month, year

def reminder(time=None, reminder_to=None, reminder_infinitive=None):

	speaker = global_variables.voice_assistant.current_speaker

	LANGUAGE = global_variables.voice_assistant.cfg['assistant']['language']
	cfg = None
	with open(CONFIG_PATH, "r", encoding='utf8') as ymlfile:
		cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)


	if not cfg:
		logger.error("Konnte Konfigurationsdatei für reminder nicht lesen.")
		return ""
		
	NO_TIME_GIVEN = random.choice(cfg['intent']['reminder'][LANGUAGE]['no_time_given'])
		
	result = ""
	if speaker:
		result = speaker + ', '

	if not time:
		return result + NO_TIME_GIVEN

	parsed_time = parse(time)
	
	hours, minutes, day, month, year = spoken_date(parsed_time, LANGUAGE)
	
	if datetime.now().date() == parsed_time.date():
		if reminder_to:
			SAME_DAY_TO = random.choice(cfg['intent']['reminder'][LANGUAGE]['reminder_same_day_to'])
			SAME_DAY_TO = SAME_DAY_TO.format(hours, minutes, reminder_to)
			result = result + " " + SAME_DAY_TO
			reminder_table.insert({'time':time, 'kind':'to', 'msg':reminder_to, 'speaker':speaker})
		elif reminder_infinitive:
			SAME_DAY_INFINITIVE = random.choice(cfg['intent']['reminder'][LANGUAGE]['reminder_same_day_infinitive'])
			SAME_DAY_INFINITIVE = SAME_DAY_INFINITIVE.format(hours, minutes, reminder_infinitive)
			result = result + " " + SAME_DAY_INFINITIVE
			reminder_table.insert({'time':time, 'kind':'inf', 'msg':reminder_infinitive, 'speaker':speaker})
		else:
			SAME_DAY_NO_ACTION = random.choice(cfg['intent']['reminder'][LANGUAGE]['reminder_same_day_no_action'])
			SAME_DAY_NO_ACTION = SAME_DAY_NO_ACTION.format(hours, minutes)
			result = result + " " + SAME_DAY_NO_ACTION
			reminder_table.insert({'time':time, 'kind':'none', 'msg':'', 'speaker':speaker})
	else:
		if reminder_to:
			TO = random.choice(cfg['intent']['reminder'][LANGUAGE]['reminder_to'])
			TO = TO.format(day, month, year, hours, minutes, reminder_to)
			result = result + " " + TO
			reminder_table.insert({'time':time, 'kind':'to', 'msg':reminder_to, 'speaker':speaker})
		elif reminder_infinitive:
			INFINITIVE = random.choice(cfg['intent']['reminder'][LANGUAGE]['reminder_infinitive'])
			INFINITIVE = INFINITIVE.format(day, month, year, hours, minutes, reminder_infinitive)
			result = result + " " + INFINITIVE
			reminder_table.insert({'time':time, 'kind':'inf', 'msg':reminder_infinitive, 'speaker':speaker})
		else:
			# Es wurde nicht angegeben, an was erinnert werden soll
			NO_ACTION = random.choice(cfg['intent']['reminder'][LANGUAGE]['reminder_no_action'])
			NO_ACTION = NO_ACTION.format(day, month, year, hours, minutes)
			result = result + " " + NO_ACTION
			reminder_table.insert({'time':time, 'kind':'none', 'msg':'', 'speaker':speaker})
			
	logger.info("Reminder mit Inhalt {} erkannt.", result)
			
	return result