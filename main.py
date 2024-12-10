# main.py

from youtube_api import search_youtube_videos, get_video_statistics
from ranker import rank_videos
from gpt_analyzer import analyze_videos_with_gpt

def main():
    # User input
    niche = input("Enter the niche (e.g., AI tutorials): ")
    region = input("Enter the region (e.g., US): ")
    max_results = int(input("Enter the maximum number of videos to analyze (e.g., 50): "))
    niche_keywords = niche.lower().split()

    # Search YouTube videos
    print("Searching for videos...")
    videos = search_youtube_videos(niche, region, max_results)

    # Rank videos
    print("Ranking videos...")
    ranked_videos = rank_videos(videos, niche_keywords)

    # Print top-ranked videos
    print("\nTop-ranked videos:")
    for video in ranked_videos[:10]:
        print(f"Title: {video['title']} (Score: {video['relevance_score']})")

    # Analyze trends with GPT
    print("\nAnalyzing trends with GPT...")
    analysis = analyze_videos_with_gpt(ranked_videos)
    print("\nGPT Analysis:")
    print(analysis)

if __name__ == "__main__":
    main()
