import pytest
from ..book import Book  # ← This imports from parent lib directory

def test_book_creation():
    book = Book("The Great Gatsby", 180)
    assert book.title == "The Great Gatsby"
    assert book.page_count == 180

def test_page_count_validation_with_integer():
    book = Book("Python 101", 250)
    assert book.page_count == 250

def test_page_count_validation_with_string(capsys):
    book = Book("Invalid Book", "not a number")
    captured = capsys.readouterr()
    assert "page_count must be an integer" in captured.out
    assert book.page_count == 0

def test_turn_page(capsys):
    book = Book("Test Book", 100)
    book.turn_page()
    captured = capsys.readouterr()
    assert "Flipping the page...wow, you read fast!" in captured.out

def test_multiple_books():
    book1 = Book("Book One", 100)
    book2 = Book("Book Two", 200)
    assert book1.title != book2.title
    assert book1.page_count != book2.page_count