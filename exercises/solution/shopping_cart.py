#Assertion Exercise --------------------------------------------------------
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


#Error Raising Exercise--------------------------------------------------------------
#Function 1: Built-in Exceptions
def add_to_cart2(item, quantity):
    if quantity < 0:
        raise ValueError(f"Cannot add a negative quantity: {quantity}")
    return f"{quantity} {item}(s) added to the cart!"


#Function 2: Custom Exceptions
class CartError(Exception):
    pass

def checkout(cart):
    if not cart:
        raise CartError("Cannot checkout an empty cart.")
    return f"Checked out {len(cart)} item(s)!"

#Fixtures Exercise --------------------------------------------------------
#Function 1: Get Total Number of Items
def total_items(cart):
    return len(cart)


# Function 2: Get Total Price of Items
def total_price(cart, price_map):
    total_price = 0
    for item in cart:
        total_price += price_map[item]
    return total_price

#Marking Exercise --------------------------------------------------------
#Function 1:
def reset_cart(cart):
    # Expected code
    # return []
    pass


#Function 2: Check if Item in Cart
def find_item(cart, item):
    return item in cart

#Mocking Exercise --------------------------------------------------------
import random

# Function 1
def get_discounted_price(cart, price_map):
	lucky_number = random.randint(1, 2000)
	if lucky_number == 7:
		discounted_price = total_price(cart, price_map) * 0.1
		return round(discounted_price, 2)