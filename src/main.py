from operator import le
import os
import sys
from ytdl import ytdl
from cutter import cutter

#change this to hardcode path
pathToDir = "/home/hdd/sambashare/music"

def main():
   sourceOfDownload = sys.argv[1:]

   for x in sourceOfDownload:

    os.chdir(pathToDir)
    isExist = os.path.exists("temp")
    if not (isExist):
        os.mkdir("temp")

    os.chdir("temp")
    print("Downloading: {}".format(x))
    
    ytdl.doDownload(x)
    

    # list to store files
    dir_path = os.curdir
    res = []
    # Iterate directory
    for path in os.listdir(dir_path):
    # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)
    
    cutter.splitmp3(res[0])

    print("Download and splitting done enjoy")
        
    


if __name__ == "__main__":
    main()