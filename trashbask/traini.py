# import pytube
# #ссылка на видео:
# PathOnPC = "C:/Users/srja/Desktop"
# link = 'https://www.youtube.com/watch?v=yzSWOWuCi-Y'
# yt = pytube.YouTube(link)
# stream = yt.streams.first()
# stream.download(PathOnPC)

from pytube import YouTube

youtube_video_url = 'https://www.youtube.com/watch?v=yzSWOWuCi-Y'

try:
    yt_obj = YouTube(youtube_video_url)
    print(yt_obj.streams.filter(only_audio=True))

    yt_obj.streams.get_by_itag(251).download(output_path='C:/Users/srja/Desktop', filename='audio.mp3')
    print('YouTube video audio downloaded successfully')
except Exception as e:
    print(e)