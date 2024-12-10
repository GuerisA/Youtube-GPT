from googleapiclient.discovery import build

API_KEY = "AIzaSyAp1cHMsE-8XZaIGcqAXS7rqctUe1UZmCo"
youtube = build("youtube", "v3", developerKey=API_KEY)

def get_video_captions(video_id):
    request = youtube.captions().list(
        part="snippet",
        videoId=video_id
    )
    response = request.execute()
    return response

video_id = "cc1H6kQtEvU"
captions = get_video_captions(video_id)
print(captions)

def download_captions(video_id, caption_id):
    request = youtube.captions().download(
        id=caption_id,
        tfmt="srt"  # Format of captions (e.g., .srt for subtitles)
    )
    response = request.execute()
    return response.decode("utf-8")

# Fetch caption ID from the metadata
captions_metadata = get_video_captions(video_id)
caption_id = captions_metadata["items"][0]["id"]  # Assuming the first caption is desired

# Download the captions
captions_text = download_captions(video_id, caption_id)
print(captions_text)
