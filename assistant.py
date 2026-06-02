import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print("You:", command)
            return command.lower()

        except Exception:
            print("Sorry, I couldn't understand.")
            return ""

def run_assistant():
    speak("Hello! I am your voice assistant.")

    while True:
        command = listen()

        if not command:
            continue

        elif "hello" in command:
            speak("Hello! How can I help you?")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}")

        elif "date" in command:
            today = datetime.date.today()
            speak(f"Today's date is {today}")

        elif "google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

        else:
            speak("I did not understand that command.")

run_assistant()