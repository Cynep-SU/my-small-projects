from gtts import gTTS
from playsound import playsound

audio = 'seech.mp3'
language = 'ru'
sp =  gTTS(text = "Что я сказала?",
            lang = language,slow = False)
sp.save(audio)
playsound(audio)