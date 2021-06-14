import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__=='__main__':
    speak("Aaj ki khabar.. Chaliye shuru karte hai")
    url="https://newsapi.org/v2/everything?q=bitcoin&apiKey=38d76dc156a04aafb4c2af1169e4ac40"
    news=requests.get(url).text
    news_dict=json.loads(news)
    arts=news_dict['articles']
    for article in arts:
        speak(article['title'])
        print(article['title'])
        speak("Agli khabar ki oaur badhate hue..Dhyan se sune")

    speak("Sune ke liye dhanyawaad...")


