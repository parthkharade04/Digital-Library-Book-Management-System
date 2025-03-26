from src.db.database import cursor, conn

def add_book(book):
    try:
        cursor.execute("INSERT INTO books VALUES (?, ?, ?, ?, ?)", (book.id, book.title, book.author, book.genre, book.status))
        conn.commit()
        return {"message": "Book added successfully"}
    except Exception as e:
        return {"error": str(e)}

def get_all_books():
    cursor.execute("SELECT * FROM books")
    return {"books": cursor.fetchall()}

def search_book(book_id=None, title=None):
    if book_id:
        cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
    elif title:
        cursor.execute("SELECT * FROM books WHERE title LIKE ?", (f"%{title}%",))
    else:
        return {"error": "Provide either book ID or title"}
    
    return {"books": cursor.fetchall()}
    
def update_book(book_id, book):
    cursor.execute("UPDATE books SET title=?, author=?, genre=?, status=? WHERE id=?", 
                   (book.title, book.author, book.genre, book.status, book_id))
    conn.commit()
    return {"message": "Book updated successfully"}

def delete_book(book_id):
    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    return {"message": "Book deleted successfully"}
