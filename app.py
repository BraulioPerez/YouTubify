from flask import Flask, render_template, request, url_for
import os
from downloader_module import VidDownloader

current_dir = os.getcwd()
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download", methods=["GET", "POST"])
def download():
    if request.method == "POST":
        vid_url = request.form["links"]
        download_dir = os.path.join(current_dir, "downloads")
        print(download_dir)
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
        downloader = VidDownloader(url=vid_url, download_folder=download_dir)
        downloader.download_video()
        return render_template("index.html", message='Video downloaded')
    return render_template("index.html", message=f"{download_dir, vid_url}")



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
