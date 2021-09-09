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




if __name__ == "__main__":
    print(sys.argv[1])
    os.chdir(sys.argv[1])
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        filenames = sys.argv[2:]
        ydl.download(filenames)