import os
from pydub import AudioSegment


class cutter:
        
    def splitmp3(filename):
        cutTime = 300000 # 5min
        print("splitting mp3", filename)
        song = AudioSegment.from_mp3(filename)
        os.remove(filename)
        

        print("filename", filename)


        result = (song[i:i+cutTime] for i in range(0, len(song), cutTime))
        
        filename = filename.replace('.mp3', 'ny')
        os.mkdir(filename)
        os.chdir(filename)
        for idx, i in enumerate(result):
            if idx == 0:
                print(len(i))
                i.export("{}.mp3".format(filename), format="mp3", tags={'album': filename})
            else:
                print(len(i)) 
                i.export("{}_{}.mp3".format(filename, idx), format="mp3", tags={'album': filename})
