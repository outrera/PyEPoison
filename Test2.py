import speech_recognition as sr
from gtts import gTTS
import time
from pygame import mixer # Load the required library
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
recon = r.recognize_google(audio)


# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    stamp=("Google Speech Recognition thinks you said " + recon)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

print(stamp)
tts = gTTS(text=stamp, lang='en')
tts.save("good.mp3")
mixer.init()
mixer.music.load('good.mp3')
mixer.music.play()
ak='what results from the chemical reaction of water and sodium'
if recon == ak:
	tts = gTTS(text="It results in caustic sose and hidrogen, oh, and also an explosion", lang='en')
	tts.save("sodium.mp3")
	mixer.init()
	mixer.music.load('sodium.mp3')
	mixer.music.play()