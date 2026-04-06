from fastapi import FastAPI
import csv
from app.scraper import run_scraper
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class URLRequest(BaseModel):
    url:str
    selector : str

@app.get("/data")
def get_data():

    result = []

    try:

         with open("data/data.csv", newline="", encoding="utf-8") as f:

            reader = csv.DictReader(f)

            for row in reader:
                result.append(row)

    except FileNotFoundError:
        return []


    return result


@app.post("/scrape")
async def scrape_url(request:URLRequest):

    data = await run_scraper(request.url,request.selector)
    return data



