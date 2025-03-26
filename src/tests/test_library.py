import pytest
from fastapi.testclient import TestClient
from src.main import app
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

client = TestClient(app)

# Sample test book data
test_book = {
    "id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "genre": "Fiction",
    "status": "Available"
}

def test_add_book():
    response = client.post("/add_book/", json=test_book)
    assert response.status_code == 200
    assert response.json() == {"message": "Book added successfully"}

def test_get_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert "books" in response.json()

def test_search_book_by_id():
    response = client.get("/search/", params={"book_id": 1})
    assert response.status_code == 200
    assert len(response.json()["books"]) > 0

def test_update_book():
    updated_book = test_book.copy()
    updated_book["status"] = "Checked Out"
    response = client.put("/update_book/1", json=updated_book)
    assert response.status_code == 200
    assert response.json() == {"message": "Book updated successfully"}

def test_delete_book():
    response = client.delete("/delete_book/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Book deleted successfully"}
