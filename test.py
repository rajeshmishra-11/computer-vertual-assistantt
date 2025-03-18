import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the voice to "Microsoft Zira Desktop"
def set_female_voice():
    voices = engine.getProperty('voices')
    for voice in voices:
        if "zira" in voice.id.lower():
            engine.setProperty('voice', voice.id)
            break

# Function to adjust the speech rate
def set_speech_rate(rate):
    engine.setProperty('rate', rate)

# Function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Example usage
set_female_voice()
set_speech_rate(150)  # Adjust speed if necessary
speak("This is how I sound with the Zira female voice.")

