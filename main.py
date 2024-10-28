import yt_dlp

def longer_than_a_minute(info, *, incomplete):
    """Download only videos longer than a minute (or with unknown duration)"""
    duration = info.get('duration')
    if duration and duration < 80:
        return 'The video is too short'

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
    'playlist_items': '101-150',  
    'match_filter': longer_than_a_minute,
}

playlist_url = 'https://www.youtube.com/playlist?list=LL'

# Function to download the videos
def download_mp3(playlist_url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

# Run the download
download_mp3(playlist_url)
