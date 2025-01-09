import random

def add_item(cart, item, quantity, price_map):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")
    if item not in price_map:
        raise KeyError("Item does not exist, ask a staff")
    cart.append({'item': item, 'quantity': quantity})


def remove_item(cart, item):
    cart.remove(item)
    return cart


def total_items(cart):
    total_items = 0
    for item in cart:
        total_items += item["quantity"]
    return total_items


def is_empty(cart):
    return len(cart) == 0


def total_price(cart, price_map):
    total_price = 0
    for item in cart:
        total_price += price_map[item]*item["quantity"]
    return total_price


def get_discounted_price(cart, price_map):
	lucky_number = random.randint(1, 2000)
	if lucky_number == 7:
		discounted_price = total_price(cart, price_map) * 0.1
		return round(discounted_price, 2)