class Coffee:
    """A class representing a coffee product in the bookstore cafe."""
    
    VALID_SIZES = ["Small", "Medium", "Large"]
    
    def __init__(self, size, price):
        """Initialize a Coffee instance with size and price."""
        self.size = size
        self.price = price
    
    @property
    def size(self):
        """Get the size of the coffee."""
        return self._size
    
    @size.setter
    def size(self, value):
        """Set the size with validation."""
        if value in self.VALID_SIZES:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")
            self._size = "Small"
    
    @property
    def price(self):
        """Get the price of the coffee."""
        return self._price
    
    @price.setter
    def price(self, value):
        """Set the price."""
        self._price = float(value)
    
    def tip(self):
        """Process a tip for the coffee - adds 1 to price."""
        print("This coffee is great, here’s a tip!")
        self.price += 1