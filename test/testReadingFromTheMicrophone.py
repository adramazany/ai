import sounddevice
import speech_recognition as sr

r = sr.Recognizer()
print(sr.Microphone.list_microphone_names())

# with sr.Microphone(device_index=2) as source:
with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(text)


