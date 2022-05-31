from loguru import logger
import yaml
import time
import pvporcupine
import pyaudio
import struct
import os
import sys
import json
import tinydb
import io
import numpy as np
from vosk import Model, SpkModel, KaldiRecognizer
from TTS import Voice
import multiprocessing
from usermgmt import UserMgmt
from intentmgmt import IntentMgmt
from pygame import mixer

CONFIG_FILE = "config.yml"
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"


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
        logger.info("\nVerwende Sprache {}", language)

        # Wakeword init
        logger.debug("\nInitialisiere Wake Word Erkennung...")
        self.wake_words = self.cfg['assistant']['wakewords']
        if not self.wake_words:
            self.wake_words = ['bumblebee']
        logger.debug("\nWake words are {}", ','.join(self.wake_words))
        self.porcupine = pvporcupine.create(keywords=self.wake_words)
        logger.debug("\nWake Word Erkennung wurde initialisiert.")

        # Audio Input
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

        # speaker recognition
        logger.info("\nInitialisiere Sprachausgabe...")
        self.tts = Voice()
        voices = self.tts.get_voice_keys_by_language(language)
        if len(voices) > 0:
            logger.info('\nStimme {} gesetzt.', voices[0])
            self.tts.set_voice(voices[0])
        else:
            logger.warning("\nEs wurden keine Stimmen gefunden.")
        self.tts.say("\nSprachausgabe aktiviert.")
        logger.debug("\nSprachausgabe initialisiert")

        # Voice recognition
        logger.info("\nInitialisiere Spracherkennung...")
        stt_model = Model('./models/vosk-model-de-0.6')
        speaker_model = SpkModel('./models/vosk-model-spk-0.4')
        self.rec = KaldiRecognizer(stt_model, speaker_model, 16000)
        self.is_listening = False
        logger.info("\nInitialisierung der Spracherkennung abgeschlossen.")

        # User Management
        logger.info("\nInitialisiere Benutzerverwaltung...")
        self.user_management = UserMgmt(init_dummies=True)
        self.allow_only_known_speakers = self.cfg["assistant"]["allow_only_known_speakers"]
        logger.info("\nBenutzerverwaltung initialisiert")

        # audio player
        mixer.init()
        self.volume = self.cfg["assistant"]["volume"]
        mixer.music.set_volume(self.volume)

        # Intent management
        logger.info("\nInitialisiere Intent-Management...")
        self.intent_management = IntentMgmt()
        logger.info('\n{} intents geladen', self.intent_management.get_count())
        self.tts.say("Initialisierung abgeschlossen")

    def __detectSpeaker__(self, input):
        bestSpeaker = None
        bestCosDist = 100
        for speaker in self.user_management.speaker_table.all():
            nx = np.array(speaker.get('voice'))
            ny = np.array(input)
            cosDist = 1 - np.dot(nx, ny) / \
                np.linalg.norm(nx) / np.linalg.norm(ny)
            if (cosDist < bestCosDist):
                if (cosDist < 0.3):
                    bestCosDist = cosDist
                    bestSpeaker = speaker.get('name')
        return bestSpeaker

    def run(self):
        logger.info("\nVoiceAssistant Instanz wurde gestartet.")
        try:
            while True:

                pcm = global_variables.voice_assistant.audio_stream.read(global_variables.voice_assistant.porcupine.frame_length)
                pcm_unpacked = struct.unpack_from("h" * global_variables.voice_assistant.porcupine.frame_length, pcm)
                keyword_index = global_variables.voice_assistant.porcupine.process(pcm_unpacked)
                if keyword_index >= 0:
                    logger.info("\nWake Word {} wurde verstanden.",global_variables.voice_assistant.wake_words[keyword_index])
                    global_variables.voice_assistant.is_listening = True

                    if global_variables.voice_assistant.is_listening:

                        if mixer.music.get_busy():
                            mixer.music.set_volume(0.1)

                        if global_variables.voice_assistant.rec.AcceptWaveform(pcm):
                            recResult = json.loads(
                                global_variables.voice_assistant.rec.Result())

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

                                # Lasse den Assistenten auf die Spracheingabe reagieren
                                output = global_variables.voice_assistant.intent_management.process(sentence, speaker)
                                global_variables.voice_assistant.tts.say(output)

                                global_variables.voice_assistant.is_listening = False
                                global_variables.voice_assistant.current_speaker = None

                    else:
                        mixer.music.set_volume(global_variables.voice_assistant.volume)

                        for cb in global_variables.voice_assistant.callbacks:
                            output = cb()

                            if output:
                                if not global_variables.voice_assistant.tts.is_busy():

                                    if mixer.music.get_busy():
                                        mixer.music.set_volume(0.1)

                                    global_variables.voice_assistant.tts.say(output)
                                    logger.debug("\n>>> Sprachausgabe: {}", output)
                                    cb(True)

                                    # TODO Reset Volume

        except KeyboardInterrupt:
            logger.debug("\nPer Keyboard beendet")
        finally:
            logger.debug('\nBeginne Aufräumarbeiten...')
            if global_variables.voice_assistant.porcupine:
                global_variables.voice_assistant.porcupine.delete()

            if global_variables.voice_assistant.audio_stream is not None:
                global_variables.voice_assistant.audio_stream.close()

            if global_variables.voice_assistant.pa is not None:
                global_variables.voice_assistant.pa.terminate()


if __name__ == '__main__':
    import global_variables
    multiprocessing.set_start_method('spawn')
    global_variables.voice_assistant = VoiceAssistant()
    logger.info("\nAnwendung wurde gestartet")
    global_variables.voice_assistant.run()
