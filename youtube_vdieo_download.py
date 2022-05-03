from pytube import *

video_url = 'https://www.youtube.com/watch?v=U2TlQbkog08' # paste here your Youtube videos' url
youtube = YouTube(video_url)
print(youtube.title)
videos= list(youtube.streams)


for x in videos:
    if x.resolution=='1080p':
        YouTube(video_url).streams.get_by_resolution('1080p').download()
        continue
    elif x.resolution=='720p':
        YouTube(video_url).streams.get_by_resolution('720p').download()




# YouTube('https://www.youtube.com/watch?v=U2TlQbkog08').streams.get_highest_resolution().download()