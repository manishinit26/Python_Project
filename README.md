# 📚 Python Capstone Project: End-to-End Book Data Pipeline

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas)

A complete data engineering pipeline that extracts book data from the web, manages it in a local database using Object-Oriented Programming (OOP), exposes it via a custom REST API, and visualizes it through analytical client scripts and an interactive web dashboard.


## 🚀 Project Features
* **Automated Web Scraping:** Extracts live book data (Title, Price, Availability, Rating) from `books.toscrape.com`.
* **OOP Database Management:** Utilizes a custom Python class to handle full CRUD operations within an SQLite database.
* **RESTful Microservice:** Deploys a FastAPI backend to securely expose the scraped data via standard HTTP endpoints.
* **Data Analytics & Export:** Consumes API data using Pandas to generate CSV exports and Matplotlib for scatter plot visualizations.
* **Interactive UI:** Features a Streamlit dashboard for real-time, browser-based data exploration.

## 🛠️ Technology Stack
* **Language:** Python 3.x
* **Data Extraction:** `requests`, `beautifulsoup4`
* **Database:** `sqlite3` (Built-in)
* **Backend API:** `fastapi`, `uvicorn`, `pydantic`
* **Data Analytics:** `pandas`, `matplotlib`
* **Frontend Web App:** `streamlit`

## 📂 Project Structure
```text
Python_Project/
│
├── web_scraper.py         # Scrapes book records from the target website
├── database.py            # Manages the SQLite schema and runs the scraper
├── main.py                # Contains the FastAPI application and REST endpoints
├── Clients_Sever.py       # Standalone client to fetch API data, generate CSV, and plot charts
├── webapp.py              # Streamlit dashboard for interactive browser visualization
│
├── requirements.txt       # (Optional) List of project dependencies
└── README.md              # Project documentation

## Setup

### 1. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

## How to Run the Project

### 1. Scrape the data and populate the database

```powershell
python web_scraper.py
```

This creates or refreshes `books.db` and stores the first 20 books.

### 2. Start the FastAPI server

```powershell
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### 3. Run the client script

In a second terminal, while the API server is running:

```powershell
python Clients_Server.py
```

The client will:

- Call `GET /books`
- Print the results as a Pandas DataFrame
- Export `exported_books.csv`
- Create `price_vs_rating.png`
- Also create `price_vs_rating.svg` so the chart can be opened as text in the editor

## REST API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/books` | Retrieve all books |
| GET | `/books/{id}` | Retrieve one book by ID |
| POST | `/books` | Create a new book |
| PUT | `/books/{id}` | Update an existing book |
| DELETE | `/books/{id}` | Delete a book |

### Example Book JSON

```json
{
  "title": "A Light in the Attic",
  "price": 51.77,
  "in_stock": "In stock",
  "rating": 3
}
```

## Output Files

After a successful run, you should see these generated files:

- `books.db` - SQLite database
- `exported_books.csv` - Clean CSV export from the API data
- `price_vs_rating.png` - Scatter plot of price vs rating
- `price_vs_rating.svg` - Editable text-based version of the plot

## Expected Result

The scraper should return exactly 20 records from the main page of Books to Scrape. The client should print a DataFrame showing those 20 rows, export the CSV, and save the scatter plot.


## Troubleshooting

- If the client says it cannot reach the API, make sure `uvicorn main:app --reload` is still running.
- If `books.db` is empty, run `python scraper.py` again before starting the API.
- If PowerShell blocks virtual environment activation, run PowerShell as a normal user and allow script execution for the session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## Notes

- The scraper only targets the first 20 books, as required by the project scope.
- The database layer uses an object-oriented manager class for CRUD operations.
- The project was validated end to end against the live site.

