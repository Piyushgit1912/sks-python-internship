# 1. SOURCE CODE: Task_4_Web_Scraper/scraper.py

"""
Task 4: Basic Web Scraper
Features:
- Scrapes articles, headlines, and links from live web pages using requests and BeautifulSoup.
- Formats and displays extracted data cleanly in the terminal.
- Exports structured scraped data into JSON and CSV formats.
- Comprehensive network and HTTP exception handling (ConnectionError, Timeout, HTTPError).
"""

import json
import csv
import sys
import requests
from bs4 import BeautifulSoup


class WebScraper:
    def __init__(self, url: str):
        self.url = url
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/118.0.0.0 Safari/537.36"
            )
        }
        self.extracted_items = []

    def fetch_page_content(self) -> str:
        """Fetches raw HTML content from the configured URL with error handling."""
        try:
            response = requests.get(self.url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.MissingSchema:
            raise ValueError("Invalid URL format. Please include http:// or https://")
        except requests.exceptions.ConnectionError:
            raise ConnectionError(f"Failed to connect to '{self.url}'. Check your internet connection.")
        except requests.exceptions.Timeout:
            raise TimeoutError("The request timed out after 10 seconds.")
        except requests.exceptions.HTTPError as err:
            raise RuntimeError(f"HTTP Error occurred: {err}")

    def scrape_quotes_or_articles(self) -> list:
        """
        Parses web content. Designed to scrape elements such as quotes, 
        news headlines, or article cards.
        """
        html = self.fetch_page_content()
        soup = BeautifulSoup(html, "html.parser")
        self.extracted_items = []

        # Example parser targeting quotes.toscrape.com / standard article cards
        cards = soup.find_all("div", class_="quote")
        if cards:
            for idx, card in enumerate(cards, 1):
                text_elem = card.find("span", class_="text")
                author_elem = card.find("small", class_="author")
                text = text_elem.get_text(strip=True) if text_elem else "No Text"
                author = author_elem.get_text(strip=True) if author_elem else "Anonymous"
                self.extracted_items.append({
                    "id": idx,
                    "title_or_text": text,
                    "author_or_source": author
                })
        else:
            # Generic fallback: scrape common headline tags (h1, h2, h3)
            headings = soup.find_all(["h1", "h2", "h3"])
            for idx, heading in enumerate(headings, 1):
                title = heading.get_text(strip=True)
                if title:
                    self.extracted_items.append({
                        "id": idx,
                        "title_or_text": title,
                        "author_or_source": self.url
                    })

        return self.extracted_items

    def export_to_json(self, file_path: str = "scraped_data.json"):
        """Exports extracted data to a JSON file."""
        if not self.extracted_items:
            print("No items to export.")
            return
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(self.extracted_items, f, indent=4, ensure_ascii=False)
        print(f"Data successfully exported to JSON: {file_path}")

    def export_to_csv(self, file_path: str = "scraped_data.csv"):
        """Exports extracted data to a CSV file."""
        if not self.extracted_items:
            print("No items to export.")
            return
        keys = self.extracted_items[0].keys()
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(self.extracted_items)
        print(f"Data successfully exported to CSV: {file_path}")


def main():
    print("\n==========================================")
    print("         BASIC WEB SCRAPER TOOL           ")
    print("==========================================")
    print("Default demo target: https://quotes.toscrape.com")
    
    target_url = input("Enter target URL (Press Enter for default demo): ").strip()
    if not target_url:
        target_url = "https://quotes.toscrape.com"

    scraper = WebScraper(target_url)

    try:
        print(f"\nFetching and parsing: {target_url}...")
        results = scraper.scrape_quotes_or_articles()
        
        if not results:
            print("No matching content or headlines found.")
            return

        print(f"\n--- Extracted {len(results)} Items ---")
        for item in results[:5]:  # Display top 5 in console
            print(f"[{item['id']}] {item['title_or_text']}")
            print(f"     Source/Author: {item['author_or_source']}\n")
        
        if len(results) > 5:
            print(f"... and {len(results) - 5} more items.\n")

        scraper.export_to_json("scraped_data.json")
        scraper.export_to_csv("scraped_data.csv")

    except Exception as e:
        print(f"\n[Scraper Error]: {e}")


if __name__ == "__main__":
    main()

