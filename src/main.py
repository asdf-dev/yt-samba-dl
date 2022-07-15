from operator import le
import os
import sys
from ytdl import ytdl
from cutter import cutter

#change this to hardcode path
pathToDir = "/Users/krois/Source/ytdl"

def main():
    sourceOfDownload = sys.argv[1:]
    #os.system("screen -q")
    #print("Using screen!")
    #print("you can detach screen by ctrl+d")
    #print("for at list of screens type screen -ls")

    os.chdir(pathToDir)
    isExist = os.path.exists("temp")
    if not (isExist):
        os.mkdir("temp")

    os.chdir("temp")
    print(sourceOfDownload)
    print("use screen -wipe to close all screen sessions")

    ytdl.doDownload(sourceOfDownload)
    

    # list to store files
    dir_path = os.curdir
    res = []
    # Iterate directory
    for path in os.listdir(dir_path):
    # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)
    
    cutter.splitmp3(res[0])
        
    


if __name__ == "__main__":
    main()