# gpt_analyzer.py

import openai
from config import OPENAI_API_KEY

# Initialize OpenAI API client
openai.api_key = OPENAI_API_KEY

def analyze_videos_with_gpt(video_metadata):
    # Prepare metadata string
    metadata_str = "\n".join(
        [f"Title: {video['title']}, Relevance Score: {video['relevance_score']}" for video in video_metadata]
    )
    
    # ChatGPT-style prompt
    prompt = f"Based on the following video metadata, summarize the trends in this niche:\n{metadata_str}"
    
    # Call the updated API
    response = openai.ChatCompletion.create(
        model="gpt-4",  # You can also use "gpt-3.5-turbo" if needed
        messages=[
            {"role": "system", "content": "You are an expert YouTube trend analyst."},
            {"role": "user", "content": prompt}
        ]
    )
    