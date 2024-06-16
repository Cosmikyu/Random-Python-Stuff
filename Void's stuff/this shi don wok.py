# this shit don work bro :(


from networkx import is_path
import requests
from bs4 import BeautifulSoup
import csv
import os
import networkx

# URL to scrape
URL = "https://www.bbc.com/news"

try:
    # Send GET request
    response = requests.get(URL)
    response.raise_for_status()  # Raise HTTPError for bad responses

    # Parse HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all article titles
    titles = soup.find_all("h3", class_="gs-c-promo-heading__title")

    # Open a CSV file to write the titles
    with open(is_path, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        
        if not file_exists:
            writer.writerow(["Title"])
        
        
        # Extract and write the text of each title
        for title in titles:
            writer.writerow([title.get_text()])

    print(f"Titles have been written to {file_path}")

except requests.RequestException as e:
    print(f"An error occurred: {e}")
