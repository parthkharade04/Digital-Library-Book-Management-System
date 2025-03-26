from fastapi import APIRouter, HTTPException
from src.models.book_model import Book
from src.services.book_service import add_book, get_all_books, search_book, update_book, delete_book

router = APIRouter()

@router.post("/add_book/")
def create_book(book: Book):
    result = add_book(book)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@router.get("/books/")
def view_books():
    return get_all_books()

@router.get("/search/")
def search_for_book(book_id: int = None, title: str = None):
    return search_book(book_id, title)

@router.put("/update_book/{book_id}")
def modify_book(book_id: int, book: Book):
    return update_book(book_id, book)

@router.delete("/delete_book/{book_id}")
def remove_book(book_id: int):
    return delete_book(book_id)
