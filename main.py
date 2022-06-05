import yaml, time, pvporcupine, pyaudio, struct, os, sys, json, io, wx.adv, wx, constants, multiprocessing, global_variables
from loguru import logger
from audioplayer import AudioPlayer
from vosk import Model, SpkModel, KaldiRecognizer
import numpy as np
from usermgmt import UserMgmt
from TTS import Voice
from intentmgmt import IntentMgmt


# UI Komponenten für das Tray Icon

# Konstanten für das Tray Icon

from notification import Notification

CONFIG_FILE = "config.yml"

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *

from mainui import Ui_MainWindow
from splashscreenui import Ui_Splash
from circ_progress import ProgressCirc
from userui import UserUI

counter = 0
class SplashScreen(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_Splash()
		self.ui.setupUi(self)

		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground)

		self.progress = ProgressCirc()
		self.progress.height = 480
		self.progress.width = 480
		self.progress.value = 80
		self.progress.font_size = 23
		self.progress.setFixedSize(self.progress.width, self.progress.height)
		self.progress.move(10,10)
		self.progress.setParent(self.ui.centralwidget)
		self.progress.add_shadow(True)
		self.progress.enable_bg = True
		self.progress.show()

		self.timer = QTimer()
		self.timer.timeout.connect(self.update)
		self.timer.start(5)


		self.show()


	def update(self):
		global counter
		self.progress.setValue(counter)
		if counter >= 100:
			self.timer.stop()
			self.main = UserUI()
			self.main.show()
			#global_variables.voice_assistant = VoiceAssistant()
			#global_variables.voice_assistant.app.MainLoop()
			self.close()
		counter += 1




class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



	
	


# Eine Klasse, die die Logik unseres TrayIcons abbildet.
class TaskBarIcon(wx.adv.TaskBarIcon):
	def __init__(self, frame):
		self.frame = frame
		super(TaskBarIcon, self).__init__()
		self.set_icon(constants.TRAY_ICON_INITIALIZING, constants.TRAY_TOOLTIP + ": Initialisiere...")
		
	# Methode, um Menü-Einträge hinzuzufügen.
	def create_menu_item(self, menu, label, func):
		item = wx.MenuItem(menu, -1, label)
		menu.Bind(wx.EVT_MENU, func, id=item.GetId())
		menu.Append(item)
		return item

	# Wir erstellen ein Menü-Eintrag, der bei einem Rechtsklick gezeigt wird.
	def CreatePopupMenu(self):
		menu = wx.Menu()
		self.create_menu_item(menu, 'Beenden', self.on_exit)
		return menu

	# Ändern des Icons und des Hilfetextes
	def set_icon(self, path, tooltip=constants.TRAY_TOOLTIP):
		icon = wx.Icon(path)
		self.SetIcon(icon, tooltip)
	
	# Beenden der Applikation über das Menü
	def on_exit(self, event):
		if global_variables.voice_assistant:
			global_variables.voice_assistant.terminate()
			wx.CallAfter(self.Destroy)
			self.frame.Close()

# Die Klasse enthält die Logik für den Part der UI			
class MainApp(wx.App):
	def OnInit(self):
		frame = wx.Frame(None)
		self.SetTopWindow(frame)
		self.icon = TaskBarIcon(frame)
		self.Bind(wx.EVT_CLOSE, self.onCloseWindow)
		
		# Erstelle einen Timer, der die Hauptschleife unseres Assistenten ausführt
		self.timer = wx.Timer(self)
		self.Bind(wx.EVT_TIMER, self.update, self.timer)
		
		return True
		
	def update(self, event):
		if global_variables.voice_assistant:
			global_variables.voice_assistant.loop()

	def onCloseWindow(self, evt):
		self.icon.Destroy()
		evt.Skip()	

class VoiceAssistant:

	def __init__(self):
		logger.info("\nInitialisiere VoiceAssistant...")
		
		self.splash_screen = SplashScreen()
		self.splash_screen.show()

		logger.info("\nInitialisiere UI...")
		self.app = MainApp(clearSigInt=False, redirect=True, filename='log.txt')
				
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
		logger.info("\nVerwende Sprache {}", language)
		
		self.show_balloon = self.cfg['assistant']['show_balloon']
			
		logger.debug("\nInitialisiere Wake Word Erkennung...")
		self.wake_words = self.cfg['assistant']['wakewords']
		if not self.wake_words:
			self.wake_words = ['bumblebee']
		logger.debug("\nWake words are {}", ','.join(self.wake_words))
		self.porcupine = pvporcupine.create(keywords=self.wake_words)
		logger.debug("\nWake Word Erkennung wurde initialisiert.")
		
		logger.debug("\nInitialisiere Audioeingabe...")
		self.pa = pyaudio.PyAudio()
		
		self.audio_stream = self.pa.open(
			rate=self.porcupine.sample_rate,
			channels=1,
			format=pyaudio.paInt16,
			input=True,
			frames_per_buffer=self.porcupine.frame_length,
			input_device_index=0)
		logger.debug("\nAudiostream geöffnet.")
		
		self.volume = self.cfg["assistant"]["volume"]
		self.silenced_volume = self.cfg["assistant"]["silenced_volume"]

		logger.info("\nInitialisiere Sprachausgabe...")
		self.tts = Voice()
		voices = self.tts.get_voice_keys_by_language(language)
		if len(voices) > 0:
			logger.info('\nStimme {} gesetzt.', voices[0])
			self.tts.set_voice(voices[0])
		else:
			logger.warning("\nEs wurden keine Stimmen gefunden.")
		self.tts.set_volume(self.volume)
		self.tts.say("Sprachausgabe aktiviert.")
		if self.show_balloon:
			Notification.show('Initialisierung', 'Sprachausgabe aktiviert', ttl=4000)
			
		logger.debug("\nSprachausgabe initialisiert")
		
		logger.info("\nInitialisiere Spracherkennung...")
		stt_model = Model('./models/vosk-model-de-0.6')
		speaker_model = SpkModel('./models/vosk-model-spk-0.4')
		self.rec = KaldiRecognizer(stt_model, speaker_model, 16000)
		self.is_listening = False
		logger.info("\nInitialisierung der Spracherkennung abgeschlossen.")
		
		logger.info("\nInitialisiere Benutzerverwaltung...")
		self.user_management = UserMgmt(init_dummies=True)
		self.allow_only_known_speakers = self.cfg["assistant"]["allow_only_known_speakers"]
		logger.info("\nBenutzerverwaltung initialisiert")
		
		# Initialisiere den Audio-Player
		self.audio_player = AudioPlayer()
		self.audio_player.set_volume(self.volume)
				
		logger.info("\nInitialisiere Intent-Management...")
		self.intent_management = IntentMgmt()
		logger.info('\n{} intents geladen', self.intent_management.get_count())
		
		self.callbacks = self.intent_management.register_callbacks()
		logger.info('\n{} callbacks gefunden', len(self.callbacks))
		self.tts.say("Initialisierung abgeschlossen")
		if self.show_balloon:
			Notification.show('Initialisierung', 'Abgeschlossen', ttl=4000)

		self.app.icon.set_icon(constants.TRAY_ICON_IDLE, constants.TRAY_TOOLTIP + ": Bereit")
		timer_start_result = self.app.timer.Start(milliseconds=1, oneShot=wx.TIMER_CONTINUOUS)
		logger.info("\nTimer erfolgreich gestartet? {}", timer_start_result)
	
	def __detectSpeaker__(self, input):
		bestSpeaker = None
		bestCosDist = 100
		for speaker in self.user_management.speaker_table.all():
			nx = np.array(speaker.get('voice'))
			ny = np.array(input)
			cosDist = 1 - np.dot(nx, ny) / np.linalg.norm(nx) / np.linalg.norm(ny)
			if (cosDist < bestCosDist):
				if (cosDist < 0.3):
					bestCosDist = cosDist
					bestSpeaker = speaker.get('name')
		return bestSpeaker
	
	def terminate(self):
		logger.debug('\nBeginne Aufräumarbeiten...')
		
		self.app.timer.Stop()
		
		global_variables.voice_assistant.cfg["assistant"]["volume"] = global_variables.voice_assistant.volume
		global_variables.voice_assistant.cfg["assistant"]["silenced_volume"] = global_variables.voice_assistant.silenced_volume
		with open(CONFIG_FILE, 'w') as f:
			yaml.dump(global_variables.voice_assistant.cfg, f, default_flow_style=False, sort_keys=False)		
		
		if global_variables.voice_assistant.porcupine:
			global_variables.voice_assistant.porcupine.delete()
			
		if global_variables.voice_assistant.audio_stream is not None:
			global_variables.voice_assistant.audio_stream.close()
			
		if global_variables.voice_assistant.audio_player is not None:
			global_variables.voice_assistant.audio_player.stop()			
			
		if global_variables.voice_assistant.pa is not None:
			global_variables.voice_assistant.pa.terminate()			
	
	def loop(self):		
		pcm = global_variables.voice_assistant.audio_stream.read(global_variables.voice_assistant.porcupine.frame_length)
		pcm_unpacked = struct.unpack_from("h" * global_variables.voice_assistant.porcupine.frame_length, pcm)		
		keyword_index = global_variables.voice_assistant.porcupine.process(pcm_unpacked)
		if keyword_index >= 0:
			logger.info("\nWake Word {} wurde verstanden.", global_variables.voice_assistant.wake_words[keyword_index])
			global_variables.voice_assistant.is_listening = True
			
		if global_variables.voice_assistant.is_listening:
			if not global_variables.voice_assistant.tts.is_busy():
				self.app.icon.set_icon(constants.TRAY_ICON_LISTENING, constants.TRAY_TOOLTIP + ": Ich höre...")
		
			if global_variables.voice_assistant.audio_player.is_playing():
				global_variables.voice_assistant.audio_player.set_volume(global_variables.voice_assistant.silenced_volume)
					
			if global_variables.voice_assistant.rec.AcceptWaveform(pcm):
				recResult = json.loads(global_variables.voice_assistant.rec.Result())
				
				speaker = global_variables.voice_assistant.__detectSpeaker__(recResult['spk'])
				if (speaker == None) and (global_variables.voice_assistant.allow_only_known_speakers == True):
					logger.info("\nIch kenne deine Stimme nicht und darf damit keine Befehle von dir entgegen nehmen.")
					global_variables.voice_assistant.current_speaker = None
				else:
					if speaker:
						logger.debug("\nSprecher ist {}", speaker)
					global_variables.voice_assistant.current_speaker = speaker
					global_variables.voice_assistant.current_speaker_fingerprint = recResult['spk']
					sentence = recResult['text']
					logger.debug('\nIch habe verstanden "{}"', sentence)
					
					output = global_variables.voice_assistant.intent_management.process(sentence, speaker)
					global_variables.voice_assistant.tts.say(output)
					if self.show_balloon:
						Notification.show("Interaktion", "Eingabe (" + speaker + "): " + sentence + ". Ausgabe: " + output, ttl=4000)
					
					global_variables.voice_assistant.is_listening = False
					global_variables.voice_assistant.current_speaker = None
		
		else:
		
			if not global_variables.context is None:
				if not global_variables.voice_assistant.tts.is_busy():
					global_variables.voice_assistant.is_listening = True
			else:		
				if not global_variables.voice_assistant.tts.is_busy():
					self.app.icon.set_icon(constants.TRAY_ICON_IDLE, constants.TRAY_TOOLTIP + ": Bereit")
				global_variables.voice_assistant.audio_player.set_volume(global_variables.voice_assistant.volume)
						
				for cb in global_variables.voice_assistant.callbacks:
					output = cb()
					
					if output:
						if not global_variables.voice_assistant.tts.is_busy():
					
							if global_variables.voice_assistant.audio_player.is_playing():
								global_variables.voice_assistant.audio_player.set_volume(global_variables.voice_assistant.audio_player.set_volume(global_variables.voice_assistant.silenced_volume))
							
							global_variables.voice_assistant.tts.say(output)
							if self.show_balloon:
								Notification.show('Callback', output, ttl=4000)
							
							cb(True)
							
							global_variables.voice_assistant.audio_player.set_volume(global_variables.voice_assistant.volume)

if __name__ == '__main__':
	multiprocessing.set_start_method('spawn')
	app = QApplication(sys.argv)
	

	splash = SplashScreen()	
	splash.show()
	sys.exit(app.exec())	

