import requests
import pandas as pd
import matplotlib.pyplot as plt


API_URL = "https://example.com/api/students_list"

# - - - Fetch data from API - - - 

def fetch_data():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()


# - - - Main Logic - - -

def main():
    # Example API response (We shall use fetch_data() in real case)
    data = [
        {"name": "Harry", "score": 100},
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 92},
        {"name": "Anne", "score": 75}
    ]

    # Convert JSON to DataFrame
    df = pd.DataFrame(data)

    # Calculate average score
    average_score = df["score"].mean()
    print(f"Average Score: {average_score:.2f}")		# Average Score: 88.00

    # Create bar chart
    plt.figure()
    plt.bar(df["name"], df["score"])
    plt.axhline(average_score)		# Avg. score reference line
    plt.xlabel("Students")
    plt.ylabel("Scores")
    plt.title("Student Test Scores")
    plt.show()

if __name__ == "__main__":
    main()