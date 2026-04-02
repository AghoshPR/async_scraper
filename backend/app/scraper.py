import asyncio
import aiohttp
import csv
import os

DATA_FILE = "data/data.csv"

URLS = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
]

async def fetch(session,url):

    try:

        async with session.get(url,timeout=5) as response:

            return await response.json()
    
    except Exception as e:
        print(f"Error:{e}")
        return None

async def main():

    async with aiohttp.ClientSession() as session:

        tasks = [fetch(session,url) for url in URLS]
        results = await asyncio.gather(*tasks)

        os.makedirs("data",exist_ok=True)

        with open(DATA_FILE,"w",newline="",encoding="utf-8") as f:

            writer = csv.writer(f)
            writer.writerow(["id","title"])

            for item in results:

                if item:
                    writer.writerow([item["id","title"]])

if __name__ == "__main__":
    asyncio.run(main())