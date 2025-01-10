import pytest
import shopping_cart as sc
from unittest.mock import patch

#-------------------------------------------------------------------------
#Assertion Exercise
from solution.shopping_cart import (
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




"""Test 4: Check if Item in Cart"""
def test_find_item():
    cart = ["apple", "banana"]
    assert find_item(cart, "apple") is True  # "apple" is in the cart
    assert find_item(cart, "orange") is False  # "orange" is not in the cart
#----------------------------------------------------------------------------------
#Error Raising Exercise

"""Built-in Exceptions"""
from solution.shopping_cart import (
    add_to_cart2
)

def test_add_to_cart2():
    # Test valid quantity
    assert add_to_cart2("apple", 3) == "3 apple(s) added to the cart!"

    # Test invalid negative quantity
    with pytest.raises(ValueError):
        add_to_cart2("apple", -1)

"""Custom Exceptions"""
from solution.shopping_cart import (
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




@pytest.fixture
def empty_cart():
    return []

@pytest.fixture
def filled_cart():
    return [{'item': 'apple', 'quantity': 2}, {'item': 'banana', 'quantity': 3}]

@pytest.fixture
def price_map():
    return {'apple': 1, 'orange': 2, 'banana': 3, 'cherry': 4}


def test_empty_cart_is_empty(empty_cart):
    assert sc.is_empty(empty_cart)


def test_add_item_to_cart(empty_cart, price_map):
    sc.add_item(empty_cart, 'orange', 1, price_map)
    assert not sc.is_empty(empty_cart)


def test_total_items_in_cart(filled_cart):
    assert sc.total_items(filled_cart) == 5

# Marking Exercise
@pytest.mark.skip(reason="Remove functionality not yet implemented")
def test_remove_item_from_cart(filled_cart):
    updated_cart = sc.remove_item(filled_cart, 'apple')
    assert sc.total_items(updated_cart) == 3


@pytest.mark.xfail(raises=ValueError)
def test_add_invalid_quantity(empty_cart, price_map):
    sc.add_item(empty_cart, 'pear', 0, price_map)
    

@pytest.mark.parametrize(
    "item, quantity, expected",
    [
        ('apple', 1, 1),
        ('banana', 2, 2),
        ('cherry', 3, 3)
    ]
)
def test_add_multiple_items(empty_cart, item, quantity, expected, price_map):
    sc.add_item(empty_cart, item, quantity, price_map)
    assert sc.total_items(empty_cart) == expected

# Mocking Exercise
def test_get_discounted_price(filled_cart, price_map):
    with patch("random.randint") as mock_randint, patch("src.shopping_cart.total_price") as mock_total_price:
        mock_randint.return_value = 7
        mock_total_price.return_value = (2*1 + 3*3)
	
        discounted_price = sc.get_discounted_price(filled_cart, price_map)
        assert discounted_price == round((2*1 + 3*3)*0.1, 2)
