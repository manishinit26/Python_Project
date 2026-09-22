import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Book Analytics", layout="wide")
st.title("📚 Book Analytics Dashboard")

# Fetch data from your running FastAPI server
try:
    response = requests.get("http://127.0.0.1:8000/books")
    response.raise_for_status()
    books_data = response.json()
    
    df = pd.DataFrame(books_data)
    
    st.subheader("Database Records")
    # Renders the pandas dataframe as an interactive web table
    st.dataframe(df, use_container_width=True) 

    st.subheader("Price vs. Rating Analysis")
    # Generate the matplotlib chart
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.scatter(df['price'], df['rating'], color='blue', alpha=0.7, edgecolors='black', s=100)
    ax.set_title("Book Price vs. Rating")
    ax.set_xlabel("Price (£)")
    ax.set_ylabel("Rating (1-5 Stars)")
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.grid(True, linestyle='--', alpha=0.5)
    
    # Renders the chart on the web page
    st.pyplot(fig) 

except Exception as e:
    st.error(f"Failed to connect to API. Is the FastAPI server running in Terminal 1? Error: {e}")