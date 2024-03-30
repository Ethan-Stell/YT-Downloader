from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

def download_video(url, path='downloads/'):
    """
    Downloads a YouTube video and saves it as an MP4 file.
    Args:
    - url: The URL of the YouTube video to download.
    - path: The directory path where the video will be saved. Defaults to 'downloads/'.
    """
    # Ensure the download directory exists
    if not os.path.exists(path):
        os.makedirs(path)
    
    # Download the video
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    file_path = stream.download(output_path=path)
    
    print(f"Downloaded '{yt.title}' successfully.")

    return file_path

def main():
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)


if __name__ == '__main__':
    main()
