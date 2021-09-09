# Another youtube downloader..

## Usage:

```
 pip install -r /path/to/requirements.txt 
```
### Download music

```
 python3 ytdl.py WHERE/TO/SAVE/FILE https://www.youtube.com/PATH
```


## Use case:
Install on raspberry pi

Setup [Samba](https://en.wikipedia.org/wiki/Samba_(software)) and share a folder.

Download music to that folder with a simple ssh to raspberry pi. 

From a remote computer to the raspberry pi
```
 ssh USER@IP PATH/TO/PYTHON_FILE/ytdl.py WHERE/TO/SAVE/FILE https://www.youtube.com/PATH
```
I suggest setting up an alias(function)

Now you're able to get it on your phone 