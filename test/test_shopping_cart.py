import pytest
import src.shopping_cart as sc
from unittest.mock import patch

# Fixtures
@pytest.fixture
def empty_cart():
    return []

@pytest.fixture
def filled_cart():
    return [{'item': 'apple', 'quantity': 2}, {'item': 'banana', 'quantity': 3}]

@pytest.fixture
def price_map():
    return {'apple': 1, 'orange': 2, 'banana': 3, 'cherry': 4}

# Tests
@pytest.mark.smoke
def test_empty_cart_is_empty(empty_cart):
    assert sc.is_empty(empty_cart)

@pytest.mark.regression
def test_add_item_to_cart(empty_cart, price_map):
    sc.add_item(empty_cart, 'orange', 1, price_map)
    assert not sc.is_empty(empty_cart)

@pytest.mark.slows
def test_total_items_in_cart(filled_cart):
    assert sc.total_items(filled_cart) == 5

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

@pytest.mark.skip(reason="Remove functionality not yet implemented")
def test_remove_item_from_cart(filled_cart):
    updated_cart = sc.remove_item(filled_cart, 'apple')
    assert sc.total_items(updated_cart) == 3

@pytest.mark.skipif(pytest.__version__ < '7.0', reason="Requires pytest 7.0 or later")
def test_skipif_example():
    assert True

@pytest.mark.xfail(raises=ValueError)
def test_add_invalid_quantity(empty_cart, price_map):
    sc.add_item(empty_cart, 'pear', 0, price_map)

@pytest.mark.usefixtures("filled_cart")
def test_cart_not_empty(filled_cart):
    assert not sc.is_empty(filled_cart)
    

def test_get_discounted_price(filled_cart, price_map):
    with patch("random.randint") as mock_randint, patch("src.shopping_cart.total_price") as mock_total_price:
        mock_randint.return_value = 7
        mock_total_price.return_value = (2*1 + 3*3)
	
        discounted_price = sc.get_discounted_price(filled_cart, price_map)
        assert discounted_price == round((2*1 + 3*3)*0.1, 2)
