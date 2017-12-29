#!/usr/bin/python3
# Filename: play.py

from aip import AipSpeech

from playsound import playsound

#SDK Credentials
APP_ID = '10573122'
API_KEY = 'F2qp7ubDMXqbNC9D4Xt2LMSD'
SECRET_KEY = '27d411927a56c89e1a21cf2f96504b24'

def play_tts(text_to_play):
#play sound from baidu tts
    aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result = aipSpeech.synthesis(text_to_play, 'zh', 1, {
        'vol': 5,
    })

    if not isinstance(result, dict):
        with open('audio.mp3', 'wb') as f:
            f.write(result)
    
    playsound(result)
    #playsound('audio.mp3')