# Async Scraper Dashboard

An asynchronous web scraping system built using Python (aiohttp and FastAPI) and React. The project demonstrates how to collect data concurrently, process it, and display it through a frontend dashboard.

---

## Project Overview

This project is a simple full-stack application that follows a complete data flow:

* A Python-based scraper collects data from multiple sources using asynchronous requests
* The scraped data is stored in a CSV file
* A FastAPI backend reads the data and exposes it through an API
* A React frontend fetches the API data and displays it in a structured format

---

## Tech Stack

Backend:

* Python
* asyncio
* aiohttp
* FastAPI

Frontend:

* React (Vite)
* Axios

---

## Key Features

* Asynchronous data fetching using asyncio
* Concurrent HTTP requests with aiohttp
* Data processing and storage in CSV format
* REST API built with FastAPI
* Frontend dashboard using React
* End-to-end data flow from scraper to UI

---

## Project Structure

```

async_scraper/
│
├── backend/
│   ├── app/
│   │   ├── api.py
│   │   ├── scraper.py
│   │   └── __pycache__/
│   │
│   ├── data/
│   │   └── data.csv
│   │
│   ├── scraper_env/        # virtual environment (ignored in git)
│   └── requirements.txt
│
├── frontend/
│   ├── node_modules/       # dependencies (ignored in git)
│   ├── public/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   ├── App.css
│   │   └── index.css
│   │
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   ├── eslint.config.js
│   └── .gitignore
│
├── .gitignore
├── LICENSE
└── README.md
```



---

## How It Works

The scraper sends multiple requests concurrently and collects data.
This data is saved into a CSV file.
The FastAPI backend reads the CSV file and provides an API endpoint.
The React frontend calls this API and displays the data in a table.

---

## Getting Started

Clone the repository:

```
git clone https://github.com/AghoshPR/async_scraper.git
cd async_scraper
```

---

### Backend Setup

```
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Run the scraper:

```
python app/scraper.py
```

Run the API server:

```
uvicorn app.api:app --reload
```

Open in browser:
http://127.0.0.1:8000/data

---

### Frontend Setup

```
cd frontend
npm install
npm run dev
```

Open in browser:
http://localhost:5173

---

## Sample Output

The frontend displays data in a simple table with id and title fields fetched from the backend API.

---


## Author

Aghosh PR


---

## License

This project is licensed under the MIT License.
