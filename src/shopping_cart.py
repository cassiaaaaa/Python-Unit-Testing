def add_item(cart, item, quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")
    cart.append({'item': item, 'quantity': quantity})


def remove_item(cart, item):
    return [i for i in cart if i['item'] != item]


def total_items(cart):
    return sum(i['quantity'] for i in cart)


def is_empty(cart):
    return len(cart) == 0