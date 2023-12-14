#Libraries needed for the project
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

#Function to download video
def download_video(url, download_folder):
    try:
        yt_video = YouTube(url)
        qualities = yt_video.streams.filter(progressive=True, file_extension="mp4")
        highest_quality = qualities.get_highest_resolution()
        highest_quality.download(output_path=download_folder)
        print("Video downloaded")
    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
        return folder

    else:
        return None

if __name__ =="__main__":
    root=tk.Tk()
    root.withdraw()

    video_url = input("Please enter a url")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started download...")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location")


