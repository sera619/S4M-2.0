import pyttsx3, yaml, time, pvporcupine, pyaudio, struct, os, sys, json, text2numde, multiprocessing, numpy

from loguru import logger
from res.TTS import Voice
from vosk import Model, SpkModel, KaldiRecognizer
from conf.UserManagement import UserManagement
from chatbot import Chat, register_call

SAMPLE_RATE = 16000
FRAME_LENGTH = 512

CONFIG_FILE = 'config.yml'

@register_call
def getTime(session_id  = ""):
	return time.strftime("%H:%M:%S")

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
		language = self.cfg['language']
		if not language:
			language = "de"
		logger.debug("\nVerwende Sprache {}", language)
			
		logger.debug("\nInitialisiere Wake Word Erkennung...")
		self.wake_words = self.cfg['wakewords']
		
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
		self.allow_trusted_user = self.cfg['allow_only_trusted_speaker']
		logger.debug("\nBenutzerverwaltung initialisiert")
		
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
			
				pcm = self.audio_stream.read(self.porcupine.frame_length)
				pcm_unpacked = struct.unpack_from("h" * self.porcupine.frame_length, pcm)		
				keyword_index = self.porcupine.process(pcm_unpacked)
				if keyword_index >= 0:
					logger.debug("\nWake Word {} wurde verstanden.", self.wake_words[keyword_index])
					self.tts.say("Was kann ich für dich tun?")
					self.is_listening = True

				if self.is_listening:
					if self.rec.AcceptWaveform(pcm):
						recResult = json.loads(self.rec.Result())
						sentence = recResult['text']
						with open('recs.txt', 'w') as file:
							file.write(sentence+'\n')

						logger.debug('recResult: {}', recResult)
						speaker = self.__detect_speaker__(recResult['spk'])
						if (speaker == None) and (self.allow_trusted_user):
							logger.warning("Ich kenne deine Stimme nicht")
							self.current_speaker = None
							self.is_listening = False
						else:
							if speaker:
								logger.debug('Sprecher ist {}', speaker)
							
							self.current_speaker = speaker

							logger.debug('\nIch habe verstanden "{}"', sentence)
							if sentence == 'ende':
								exit()
							self.is_listening = False
							self.current_speaker = None
						



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
	multiprocessing.set_start_method('spawn')

	va = VoiceAssistant()
	logger.info("Anwendung wurde gestartet")
	va.run()
