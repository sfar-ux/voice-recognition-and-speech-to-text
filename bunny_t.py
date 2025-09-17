import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import datetime
import random

# Initialize the text-to-speech engine
engine = pyttsx3.init()  # Platform auto-detect
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Choose voice

# Speak output
def speak(text):
    print(f"Bunny T: {text}")
    engine.say(text)
    engine.runAndWait()

# Greeting function
def greet_me():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hello Sir, I am your digital assistant Bunny T!")
    speak("How may I help you?")

# Command input: voice with fallback
def my_command():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            speak("Listening...")
            r.adjust_for_ambient_noise(source, duration=2)
            audio = r.listen(source)
            command = r.recognize_google(audio, language='en-in')
            print("You said:", command)
            return command.lower()
    except Exception as e:
        speak("Microphone not available. Please type your command.")
        print(f"(Fallback) Error: {e}")
        return input("Command: ").lower()

# Assistant logic
def handle_query(query):
    if not query.strip():
        speak("I didn't catch any command. Please try again.")
        return

    # Basic responses
    if "how are you" in query:
        speak(random.choice(["I'm great, thanks for asking!", "I'm fine, Sir!", "Ready to assist!"]))
    elif "who are you" in query or "what are you" in query:
        speak("I am Bunny T, your Python-powered voice assistant.")
    elif "bye" in query or "exit" in query or "stop" in query:
        speak("Goodbye Sir, have a great day!")
        exit()

    # Open websites
    elif "open youtube" in query:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")

    elif "open google" in query:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")

    elif "open gmail" in query:
        webbrowser.open("https://mail.google.com")
        speak("Opening Gmail.")

    # Search Wikipedia or Google
    else:
        speak("Searching your query...")
        try:
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia:")
            speak(result)
        except Exception:
            speak("I opened Google for your query.")
            webbrowser.open(f"https://www.google.com/search?q={query}")

# ---------- MAIN LOOP ----------
if __name__ == '__main__':
    greet_me()
    while True:
        query = my_command()
        handle_query(query)
        speak("Next command, Sir.")
