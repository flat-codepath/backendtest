# importing the data from the database.py file
from database import *

order_items = ["tofu_log", "burger"]

def find_min_price(order_items):
    price = float('inf')
    hotel_with_min_prices = None
    found = False

    # checking for the allItems in a hotel
    for restaurant, menu in restaurant_data.items():
        if all(food in menu for food in order_items):
            total_price = sum(menu[food] for food in order_items)

            if total_price < price:
                price = total_price
                hotel_with_min_prices = restaurant
                found = True


    return (hotel_with_min_prices, price) if found else None


result = find_min_price(order_items)
