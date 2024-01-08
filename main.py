from pytube import YouTube
from sys import argv

link = argv[1]
path = argv[2]
youtube = YouTube(link)

youtube_download = youtube.streams.get_highest_resolution()

youtube_download.download(path)
