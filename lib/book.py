class Book:
    """A class representing a book in the bookstore."""
    
    def __init__(self, title, page_count):
        """Initialize a Book instance with title and page_count."""
        self.title = title
        self.page_count = page_count
    
    @property
    def page_count(self):
        """Get the page count of the book."""
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        """Set the page count with validation."""
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")
            self._page_count = 0
    
    def turn_page(self):
        """Simulate turning a page in the book."""
        print("Flipping the page...wow, you read fast!")