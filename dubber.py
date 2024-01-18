import os
import speech_recognition
from googletrans import Translator
from gtts import gTTS
import moviepy.editor as mp

def translate_and_generate_audio(text, target_language="id"):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print(f"Terjemahan ke {target_language}: {translation.text}")

    tts = gTTS(translation.text, lang=target_language)
    return tts

def process_video(input_path, output_path):
    video_clip = mp.VideoFileClip(input_path)
    audio = video_clip.audio
    duration = int(video_clip.duration)

    recognizer = speech_recognition.Recognizer()

    for current_time in range(0, duration, 10):  # Ambil sampel setiap 10 detik
        audio_clip = audio.subclip(current_time, current_time + 10)
        audio_clip.write_audiofile(f"{output_path}/temp_audio_{current_time}.wav", codec='pcm_s16le')

        with speech_recognition.AudioFile(f"{output_path}/temp_audio_{current_time}.wav") as audio_file:
            audio_content = recognizer.record(audio_file)

            text_voice = recognizer.recognize_google(audio_content, language="en")

            tts = translate_and_generate_audio(text_voice, target_language="id")
            tts.save(f"{output_path}/audio_{current_time}.mp3")

            print(f"Audio terjemahan pada detik {current_time} disimpan sebagai audio_{current_time}.mp3")

    video_clip.close()

if __name__ == "__main__":
    video_path = "vidioPidato.mp4"  # Ganti dengan path ke video Anda
    output_path = "./outputDubber"  # Ganti dengan path direktori keluaran Anda

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    process_video(video_path, output_path)
