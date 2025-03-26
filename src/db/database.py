import sqlite3

# Database Connection
conn = sqlite3.connect("library.db", check_same_thread=False)
cursor = conn.cursor()

# Create Books Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        genre TEXT,
        status TEXT CHECK(status IN ('Available', 'Checked Out')) NOT NULL
    )
''')
conn.commit()
