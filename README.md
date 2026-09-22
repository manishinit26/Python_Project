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


## 💻 Complete Step-by-Step Setup Guide

Follow these instructions to set up the environment and run the pipeline from start to finish.

### 1. Environment Setup
Clone the repository and open the folder in your terminal (or VS Code). Initialize and activate a virtual environment.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate


## ⚙️ Execution Instructions

This project requires running a backend server and frontend clients simultaneously using two separate terminal windows.

### Phase 1: Initialize the Database (Terminal 1)
Ensure your virtual environment is active. Run the database script to scrape the website and generate the `books.db` file.

```bash
python database.py

Bash
uvicorn main:app
