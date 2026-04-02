from fastapi import FastAPI
import csv

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/data")
def get_data():

    result = []

    with open("data/data.csv", newline="", encoding="utf-8") as f:

        reader = csv.DictReader(f)

        for row in reader:
            result.append(row)

    return result
