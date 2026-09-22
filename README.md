# 📚 Python Capstone Project: End-to-End Book Data Pipeline

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas)

A complete data engineering pipeline that extracts book data from the web, manages it in a local database using Object-Oriented Programming (OOP), exposes it via a custom REST API, and visualizes it through analytical client scripts and an interactive web dashboard.

## 🚀 Project Overview

This project bridges the gap between raw data collection and actionable data visualization. It utilizes the exact foundational architecture used by Data and AI Engineers to feed real-time data into analytics systems and machine learning models.

### Core Architecture
1. **Web Scraping Engine:** Extracts live book data (Title, Price, Availability, and Rating) from `books.toscrape.com`.
2. **Database Management (OOP):** Uses an SQLite database manager class to seamlessly handle full CRUD (Create, Read, Update, Delete) operations.
3. **REST API Microservice:** Deploys a FastAPI server to securely expose the database via standardized HTTP endpoints (`GET`, `POST`, `PUT`, `DELETE`).
4. **Analytics Client:** Consumes the API payload using Pandas to clean the data, exports it to a CSV, and generates a Price vs. Rating scatter plot using Matplotlib.
5. **Interactive Web Dashboard:** A Streamlit application for dynamic, in-browser data visualization.

---

## 📂 Repository Structure

* `web_scraper.py` — Web scraping script using BeautifulSoup.
* `database.py` — Manages the SQLite schema and populates `books.db`.
* `main.py` — The FastAPI microservice and REST endpoints.
* `Clients_Sever.py` — Standalone client script to fetch API data, generate CSVs, and plot charts.
* `webapp.py` — Streamlit dashboard for interactive UI visualization.

---

## 💻 Installation & Setup

**1. Clone the repository:**
```bash
git clone [https://github.com/manishinit26/Python_Project.git](https://github.com/manishinit26/Python_Project.git)
cd Python_Project

2. Initialize and activate a virtual environment:
Windows:

Bash
python -m venv venv
venv\Scripts\activate
macOS/Linux:

Bash
python3 -m venv venv
source venv/bin/activate
3. Install all required dependencies:

Bash
pip install requests beautifulsoup4 fastapi uvicorn pydantic pandas matplotlib streamlit




