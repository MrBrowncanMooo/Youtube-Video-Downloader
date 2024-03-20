# import headers
from pytube import YouTube
from pytube.exceptions import RegexMatchError
# YouTube('https://www.youtube.com/RNRkJ0DksjU').streams.first().download()
# yt = YouTube('https://www.youtube.com/watch?v=RNRkJ0DksjU')
# yt.streams.filter(progressive=True, file_extension='mp4').order_by(
#     'resolution').desc().first().download()
# tkinter imports
import tkinter as tk
from tkinter import messagebox
from tkinter import *

# other
from time import sleep
import getpass
from pprint import pprint, pformat


class YouTubeVideo:
    def __init__(self, givenUrl):
        self.givenUrl = givenUrl

    def download_audio(self):
        try:
            yt = YouTube(self.givenUrl)  # create the object
            print(yt.streams.filter(only_audio='True').asc().first())
            video = yt.streams.filter(only_audio='True').asc().first()
            video.download("/home/"+getpass.getuser() +
                           "/Downloads", filename_prefix="YTAudio")
        except RegexMatchError as urlWrong:
            print('url not entered')

    def download_video(self):
        try:
            yt = YouTube(self.givenUrl)  # create the object
            print(yt.streams.filter(progressive='True').desc().first())
            video = yt.streams.filter(progressive='True').desc().first()
            video.download("/home/"+getpass.getuser() +
                           "/Downloads", filename_prefix="YTVideo")
        except RegexMatchError as urlWrong:
            print('url not entered')

# calls the specific downloader we want


def want_audio(url):
    audio = YouTubeVideo(url)
    audio.download_audio()


def want_video(url):
    video = YouTubeVideo(url)
    video.download_video()


# tkinter gui
request = tk.Tk()  # create the object
request.title('Youtube video')

# simple label explaining what to do
instructions = Label(request, text='Enter Youtube video Url')
instructions.grid(row=0, columnspan=2)

# create the text entry field
url = Entry(request)
url.grid(columnspan=2)

# create the buttons for mp3 and mp4
Mp3 = Button(request, text="Download Mp3",
             command=lambda: want_audio(url.get()))
Mp4 = Button(request, text="Download Mp4",
             command=lambda: want_video(url.get()))
Mp3.grid(row=2, column=0)
Mp4.grid(row=2, column=1)

request.mainloop()
