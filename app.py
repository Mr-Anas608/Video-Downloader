import yt_dlp
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    video_url = request.form.get('video_url')
    try:
        # Use yt_dlp to extract video information
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Fetch the best video and audio formats
            'noplaylist': True,  # Ensure only a single video is processed
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)

            # Extract the direct URL for video playback
            if 'url' in info_dict:
                direct_video_url = info_dict['url']  # Direct URL to video
                return redirect(direct_video_url)
            elif 'formats' in info_dict and len(info_dict['formats']) > 0:
                # If no single 'url', fallback to the first available format
                direct_video_url = info_dict['formats'][-1]['url']
                return redirect(direct_video_url)
            else:
                return "<h3 style='color: red;'>Error: Unable to extract video URL.</h3>"

    except Exception as e:
        return f"<h3 style='color: red;'>Error: {str(e)}</h3><p>Ensure the video URL is correct!</p>"

if __name__ == '__main__':
    app.run(debug=True)
