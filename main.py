import yt_dlp

ydl_opts = {
    'cookiefile': 'cookies.txt',  
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',  
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '256', 
    }],
    'noplaylist': False,  
    'playlist_items': '1-100',  
}

playlist_url = 'https://www.youtube.com/playlist?list=LL'

# Function to download the videos
def download_mp3(playlist_url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

# Run the download
download_mp3(playlist_url)
