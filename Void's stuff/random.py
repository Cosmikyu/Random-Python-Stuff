import random
import string
import requests


def generate_random_youtube_link():
    # Valid characters for YouTube video IDs
    characters = string.ascii_letters + string.digits + '-' + ''
    # YouTube video ID consists of 11 characters
    video_id = ''.join(random.choices(characters, k=11))
    youtubelink = f"{video_id}"
    return youtubelink

if __name__ == "__main__":
    random_youtube_link = generate_random_youtube_link()
    print("Random YouTube Link:")
    print(random_youtube_link)
    
    r = requests.get("https://www.youtube.com/watch?v={youtubelink}") # random video id
"Video unavailable" in r.text



