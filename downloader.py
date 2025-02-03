import yt_dlp

def download_video_yt_dlp(url: str, output_path: str = "downloads"):
    ydl_opts = {
        "outtmpl": f"{output_path}/%(title)s.%(ext)s",
        "format": "bestvideo+bestaudio/best"
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Введите ссылку на видео YouTube: ")
    download_video_yt_dlp(video_url)
