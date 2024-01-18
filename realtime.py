import googletrans
import speech_recognition
import gtts
import playsound

def translate_and_play():
    recognizer = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        print("Bicara Sekarang!")

        try:
            voice = recognizer.listen(source)
            text_voice = recognizer.recognize_google(voice, language="id")
            print("Bahasa Asli:", text_voice)

            translator = googletrans.Translator()
            translation = translator.translate(text_voice, dest="en")
            print("Terjemahan:", translation.text)

            convert_audio = gtts.gTTS(translation.text, lang="en")
            convert_audio.save("voice_realtime.mp3")

            playsound.playsound("voice_realtime.mp3")

        except speech_recognition.UnknownValueError:
            print("Maaf, tidak dapat mendeteksi suara. Coba lagi.")
        except Exception as e:
            print("Terjadi kesalahan:", e)

if __name__ == "__main__":
    try:
        while True:
            translate_and_play()
    except KeyboardInterrupt:
        print("Aplikasi berhenti.")
