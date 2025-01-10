import pytest
from starting_code.shopping_cart import (
    add_to_cart,
    remove_from_cart,
    is_cart_empty,
    find_item,
)

# Assertions Exercise

"""Test 1: Add Item to Cart"""
def test_add_to_cart():
    """Write your code below"""




"""Test 2: Remove Item from Cart"""
"""Write your code below"""




"""Test 3: Check for Empty Cart"""
"""Write your code below"""




"""Test 4: Check if Item in Cart"""
def test_find_item():
    cart = ["apple", "banana"]

"""Write your code below"""



# Error handling Exercise
"""Test 1: Built-in Exceptions"""
from starting_code.shopping_cart import add_to_cart2
def test_add_to_cart():
    # Test valid quantity
    pass

    # Test invalid negative quantity




# """Test 2: Custom Exceptions"""

from starting_code.shopping_cart import (
    CartError,
    checkout
)

def test_checkout():
    # Test non-empty cart
    pass

    # Test empty cart raises CartError
    



# Fixtures Exercise

# Marking Exercise

# Mocking Exercise