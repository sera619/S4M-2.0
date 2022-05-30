"""
	______________________________________________________________
							   S4M 2.0
						    Voice Assistant
	--------------------------------------------------------------
				This software is developed by S3R43o3.
	Do not copy or modify without the permission of the developer.
						  	2022 © S3R43o3
	______________________________________________________________

"""

import pyttsx3, yaml, datetime, pvporcupine, pyaudio, struct, os, sys, json, text2numde, multiprocessing, numpy, io, pytz
from loguru import logger
from res.TTS import Voice
from vosk import Model, SpkModel, KaldiRecognizer
from chatbot import Chat, register_call
from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_DE
from snips_nlu.dataset import Dataset
from conf.IntentManagement import IntentManagement 
from conf.UserManagement import UserManagement


SAMPLE_RATE = 16000
FRAME_LENGTH = 512
CONFIG_FILE = 'config.yml'

class VoiceAssistant():

	def __init__(self):
		logger.info("\nInitialisiere VoiceAssistant...")

		logger.debug("\nLese Konfiguration...")
		global CONFIG_FILE
		with open(CONFIG_FILE, "r", encoding='utf8') as ymlfile:
			self.cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)
		if self.cfg:
			logger.debug("\nKonfiguration gelesen.")
		else:
			logger.debug("\nKonfiguration konnte nicht gelesen werden.")
			sys.exit(1)
		language = self.cfg['assistant']['language']
		if not language:
			language = "de"
		logger.debug("\nVerwende Sprache {}", language)
			
		logger.debug("\nInitialisiere Wake Word Erkennung...")
		self.wake_words = self.cfg['assistant']['wakewords']
		
		if not self.wake_words:
			self.wake_words = ['bumblebee']
		logger.debug("\nWake Words sind {}", ','.join(self.wake_words))
		self.porcupine = pvporcupine.create(keywords=self.wake_words)
		# Sensitivities (sensitivities=[0.6, 0.35]) erweitert oder schränkt
		# den Spielraum bei der Intepretation der Wake Words ein
		logger.debug("\nWake Word Erkennung wurde initialisiert.")
		

		logger.debug("\nInitialisiere Audioeingabe...")
		self.pa = pyaudio.PyAudio()
		
		# Get input device list 
		# for i in range(self.pa.get_device_count()):
		# 	logger.debug('id: {}, name: {}', self.pa.get_device_info_by_index(i).get('index'),
		# 		self.pa.get_device_info_by_index(i).get('name'))
		
		self.audio_stream = self.pa.open(
			rate=self.porcupine.sample_rate,
			channels=1,
			format=pyaudio.paInt16,
			input=True,
			frames_per_buffer=self.porcupine.frame_length,
			input_device_index=0)
		logger.debug("\nAudiostream geöffnet.")

		# Initialisiere TTS
		logger.debug("\nInitialisiere Sprachausgabe...")
		self.tts = Voice()
		voices = self.tts.get_voice_keys_by_language(language)
		if len(voices) > 0:
			logger.info('\nStimme {} gesetzt.', voices[0])
			self.tts.set_voice(voices[0])
		else:
			logger.warning("\nEs wurden keine Stimmen gefunden.")
		logger.debug("\nSprachausgabe initialisiert")

		logger.debug("\nInitialisiere Spracherkennung...")
		stt_model = Model("./models/vosk-model-de-0.6")
		speaker_model = SpkModel("./models/vosk-model-spk-0.4")
		self.rec = KaldiRecognizer(stt_model, speaker_model,16000)
		self.is_listening = False
		logger.debug("\nSpracherkennung initialisiert")
		
		logger.debug("\nInitialisiere Benutzerverwaltung...")
		self.user_management = UserManagement(init_dummies=True)
		self.allow_trusted_user = self.cfg['assistant']['allow_only_trusted_speaker']
		logger.debug("\nBenutzerverwaltung initialisiert")
		

		logger.debug("\nInitialisiere Intent-Management...")
		self.intent_management = IntentManagement()
		logger.debug("\n{} intents initialisiert", self.intent_management.get_count())

		# logger.debug("\nInitialisiere Chatbot...")
		# self.nlu_enginge = None
		# dataset = Dataset.from_yaml_files("de", ['./temp/stop_dataset.yaml', './temp/time_dataset.yaml'])
		# nlu_engine = SnipsNLUEngine(config=CONFIG_DE)
		# self.nlu_enginge = nlu_engine.fit(dataset)

		# if not self.nlu_enginge:
		# 	logger.error('\nKonnte Dialog-Engine nicht laden!')
		# 	sys.exit(1)
		# else:
		# 	logger.debug('\nDialog Metadaten: {} geladen.', self.nlu_enginge.dataset_metadata)
		# logger.debug("\nChatbot initialisiert")

		
		self.tts.say("\nInitialisierung abgeschlossen")


	def __detect_speaker__(self, input):
		bestSpeaker = None
		bestCosDist = 100
		for speaker in self.user_management.speaker_table.all():
			nx = numpy.array(speaker.get('voice'))
			ny = numpy.array(input)
			cosDist = numpy.dot(nx,ny) / numpy.linalg.norm(nx) / numpy.linalg.norm(ny)
			if (cosDist < bestCosDist):
				if (cosDist < 0.5):
					bestCosDist = cosDist
					bestSpeaker = speaker.get('name')
		return bestSpeaker
		
	def run(self):
		logger.debug("\nVoiceAssistant Instanz wurde gestartet.")
		try:
			while True:
			
				pcm = GLOBALS.voice_assistant.audio_stream.read(GLOBALS.voice_assistant.porcupine.frame_length)
				pcm_unpacked = struct.unpack_from("h" * GLOBALS.voice_assistant.porcupine.frame_length, pcm)		
				keyword_index = GLOBALS.voice_assistant.porcupine.process(pcm_unpacked)
				if keyword_index >= 0:
					logger.info("Wake Word {} wurde verstanden.", GLOBALS.voice_assistant.wake_words[keyword_index])
					GLOBALS.voice_assistant.is_listening = True
					
				# Spracherkennung
				if GLOBALS.voice_assistant.is_listening:
					if GLOBALS.voice_assistant.rec.AcceptWaveform(pcm):
						recResult = json.loads(GLOBALS.voice_assistant.rec.Result())
						
						speaker = GLOBALS.voice_assistant.__detectSpeaker__(recResult['spk'])
						if (speaker == None) and (GLOBALS.voice_assistant.allow_only_known_speakers == True):
							logger.info("Ich kenne deine Stimme nicht und darf damit keine Befehle von dir entgegen nehmen.")
							GLOBALS.voice_assistant.current_speaker = None
						else:
							if speaker:
								logger.debug("Sprecher ist {}", speaker)
							GLOBALS.voice_assistant.current_speaker = speaker
							GLOBALS.voice_assistant.current_speaker_fingerprint = recResult['spk']
							sentence = recResult['text']
							logger.debug('Ich habe verstanden "{}"', sentence)
							
							# Lasse den Assistenten auf die Spracheingabe reagieren
							output = GLOBALS.voice_assistant.intent_management.process(sentence, speaker)
							GLOBALS.voice_assistant.tts.say(output)
							
							GLOBALS.voice_assistant.is_listening = False
							GLOBALS.voice_assistant.current_speaker = None
						



		except KeyboardInterrupt:
			logger.debug("\nPer Keyboard beendet")
		finally:
			logger.debug('\nBeginne Aufräumarbeiten...')
			if self.porcupine:
				self.porcupine.delete()
				
			if self.audio_stream is not None:
				self.audio_stream.close()
				
			if self.pa is not None:
				self.pa.terminate()

if __name__ == '__main__':
	import util.GlobalVariables as GLOBALS
	multiprocessing.set_start_method('spawn')
	GLOBALS.voice_assistant = VoiceAssistant()
	#va = VoiceAssistant()
	logger.debug("\nAnwendung wurde gestartet")
	GLOBALS.voice_assistant.run()
