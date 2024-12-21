from flask import Flask, render_template, request, jsonify
import yt_dlp

app = Flask(__name__)

def get_download_url(url):
    try:
        url = 'https://www.youtube.com/watch?v=PbACUfeDhDA'
        ydl_opts = {
            'noplaylist': True,  # Ensures we're extracting a single video
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info.get('formats', [])
            
            # Filter formats into categories
            video_audio_formats = [
                fmt for fmt in formats if fmt.get('vcodec') != 'none' and fmt.get('acodec') != 'none'
            ]
            audio_only_formats = [
                fmt for fmt in formats if fmt.get('vcodec') == 'none' and fmt.get('acodec') != 'none'
            ]
            
            return info
        
    except Exception:
        return None


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sample')
def sample():
    return get_download_url('https://www.youtube.com/watch?v=PbACUfeDhDA')


@app.route('/download_url', methods=['POST'])
def download_url():
    video_url = request.form.get('video_url')
    if not video_url:
        return "Error: URL is required", 400

    try:
       info = get_download_url(video_url)

       if info:
           return info
       else:
            return "Error: failed to fetch download_url"
    except Exception:
        None



@app.route('/video_info', methods=['POST'])
def video_info():   
    video_url = request.form.get('video_url')
    if not video_url:
        return "Error: URL is required", 400
    try:
        ydl_opts = {
                'formate' : 'best',
                'noplaylist' : True,
                'quiet' : True
            }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)

            video_details = {
                'title' : info.get('title'),
                'thumbnail' : info.get('thumbnail'),
                'uploader' : info.get('uploader'),
                'duration' : info.get('duration'),
                'view_count' : info.get('view_count'),
                'like_count' : info.get('like_count'),
                'dislike_count' : info.get('upload_date'),
                'description' : info.get('description'),
                'upload_date' : info.get('upload_date'),
                'url' : info.get('url'),
            }
    except Exception:
       return None, 500
    
    return video_details, 200



if __name__ == '__main__':
    app.run(debug=True)