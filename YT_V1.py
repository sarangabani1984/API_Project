import os
import json
import pandas as pd
from datetime import datetime
from googleapiclient.discovery import build

# Replace 'YOUR_API_KEY' with your actual API key
api_key = "AIzaSyDKHoaT4TjFd01BJkgLlLm2s-RTeBQhdJM"
youtube = build("youtube", "v3", developerKey=api_key)

# Replace 'YOUR_SEARCH_QUERY' with your search term
search_query = "think & grow rich book review"

# Step 1: Search for videos
search_response = youtube.search().list(
    part="snippet",
    q=search_query,
    type="video",
    maxResults=10  # Get more videos to filter top 5
).execute()

# Extract video IDs
video_ids = [item['id']['videoId'] for item in search_response['items']]

# Step 2: Get video statistics (view count)
video_stats_response = youtube.videos().list(
    part="statistics,snippet",
    id=",".join(video_ids)  # Pass all video IDs
).execute()

# Extract required data
video_data = []
for item in video_stats_response['items']:
    video_data.append({
        "Channel_name": item['snippet']['channelTitle'],
        "Video ID": item['id'],
        "Channel ID": item['snippet']['channelId'],
        "Title": item['snippet']['title'],
        "publishedAt": item['snippet']['publishedAt'],
        "View Count": int(item['statistics'].get('viewCount', 0))  # Convert to int for sorting
    })

# Step 3: Sort videos by view count (descending) and get the top 5
top_videos = sorted(video_data, key=lambda x: x["View Count"], reverse=True)[:5]

# Convert to DataFrame
df = pd.DataFrame(top_videos)

# Ensure the directory exists
save_directory = "D:\\YouTube_Analysis"
os.makedirs(save_directory, exist_ok=True)

# Get today's date (YYYY-MM-DD format)
current_date = datetime.today().strftime('%Y-%m-%d')

# Create a valid filename using the search query + date
file_name = f"{search_query.replace(' ', '_')}_Top5_Videos_{current_date}.csv"
file_path = os.path.join(save_directory, file_name)

# Save DataFrame to CSV
df.to_csv(file_path, index=False)

print(f"File saved successfully at: {file_path}")
