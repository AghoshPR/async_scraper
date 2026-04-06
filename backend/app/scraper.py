import asyncio
import aiohttp
import csv
import os
from bs4 import BeautifulSoup

DATA_FILE = "data/data.csv"

# URL = "https://news.ycombinator.com/"


async def fetch(session, url):

    try:

        async with session.get(url, timeout=5) as response:

            return await response.text()

    except Exception as e:
        print(f"Error:{e}")
        return None


def parse_html(html, selector):
    soup = BeautifulSoup(html, "html.parser")

    if not selector or selector.strip() == "":
        return []

    elements = soup.select(selector)

    data = []

    for index, item in enumerate(elements, start=1):
        text = item.get_text(strip=True)

        if text:

            data.append({
                "id": index,
                "title": text
            })
    return data


async def run_scraper(url, selector):

    async with aiohttp.ClientSession() as session:

        html = await fetch(session, url)

        if not html:
            return []

        results = parse_html(html, selector)

        os.makedirs("data", exist_ok=True)

        with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:

            writer = csv.writer(f)
            writer.writerow(["id", "title"])

            for item in results:
                if item:
                    writer.writerow([item["id"], item["title"]])
        return results
