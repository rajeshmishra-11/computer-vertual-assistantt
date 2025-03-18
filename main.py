
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import google.generativeai as genai
import pyaudio

#pip install pocketshinx

recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi= "..........."

# Function to adjust the speech rate
def set_speech_rate(rate):
    engine.setProperty('rate', rate)

def set_female_voice():
    voices = engine.getProperty('voices')
    for voice in voices:
        if "zira" in voice.id.lower():
            engine.setProperty('voice', voice.id)
            break

def speek(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
    # Configure API key
    genai.configure(api_key=".............")

    # Initialize the model
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Start a chat session
    chat = model.start_chat()

    # Send a message
    response = chat.send_message(command)

    # Print response
    return response.text
    

def processCommand(c):
    # open software
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("http://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("http://linkedin.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("http://whatsapp.com")
    elif "open brave" in c.lower():
        webbrowser.open("http://brave.com")

    #play song 
    elif c.lower().startswith("play"):
        song= c.lower().split(" ")[1]
        link= musicLibrary.music[song]
        webbrowser.open(link)


    #Tell the news
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=................")


    # Extract the headlines
        if r.status_code == 200:
            print("OK")
            # Convert the response to JSON format
            data = r.json()
            #Extract the articles  
            articles = data.get('articles', [])
            set_speech_rate(150)
            for article in articles:
                speek(article['title'])
        else:
            speek("Sorry, I couldn't retrieve the news.")

    else:
        #Let openAI handle the request
        output= aiprocess(c)
        speek(output)
       

        

if __name__ =="__main__":
    set_female_voice()
    speek("Initializing jarvis....")

    while True:
    # Initialize the recognizer
        recognizer = sr.Recognizer()

    # Use the microphone as the source for input
        with sr.Microphone() as source:
            print("Listening...")
        # Adjust the recognizer sensitivity to ambient noise
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
        # Listen for the first phrase and extract it into audio data
            audio_data = recognizer.listen(source)
            print("Recognizing...")

        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
            print("You said: " + text)
            if (text.lower()=="jarvis"):
                speek("ya")
                #listen for command
                with sr.Microphone() as source:
                    print("jarvis active...")
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    audio_data = recognizer.listen(source)
                    text = recognizer.recognize_google(audio_data)
                    processCommand(text)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Could not request results from the speech recognition service.")
