import os
import youtube_dl
import pyttsx3
import playsound
from googleapiclient.discovery import build

# Set your YouTube API key here
API_KEY = "AIzaSyDEcT5j2ArBXFqr-LBOiE74uvSbvyC65AQ"

# YouTube API setup
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Text-to-speech setup
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to search and play a YouTube video
def play_video(query):
    search_response = youtube.search().list(q=query, part='id,snippet', maxResults=1).execute()
    video_id = search_response['items'][0]['id']['videoId']

    url = f"https://www.youtube.com/watch?v={video_id}"

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'temp.mp3',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Play the downloaded audio file
    playsound.playsound('temp.mp3')

    # Delete the temporary audio file
    os.remove('temp.mp3')

# Main loop
while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        break

    # Play music if the user asks
    if 'play music' in user_input.lower():
        speak("Sure! What music would you like to listen to?")
        music_query = input("You: ")
        speak(f"Playing {music_query}")
        play_video(music_query)
    else:
        # Respond to user input
        speak("I'm sorry, I didn't understand that.")
