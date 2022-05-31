import os,sys, yaml, json, random
from loguru import logger
import global_variables
from chatbot import Chat, register_call
from pygame import mixer


@register_call('animalSound')
def animalSound(session_id = "general", animal="none"):
    config_path = os.path.join('intents','functions','animalsound','config_animalsounds.yml')
    ogg_path = os.path.join('intents', 'functions', 'animalsound', 'animals')
    cfg = None
    
    with open(config_path, "r", encoding='utf8') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

    if not cfg:
        logger.error('\nKonnte Konfigurationsdatei für Intent "animalSound" nicht laden.')
        return ""
    
    LANGUAGE = global_variables.voice_assistant.cfg['assistant']['language']
    ANIMAL_UNKOWN = random.choice(cfg['animal_unknown'][LANGUAGE])

    animals = {}

    for key, value in cfg['intent']['animalsounds']['animals'].items():
        animals[key] = value

    for a in animals:
        if animal.strip().lower() in animals[a]:
            ogg_file = os.path.join(ogg_path, a + '.mp3')
            if mixer.music.is_busy():
                mixer.music.stop()
            mixer.music.load(ogg_file)
            mixer.music.play()
            return ""
    return ANIMAL_UNKOWN