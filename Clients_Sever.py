import requests
import pandas as pd
import matplotlib.pyplot as plt

def run_analytics_client():
    # 1. Fetch data from the FastAPI GET endpoint
    api_url = "http://127.0.0.1:8000/books"
    print(f"Fetching data from {api_url}...")
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        books_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to API. Is the FastAPI server running? Details: {e}")
        return

    # 2. Load into a Pandas DataFrame and print to console
    df = pd.DataFrame(books_data)
    print("\n--- Data successfully loaded into Pandas DataFrame ---")
    print(df.head()) # Print first 5 rows to verify
    
    # 3. Export to CSV
    csv_filename = "exported_books.csv"
    df.to_csv(csv_filename, index=False)
    print(f"\nData exported successfully to {csv_filename}")

    # 4. Generate Scatter Plot (Price vs Rating)
    plt.figure(figsize=(10, 6))
    plt.scatter(df['price'], df['rating'], color='blue', alpha=0.7, edgecolors='black', s=100)
    
    plt.title("Book Price vs. Rating (First 20 Books)", fontsize=14)
    plt.xlabel("Price (£)", fontsize=12)
    plt.ylabel("Rating (1-5 Stars)", fontsize=12)
    plt.yticks([1, 2, 3, 4, 5]) # Ensure Y-axis only shows discrete 1-5 ratings
    plt.grid(True, linestyle='--', alpha=0.5)
    
    # 5. Save the chart
    plot_filename = "price_vs_rating.png"
    plt.savefig(plot_filename)
    print(f"Scatter plot saved successfully as {plot_filename}")

if __name__ == "__main__":
    run_analytics_client()