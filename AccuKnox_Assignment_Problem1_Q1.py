
import requests		# For API calls
import sqlite3		# Local SQLite database

API_URL = "https://www.exampleapi.com/api/books_list/"	# Example API
DB_NAME = "book_list.db"		# Database name

# - - - 1. Fetch Data from API - - -

def fetch_books():
	response = requests.get(API_URL)
	response.raise_for_status()	# Raises error for failed request
	return response.json()

# - - - 2. Initialize SQLite Database - - -

def init_db():
	conn = sqlite3.connect(DB_NAME)
	cursor = conn.cursor()		# Control structure to interact with db
	cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL, 
author TEXT NOT NULL,
year INTEGER
)   
""")
	conn.commit()		# Permanently saves changes
	conn.close()		# Terminate database connection
	
	# - - - Store Data in DB - - -
	
	def store_books(books):
		conn = sqlite3.connect(DB_NAME)
		cursor = conn.cursor()
		
		for book in books:
			cursor.execute("""
				INSERT INTO books (title, author, year)
				VALUES (?, ?, ?)""",
				(book["title"], book["author"], book["year"])
				)

		conn.commit()
		conn.close()

	# - - - 3. Retrieve and Display Data - - -
	
	def display_books():
		conn = sqlite3.connect(DB_NAME)
		cursor = conn.cursor()
		
		cursor.execute(" SELECT title, author, year FROM books")
		rows = cursor.fetchall()		# Retrieve all rows from db
		
		print("\n Stored Books:")
		for title, author, year in rows:
			print("f - {title} by {author} ({year})")

		conn.close()		# Not using commit as no changes made to database
	
	if __name__ == "__main__":
		init_db()
		books = fetch_books()
		store_books(books)
		display_books()