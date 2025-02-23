import yt_dlp
import os

def download_video_yt_dlp(url: str, output_folder: str = "downloads"):
    # Создаем папку, если её нет
    os.makedirs(output_folder, exist_ok=True)
    
    ydl_opts = {
        "outtmpl": os.path.join(output_folder, "%(title)s.%(ext)s"),  # Имя файла по названию видео
        "format": "bestvideo[height<=720][ext=mp4][vcodec^=avc1]+bestaudio[ext=m4a]/best[ext=mp4]",
        "merge_output_format": "mp4",
        "noplaylist": True,
        "geo_bypass": True,
        "quiet": False,
        "postprocessors": [{
            "key": "FFmpegMetadata"
        }]
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Введите ссылку на видео YouTube: ")
    download_video_yt_dlp(video_url)
