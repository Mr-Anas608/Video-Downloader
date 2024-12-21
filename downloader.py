import yt_dlp


# A utility function to extract values safely from a dictionary
def extract_key(dictionary, key, default=None):
    return dictionary.get(key, default)


# A function for filtering extracted information
def filter_info(info):
    title = extract_key(info, "title")
    thumbnail = extract_key(info, "thumbnail")
    formats = extract_key(info, "formats", [])  # Default to an empty list if formats key is missing

    # Filter formats for video and audio separately
    video_formats = [f for f in formats if (extract_key(f, "vcodec") != 'none' or extract_key(f, "acodec") != 'none')]
    audio_formats = [f for f in formats if (extract_key(f, "vcodec") == 'none' and extract_key(f, "acodec") != 'none')]

    # Now filter video and audio formats for commonly used details
    filter_video_formats = []
    filter_audio_formats = []

    # Process video formats
    for f in video_formats:
        t = {}
        filesize = extract_key(f, "filesize", extract_key(f, "filesize_approx", 0))
        if filesize:  # Ensure filesize is not None or 0
            if filesize >= (1024 * 1024 * 1024):  # Greater than or equal to 1 GB
                t['filesize'] = f"{round(filesize / (1024 * 1024 * 1024), 2)} GB"
            else:  # Less than 1 GB
                t['filesize'] = f"{round(filesize / (1024 * 1024), 1)} MB"

        t["url"] = extract_key(f, "url")
        resolution = extract_key(f, "resolution", "0x0").split("x")[-1]  # Get vertical resolution
        t["resolution"] = resolution
        t["ext"] = extract_key(f, "ext")

        # Append processed video format
        filter_video_formats.append(t)

    # Process audio formats
    for f in audio_formats:
        t = {}
        filesize = extract_key(f, "filesize", extract_key(f, "filesize_approx", 0))
        if filesize:  # Ensure filesize is not None or 0
            if filesize >= (1024 * 1024 * 1024):  # Greater than or equal to 1 GB
                t['filesize'] = f"{round(filesize / (1024 * 1024 * 1024), 2)} GB"
            else:  # Less than 1 GB
                t['filesize'] = f"{round(filesize / (1024 * 1024), 1)} MB"

        t["url"] = extract_key(f, "url")
        t["ext"] = extract_key(f, "ext")
        abr = extract_key(f, "abr", 0)
        t["abr"] = f"{round(abr)} Kbps" if abr else "Unknown"

        # Append processed audio format
        filter_audio_formats.append(t)

    # Return the filtered information
    return {
        'title': title,
        'thumbnail': thumbnail,
        'videos': filter_video_formats,
        'audios': filter_audio_formats
    }


# A function to extract download information using extract_info in YoutubeDL Class from yt_dlp library
def get_download_options(url):
    ydl_opts = {}

    # try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        info_after_filter = filter_info(info)
        return info_after_filter

    # except yt_dlp.utils.DownloadError as e:
    #     return {"error": f"The provided URL is not supported: {str(e)}"}
    # except Exception as e:
    #     return {"error": f"An unexpected error occurred: {str(e)}"}
