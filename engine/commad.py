import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Use a female voice (Change to voices[0] for male)
    engine.setProperty('rate', 125)  # Adjust speech speed
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        try:
            audio = r.listen(source, timeout=5)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')  # Using Google Speech Recognition
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return ""
        except sr.RequestError:
            print("Speech Recognition service is unavailable.")
            return ""

# Start voice recognition and speak back the command
if __name__ == "__main__":
    text = takecommand()
    if text:
        speak(text)
