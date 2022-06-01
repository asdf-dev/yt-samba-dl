import os
import sys
from ytdl import ytdl


def main():
    sourceOfDownload = sys.argv[1:]
    #os.system("screen -q")
    #print("Using screen!")
    #print("you can detach screen by ctrl+d")
    #print("for at list of screens type screen -ls")

    #os.chdir("/home/hdd/sambashare/music")
    os.chdir("/Users/krois/Source/ytdl")
    print(sourceOfDownload)
    print("use screen -wipe to close all screen sessions")

    ytdl.doDownload(sourceOfDownload)

if __name__ == "__main__":
    main()