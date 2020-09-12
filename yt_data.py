import youtube_dl

url = 'https://www.youtube.com/watch?v=o_7nfzI22Ls'

ydl = youtube_dl.YoutubeDL({})
with ydl:
    video = ydl.extract_info(url, download=False)

# print('{}-{}'.format(video['artist'], video['track']))
# print(list(video.keys()))
print(video['title'])