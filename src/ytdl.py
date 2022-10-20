from distutils.log import info
from yt_dlp import YoutubeDL

class ytdl:
    def doDownload(sourceToDownload):
        ydl_opts = {
                'outtmpl': '%(title)s.%(ext)s',
                'format': 'bestaudio/best',
                'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]}
        with YoutubeDL(ydl_opts) as ydl:
           ydl.download(sourceToDownload)


