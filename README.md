# Bookstore Object-Oriented Programming Lab

## 📚 Overview

This project implements an Object-Oriented Programming solution for a bookstore management system. It consists of two main classes that model different products carried by the store:

- **Book Class** - Represents books available in the store
- **Coffee Class** - Represents coffee products sold in the store's cafe

Both classes feature attribute validation, properties, and methods that simulate real-world bookstore operations.

---

## 🎯 Project Objectives

- Demonstrate understanding of Python classes and Object-Oriented Programming
- Implement attribute validation using properties and setters
- Create methods that modify object state
- Write clean, documented, and testable code
- Pass all unit tests for both classes

---

## 📦 Class Descriptions

### Book Class

The `Book` class represents a book with the following features:

#### Attributes
| Attribute | Type | Description |
|-----------|------|-------------|
| `title` | String | The title of the book |
| `page_count` | Integer | Number of pages in the book |

#### Properties
- **`page_count`**: Validates that the value is an integer. Prints an error message and sets to `0` if validation fails.

#### Methods
| Method | Description |
|--------|-------------|
| `turn_page()` | Simulates turning a page in the book. Prints: *"Flipping the page...wow, you read fast!"* |

#### Usage Example
```python
from lib.book import Book

# Create a book
book = Book("The Great Gatsby", 180)

# Access attributes
print(book.title)        # "The Great Gatsby"
print(book.page_count)   # 180

# Turn a page
book.turn_page()         # "Flipping the page...wow, you read fast!"

# Test validation (will print error)
bad_book = Book("Invalid", "not a number")
# Output: page_count must be an integer
print(bad_book.page_count)  # 0