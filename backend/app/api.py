from fastapi import FastAPI
import csv

app = FastAPI()

@app.get("/data")
def get_data():

    result = []

    with open("data/data.csv",newline="",encoding="utf-8") as f:

        reader = csv.DictReader(f)

        for row in reader:
            result.append(row)
    
    return result