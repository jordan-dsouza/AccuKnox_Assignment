import csv
import sqlite3

# - - - Configuration - - -
CSV_FILE = "users.csv"
DB_FILE = "users.db"

# - - - Initialize database - - -
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# - - - Insert CSV data into database - - -

def insert_users_from_csv():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    with open(CSV_FILE, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute(
                "INSERT INTO users (name, email) VALUES (?, ?)",
                (row["name"], row["email"])
            )

    conn.commit()
    conn.close()

# - - - Main execution - - -
if __name__ == "__main__":
    init_db()
    insert_users_from_csv()
    print("CSV data successfully inserted into SQLite database.")