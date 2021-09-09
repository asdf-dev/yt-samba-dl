import os
import youtube_dl
import sys

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

path = '/home/krois/Desktop/'


if __name__ == "__main__":
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        os.chdir(path)
        filenames = sys.argv[1:]
        ydl.download(filenames)