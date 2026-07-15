import pytest
from ..coffee import Coffee  # ← This imports from parent lib directory

def test_coffee_creation():
    coffee = Coffee("Medium", 4.50)
    assert coffee.size == "Medium"
    assert coffee.price == 4.50

def test_size_validation_valid():
    small = Coffee("Small", 3.50)
    medium = Coffee("Medium", 4.50)
    large = Coffee("Large", 5.50)
    
    assert small.size == "Small"
    assert medium.size == "Medium"
    assert large.size == "Large"

def test_size_validation_invalid(capsys):
    coffee = Coffee("Extra Large", 5.00)
    captured = capsys.readouterr()
    assert "size must be Small, Medium, or Large" in captured.out
    assert coffee.size == "Small"

def test_price_setting():
    coffee = Coffee("Small", 3.50)
    assert coffee.price == 3.50
    
    coffee.price = 4.00
    assert coffee.price == 4.00

def test_tip_method(capsys):
    coffee = Coffee("Large", 5.00)
    original_price = coffee.price
    
    coffee.tip()
    captured = capsys.readouterr()
    
    assert "This coffee is great, here's a tip!" in captured.out
    assert coffee.price == original_price + 1

def test_tip_multiple_times():
    coffee = Coffee("Medium", 4.50)
    
    coffee.tip()
    assert coffee.price == 5.50
    
    coffee.tip()
    assert coffee.price == 6.50
    
    coffee.tip()
    assert coffee.price == 7.50