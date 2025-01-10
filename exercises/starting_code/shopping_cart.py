"""------------------------------------Assertion Exercise---------------------------------------"""

#Function 1: Add Item to Cart
def add_to_cart(cart, item):
    cart.append(item)
    return cart


#Function 2: Remove Item from Cart
def remove_from_cart(cart, item):
    if item in cart:
        cart.remove(item)
    return cart


#Function 3: Check for Empty Cart
def is_cart_empty(cart):
    return len(cart) == 0


#Function 4: Check if Item in Cart
def find_item(cart, item):
    return item in cart

"""------------------------------------Error Raising Exercise---------------------------------"""

#Built-in Exceptions

def add_to_cart2(item, quantity):
    """
    Function raises an error when a negative quantity is added to cart
    """
    if quantity < 0:
        raise ValueError(f"Cannot add a negative quantity: {quantity}")
    return f"{quantity} {item}(s) added to the cart!"

#Custom Exceptions
class CartError(Exception):
    pass

def checkout(cart):
    if not cart:
        raise CartError("Cannot checkout an empty cart.")
    return f"Checked out {len(cart)} item(s)!"
