import pytest
from shopping_cart import (
    add_to_cart,
    remove_from_cart,
    is_cart_empty,
    find_item,
)

# Assertions Exercise -------------------------------------------------------------

"""Test 1: Add Item to Cart"""
def test_add_to_cart():
    #Write your code below
    pass


"""Test 2: Remove Item from Cart"""
def test_remove_from_cart():
    #Write your code below
    pass


"""Test 3: Check for Empty Cart"""
def test_is_cart_empty():
    #Write your code below
    pass


# Error handling Exercise -------------------------------------------------------------
"""Test 1: Built-in Exceptions"""
from shopping_cart import add_to_cart2
def test_add_to_cart2():
    # Test valid quantity
    pass

    # Test invalid negative quantity




"""Test 2: Custom Exceptions"""

from shopping_cart import (
    CartError,
    checkout
)

def test_checkout():
    # Test non-empty cart
    pass

    # Test empty cart raises CartError
    



#----------------------------------------------------------------------------------------------------
# Fixtures Exercise
from shopping_cart import (
    total_items,
    total_price
)

"""Fixtures"""
# Write decorator
def filled_cart():
    # Returns filled cart
    pass

# Write decorator
def price_map():
    # Returns price map
    pass


"""Test 1: Check Total Number of Items"""
def test_total_items(): # Pass in needed fixture
    # Test total_items() using fixture
    pass


"""Test 2: Get Total Price"""
def test_total_price(): # Pass in needed fixtures
    # Test total_price() using fixtures
    pass

#----------------------------------------------------------------------------------------------------
# Marking Exercise
from shopping_cart import(
    reset_cart,
    find_item
)

"""Test 1: Check Reset Cart (Skip this test)"""
# Write Marking for Q3
# Write Marking for Q1
def test_reset_cart(filled_cart):
    updated_cart = reset_cart(filled_cart)
    assert updated_cart == []


"""Test 2: Check Items in Cart"""
# Marking for Q3
# Marking for Q2
def test_find_items(filled_cart, item, expected):
    # Test find_item() output
    pass

#----------------------------------------------------------------------------------------------------
# Mocking Exercise
from unittest.mock import patch
from shopping_cart import get_discounted_price

"""Test 1: Check Discounted Price"""
def test_get_discounted_price(filled_cart, price_map):
    # Mock return values for randint and total_price
    # Test get_discounted_price
    pass