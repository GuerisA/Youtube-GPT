# youtube_api.py

from googleapiclient.discovery import build
from config import YOUTUBE_API_KEY

# Initialize YouTube API client
youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

def search_youtube_videos(niche, region, max_results, page_token=None):
    request = youtube.search().list(
        q=niche,
        part="snippet",
        type="video",
        maxResults=max_results,
        regionCode=region,
        order="relevance",
        pageToken=page_token
    )
    return request.execute()

def get_video_statistics(video_id):
    request = youtube.videos().list(
        part="statistics,snippet",
        id=video_id
    )
    return request.execute()
