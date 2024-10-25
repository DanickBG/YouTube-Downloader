# YouTube-Downloader
Automated YouTube Downloader with yt-dlp

To download MP3 files from a YouTube playlist like your "Liked Videos," you can use Python along with the yt-dlp library. This tool is an improved version of youtube-dl that supports downloading audio and video from YouTube and other platforms.

Start with:

```pip install yt-dlp```

yt-dlp requires ffmpeg to convert video files to audio formats (like MP3). You can install it using:

On macOS with Homebrew:
```brew install ffmpeg```

On Ubuntu/Debian:
```sudo apt-get install ffmpeg```

Then just run main.py

If you want to download your Liked Videos you can use Google Chrome Extention to download the cookies locally and then paste the .txt file in the directory of the python script and add:
```
'cookiefile': 'cookies.txt',
```
in
```
ydl_opts={}
```
