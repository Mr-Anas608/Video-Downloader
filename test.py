import yt_dlp
from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    video_url = request.form.get('video_url')
    try:
        # Download the video using yt-dlp
        ydl_opts = {
            'outtmpl': 'downloads/%(title)s.%(ext)s',  # Save to "downloads" folder
            'format': 'bestvideo+bestaudio/best',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)
            video_title = info_dict.get('title', 'video')
            video_filename = f"{video_title}.mp4"
        
        # Provide the file for download
        video_path = os.path.join('downloads', video_filename)
        return send_file(video_path, as_attachment=True)
    
    except Exception as e:
        return f"<h3 style='color: red;'>Error: {str(e)}</h3><p>Make sure the URL is correct!</p>"

if __name__ == '__main__':
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    app.run(debug=True)
