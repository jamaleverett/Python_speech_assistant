import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import yfinance as yf # to fetch financial data
import ssl
import certifi
import time
import os  # to remove created audio files

class person:
    name = ''
    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

r = sr.Recognizer()  #initialize a recognizer
#listen for auido and covert it to text:
def record_audio(ask=False):
    with sr.Microphone() as source:  #microphone as source
        if ask:
            speak(ask)
        audio = r.listen(source)  #listen for audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  #coverts audio to text
        except sr.UnknownValueError:  #error: recognize does not understand
            speak('Whoops! I did not get that')
        except sr.RequestError:
            speak('Oh, gosh! It looks like the service is down')  #error: recognizer is not connected
        print(f">>{voice_data.lower()}")  #prints what user said
        return voice_data.lower()

# get string and makes audio file to be played
def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')  #tts(voice) #choose lang of choice
    r = random.randint(1, 20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)  #will save file as mp3
    playsound.playsound(audio_file)  #will play audio file
    print(f"kiri: {audio_file}")  #will print what app said
    os.remove(audio_file)  #removes audio file
    
def respond(voice_data):
    #1: greeting
    if there_exists(['hey', 'hi', 'hello']):
        greetings = [f"heyo! How vcan I help you {person_obj.name}", f"hey, what's up {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        speak(greet)

    #2: name
    if there_exists(["what is your name", "what's your name", "tell me your name"]):
        if person_obj.name:
            speak("my name is Marley")
        else:
            speak("my name is Marley, what's your name?")

    if there_exists(["my name is"]);
        person_name = voice_data.split("is")[-1].strip()
        speak(f"okay, i'll remember that {person_name}")
        person_obj.setName(person_name)  #remembers name in person object
        
    #3: greeting
    if there_exists(["how are you", "how are you doimg"]):
    
    
    #4: time
    if there_exists(["what's the time", "tell me the time", "what time is it"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        speak(time)

    #5: search google
    if there_exists(["search for"]) and 'youtube' not in voice_data
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'here is what I found for {search_term} on google')  #will return google search results
        
    #6: search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on youtube')

    #7 get stock price
    if there_exists(["price of"]):
        search_term = voice_data.lower().split(" of ")[-1].strip() #strip removes whitespace after/before a term in string
        stocks = {
            "apple":"AAPL",
            "microsoft":"MSFT",
            "facebook":"FB",
            "tesla":"TSLA",
            "bitcoin":"BTC-USD"
        }
        try:
            stock = stocks[search_term]
            stock = yf.Ticker(stock)
            price = stock.info["regularMarketPrice"]

            speak(f'price of {search_term} is {price} {stock.info["currency"]} {person_obj.name}')
        except:
            speak('oops, something went wrong')
    if there_exists(["exit", "quit", "goodbye"]):
        speak("going offline")
        exit()


time.sleep(1)

person_obj = person()
while(1):
    voice_data = record_audio() # get the voice input
    respond(voice_data) # respond
