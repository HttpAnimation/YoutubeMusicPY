import youtube_dl

# Replace the playlist URL with your desired playlist URL
playlist_url = "https://music.youtube.com/playlist?list=PLTZLpQSU2D776UBx2q44uBvzGvrTXtZu2"

# Set options for youtube_dl
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': '%(title)s.%(ext)s',
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    # Download the playlist
    ydl.download([playlist_url])
