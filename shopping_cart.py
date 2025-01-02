def add_item(item, items):
    if len(items) == 5:
        raise OverflowError("Cannot add more items")
    items.append(item)

def total_num_of_items(items):
    return len(items)

def get_items(items):
    return items

def get_total_price(items, price_map):
    total_price = 0
    for item in items:
        total_price += price_map.get(item)
    return total_price