import pytest

#-------------------------------------------------------------------------
#Assertion Exercise
from shopping_cart import (
    add_to_cart,
    remove_from_cart,
    is_cart_empty,
    find_item
)

"""Test 1: Add Item to Cart"""
def test_add_to_cart():
    cart = []
    add_to_cart(cart, "apple")
    assert cart == ["apple"]  # Check that "apple" was added to the cart
    add_to_cart(cart, "banana")
    assert cart == ["apple", "banana"]  # Check that "banana" was also added


"""Test 2: Remove Item from Cart"""
def test_remove_from_cart():
    cart = ["apple", "banana"]
    remove_from_cart(cart, "apple")
    assert cart == ["banana"]  # Check that "apple" was removed
    remove_from_cart(cart, "orange")  # Try to remove an item not in the cart
    assert cart == ["banana"]  # Cart remains unchanged


"""Test 3: Check for Empty Cart"""
def test_is_cart_empty():
    cart = []
    assert is_cart_empty(cart) is True  # Cart is empty
    cart.append("apple")
    assert is_cart_empty(cart) is False  # Cart is not empty

#----------------------------------------------------------------------------------
#Error Raising Exercise

"""Built-in Exceptions"""
from shopping_cart import (
    add_to_cart2
)

def test_add_to_cart2():
    # Test valid quantity
    assert add_to_cart2("apple", 3) == "3 apple(s) added to the cart!"

    # Test invalid negative quantity
    with pytest.raises(ValueError):
        add_to_cart2("apple", -1)


"""Custom Exceptions"""
from shopping_cart import (
    CartError,
    checkout
)

def test_checkout():
    # Test non-empty cart
    assert checkout(["apple", "banana", "carrot"]) == "Checked out 3 item(s)!"

    # Test empty cart raises CartError
    with pytest.raises(CartError, match="Cannot checkout an empty cart."):
        checkout([])

#----------------------------------------------------------------------------------------------------
# Fixtures Exercise
from shopping_cart import (
    total_items,
    total_price
)

"""Fixtures"""
@pytest.fixture
def filled_cart():
    return ["apple", "banana", "strawberry"]

@pytest.fixture
def price_map():
    return {'apple': 1, 'orange': 2, 'banana': 3, 'strawberry': 4}


"""Test 1: Check Total Number of Items"""
def test_total_items(filled_cart):
    assert total_items(filled_cart) == 3 


"""Test 2: Get Total Price"""
def test_total_price(filled_cart, price_map):
    expected_total_price = 1+3+4
    assert total_price(filled_cart, price_map) == expected_total_price

#----------------------------------------------------------------------------------------------------
# Marking Exercise
from shopping_cart import(
    reset_cart,
    find_item
)

"""Test 1: Check Total Number of Items"""
@pytest.mark.marking
@pytest.mark.skip(reason="Remove functionality not yet implemented")
def test_reset_cart(filled_cart):
    updated_cart = reset_cart(filled_cart)
    assert updated_cart == []


"""Test 2: Check Items in Cart"""
@pytest.mark.marking
@pytest.mark.parametrize(
    "item, expected",
    [
        ('apple', True),
        ('banana', True),
        ('cherry', False)
    ]
)
def test_find_items(filled_cart, item, expected):
    assert find_item(filled_cart, item) == expected

#----------------------------------------------------------------------------------------------------
# Mocking Exercise
from shopping_cart import get_discounted_price
from unittest.mock import patch

"""Test 1: Check Discounted Price"""
def test_get_discounted_price(filled_cart, price_map):
    with patch("random.randint") as mock_randint, patch("shopping_cart.total_price") as mock_total_price:
        mock_randint.return_value = 7
        mock_total_price.return_value = 1+3+4
	
        discounted_price = get_discounted_price(filled_cart, price_map)
        assert discounted_price == round((1+3+4)*0.1, 2)
