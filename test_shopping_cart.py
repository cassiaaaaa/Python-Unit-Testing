from unittest.mock import Mock
from item_database import ItemDatabase
import src.calculator as sc
import pytest

@pytest.fixture
def cart():
    # All setup for the cart here...
    return []

def test_can_add_item_to_cart(cart):
    sc.add_item("apple", cart)
    assert sc.total_num_of_items(cart) == 1


def test_when_item_added_then_cart_contains_item(cart):
    sc.add_item("apple", cart)
    assert "apple" in sc.get_items(cart)


def test_when_add_more_than_max_items_should_fail(cart):
    for _ in range(5):
        sc.add_item("apple", cart)

    with pytest.raises(OverflowError):
        sc.add_item("apple", cart)


def test_can_get_total_price(cart):
    sc.add_item("apple", cart)
    sc.add_item("orange", cart)
    item_database = ItemDatabase()

    def mock_get_item(item: str):
        if item == "apple":
            return 1.0
        if item == "orange":
            return 2.0
        
    item_database.get = Mock(side_effect=mock_get_item)
    assert sc.get_total_price(cart, item_database) == 3.0
