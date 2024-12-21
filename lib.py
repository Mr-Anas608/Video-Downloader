# import yt_dlp, pprint

# def get_download_url(url):
#     try:
#         ydl_opts = {
#             'formate' : 'best',
#             'noplaylist' : True
#         }

#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(url, download=False)
#             title = info.get('title')
#             url = info.get('url')
#             formats = info.get('formats', [])
#             return {
#                 'title' : title, 
#                 'url' : url,
#                 'formats': formats
#             }
        
        
#     except Exception:
#         return None
    
    
# def get_video_info(url):
#     ydl_opts = {}
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info = ydl.extract_info(url, download=False)
#     return info

# # Usage
# info = get_video_info('https://www.youtube.com/watch?v=_1GAszHUP7E')
# # print(f"Title: {info['title']}")
# # print(f"Duration: {info['duration']} seconds")

# pprint.pprint(info)
    
# # pprint.pprint(get_download_url('https://www.youtube.com/watch?v=PbACUfeDhDA'))


# # url=('https://www.youtube.com/watch?v=PbACUfeDhDA')

# # ydl_opts = {
# #                 'formate' : 'best',
# #                 'noplaylist' : True,
# #                 'quiet' : True
# #             }
        
# # with yt_dlp.YoutubeDL(ydl_opts) as ydl:
# #             info = ydl.extract_info(url, download=False)

# #             video_details = {
# #                 'title' : info.get('title'),
# #                 'thumbnail' : info.get('thumbnail'),
# #                 'uploader' : info.get('uploader'),
# #                 'duration' : info.get('duration'),
# #                 'view_count' : info.get('view_count'),
# #                 'like_count' : info.get('like_count'),
# #                 'dislike_count' : info.get('upload_date'),
# #                 'description' : info.get('description'),
# #                 'upload_date' : info.get('upload_date'),
# #                 'url' : info.get('url'),
# #             }
# #             pprint.pprint(video_details)


# import yt_dlp
# import pprint

# url = 'https://www.youtube.com/watch?v=PbACUfeDhDA'
# ydl_opts = {
#             'noplaylist': True,  # Ensures we're extracting a single video
#         }

# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(url, download=False)
#             formats = info.get('formats', [])
            
#             # Filter formats into categories
#             video_audio_formats = [
#                 fmt for fmt in formats if fmt.get('vcodec') != 'none' and fmt.get('acodec') != 'none'
#             ]
#             audio_only_formats = [
#                 fmt for fmt in formats if fmt.get('vcodec') == 'none' and fmt.get('acodec') != 'none'
#             ]
            
#             pprint.pprint(video_audio_formats)
           

  
import requests
from urllib.parse import urlparse

def is_valid_url(url):
    try:
        # Check if the URL is well-formed
        parsed = urlparse(url)
        if not (parsed.scheme and parsed.netloc):
            return False
        # Send a HEAD request to check if the URL is accessible
        response = requests.head(url, timeout=5)
        return response.status_code >= 200 and response.status_code < 400
    except (ValueError, requests.RequestException):
        return False
