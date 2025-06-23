"""
Simple Web Scraper
Author: Diego Domínguez
Date: 2025-06-23
"""

import requests
from bs4 import BeautifulSoup
from typing import List
import logging

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

URL = "https://www.bbc.com/mundo"
HEADERS = {"User-Agent": "Mozilla/5.0"}

# ---------------------------------------------------------------------------
# Logging setup
# ---------------------------------------------------------------------------

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

# ---------------------------------------------------------------------------
# Business logic
# ---------------------------------------------------------------------------

def fetch_page(url: str) -> str:
    """
    Sends a GET request to the specified URL and returns the HTML content.
    Returns an empty string if the request fails.
    """
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        logging.error(f"Failed to connect to the page: {e}")
        return ""

def extract_titles(html: str, class_name: str, limit: int = 5) -> List[str]:
    """
    Extracts and returns the text of <a> tags with the given class name.
    Limits the number of results returned to `limit`.
    """
    soup = BeautifulSoup(html, "html.parser")
    elements = soup.find_all("a", class_=class_name)

    if not elements:
        logging.warning("No titles found with the specified class.")
        return []

    titles = [element.get_text(strip=True) for element in elements[:limit]]
    return titles

# ---------------------------------------------------------------------------
# Presentation
# ---------------------------------------------------------------------------

def show_titles(titles: List[str]) -> None:
    """
    Displays the extracted titles in a numbered list.
    """
    if not titles:
        print("No news titles found.")
    else:
        print("📰 Retrieved News Titles:")
        for i, title in enumerate(titles, start=1):
            print(f"{i}. {title}")

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    """
    Entry point of the application: fetches the page, extracts titles, and prints them.
    """
    html = fetch_page(URL)
    if html:
        titles = extract_titles(html, "bbc-1i4ie53 e1d658bg0")
        show_titles(titles)

if __name__ == "__main__":
    main()
