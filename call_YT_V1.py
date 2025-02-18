import os  # Import the os module
from YT_V1 import youtube_search, save_to_csv  # Import the functions from YT_V1.py

def analyze_and_save(api_key, search_query):
    """
    Searches YouTube, retrieves top videos, and saves the results to a CSV file.

    Args:
        api_key (str): Your YouTube API key.
        search_query (str): The search query to use on YouTube.
    """
    try:
        # Perform YouTube search and get video data
        video_data = youtube_search(api_key, search_query)

        # Save results to CSV
        save_to_csv(video_data, search_query)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual API key
    api_key = "AIzaSyDKHoaT4TjFd01BJkgLlLm2s-RTeBQhdJM"

    # Replace 'YOUR_SEARCH_QUERY' with your search term
    search_query = "how to analyze the stock market in tamil"

    analyze_and_save(api_key, search_query)