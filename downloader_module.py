from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

class VidDownloader():
    def __init__(self, url, download_folder):
        self.url = url
        self.download_folder = download_folder

    def download_video(self):
        try:
            yt_video = YouTube(self.url)
            qualities = yt_video.streams.filter(progressive=True, file_extension="mp4")
            highest_quality = qualities.get_highest_resolution()
            highest_quality.download(output_path=self.download_folder)
            return "Video downloaded"
        except Exception as e:
            print(e)
