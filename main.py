import googletrans
import speech_recognition
import gtts
import playsound
# print(googletrans.LANGUAGES)

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Bicara Sekarang!")
    voice = recognizer.listen(source)
    text_voice = recognizer.recognize_google(voice,language="id")
    print(text_voice)
translator = googletrans.Translator()
# translation = translator.translate("Selamat Datang",dest="en")
translation = translator.translate(text_voice,dest="en")
print(translation.text)

convert_audio = gtts.gTTS(translation.text, lang="en")
convert_audio.save("voice.mp3")

playsound.playsound("voice.mp3")
