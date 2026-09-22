# 📚 End-to-End Book Data Pipeline & Analytics System

An end-to-end Python data pipeline that extracts book data from the web, manages it in a local database using Object-Oriented Programming (OOP), exposes it via a custom REST API, and consumes it through analytical client scripts and an interactive web dashboard.

## 🚀 Project Overview
This project demonstrates a complete data engineering and backend architecture. It bridges the gap between raw data collection and actionable data visualization, utilizing the exact framework used to feed real-time data into Machine Learning models and analytics systems.

### Core Features
* **Web Scraping Engine:** Extracts live data (Title, Price, Availability, and Rating) from `books.toscrape.com` using BeautifulSoup.
* **OOP Database Management:** Built an SQLite database manager class to seamlessly handle full CRUD (Create, Read, Update, Delete) operations.
* **REST API Microservice:** Deployed a FastAPI server to securely expose the database via standardized HTTP endpoints (`GET`, `POST`, `PUT`, `DELETE`).
* **Analytics Client:** Consumes the API payload using Pandas to clean the data, exports it to a CSV, and generates a Price vs. Rating scatter plot using Matplotlib.
* **Interactive Web Dashboard:** Includes a Streamlit web application to visualize the data dynamically in the browser.

## 🛠️ Technology Stack
* **Language:** Python 3.x
* **Data Extraction:** `requests`, `beautifulsoup4`
* **Database:** `sqlite3` (Built-in)
* **API Framework:** `fastapi`, `uvicorn`, `pydantic`
* **Data Analytics:** `pandas`, `matplotlib`
* **Frontend Web App:** `streamlit`

## 📂 Project Structure
* `web_scraper.py` - Scrapes book records from the target website.
* `database.py` - Manages the SQLite schema and runs the scraper to populate `books.db`.
* `main.py` - Contains the FastAPI application and REST endpoints.
* `Clients_Sever.py` - Standalone client that requests API data, generates a CSV, and plots the data.
* `webapp.py` - Streamlit dashboard for interactive browser visualization.

## 💻 Installation & Setup

**1. Clone the repository and navigate into the project directory:**
```bash
git clone [https://github.com/divishagarg/End-to-End-Book-Data-Pipeline-Analytics-System.git](https://github.com/divishagarg/End-to-End-Book-Data-Pipeline-Analytics-System.git)
cd End-to-End-Book-Data-Pipeline-Analytics-System
