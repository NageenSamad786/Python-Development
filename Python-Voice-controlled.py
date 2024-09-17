import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Function to speak the text
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to listen for commands
def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"Command recognized: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service.")
            speak("Sorry, there was an issue with the speech recognition service.")
            return None

# Main function to process commands
def process_command(command):
    if command:
        command = command.lower()
        if "hello" in command:
            speak("Hello! How can I assist you today?")
        elif "your name" in command:
            speak("I am your personal assistant.")
        elif "what time is it" in command:
            from datetime import datetime
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            speak(f"The time is {current_time}")
        elif "stop" in command:
            speak("Goodbye!")
            return False
        else:
            speak("I am not sure how to respond to that.")
    return True

# Main loop
if __name__ == "__main__":
    speak("Personal assistant activated.")
    while True:
        command = listen_command()
        if not process_command(command):
            break
