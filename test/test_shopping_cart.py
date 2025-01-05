import pytest
import shopping_cart as sc

# Fixtures
@pytest.fixture
def empty_cart():
    return []

@pytest.fixture
def filled_cart():
    return [{'item': 'apple', 'quantity': 2}, {'item': 'banana', 'quantity': 3}]

# Tests
@pytest.mark.smoke
def test_empty_cart_is_empty(empty_cart):
    assert sc.is_empty(empty_cart)

@pytest.mark.regression
def test_add_item_to_cart(empty_cart):
    sc.add_item(empty_cart, 'orange', 1)
    assert not sc.is_empty(empty_cart)

@pytest.mark.slow
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
def test_add_multiple_items(empty_cart, item, quantity, expected):
    sc.add_item(empty_cart, item, quantity)
    assert sc.total_items(empty_cart) == expected

@pytest.mark.skip(reason="Remove functionality not yet implemented")
def test_remove_item_from_cart(filled_cart):
    updated_cart = sc.remove_item(filled_cart, 'apple')
    assert sc.total_items(updated_cart) == 3

@pytest.mark.skipif(pytest.__version__ < '7.0', reason="Requires pytest 7.0 or later")
def test_skipif_example():
    assert True

@pytest.mark.xfail(raises=ValueError)
def test_add_invalid_quantity(empty_cart):
    sc.add_item(empty_cart, 'pear', 0)

@pytest.mark.usefixtures("filled_cart")
def test_cart_not_empty(filled_cart):
    assert not sc.is_empty(filled_cart)
