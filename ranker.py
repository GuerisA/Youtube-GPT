# ranker.py

def rank_videos(videos, niche_keywords):
    ranked_videos = []
    for video in videos["items"]:
        title = video["snippet"]["title"]
        relevance_score = sum(1 for word in niche_keywords if word.lower() in title.lower())
        video_id = video["id"]["videoId"]

        # You can extend this with statistics like views or likes if available
        ranked_videos.append({
            "video_id": video_id,
            "title": title,
            "relevance_score": relevance_score,
            "thumbnail": video["snippet"]["thumbnails"]["default"]["url"],
        })

    return sorted(ranked_videos, key=lambda x: -x["relevance_score"])
