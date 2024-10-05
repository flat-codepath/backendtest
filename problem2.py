# importing the data from the database.py file
from database import *

# order_items = ["tofu_log", "burgr"]
# or
order_items =[order1, order2]=input('order the items by space in between each item').split()



def find_min_price(order_items):
    # convert string 'inf' to infinite
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



    if found:
        return (hotel_with_min_prices, price)
    else:
        return None


result = find_min_price(order_items)
if result is not None:
   for item in result:
       print(f'{item} ,',end='')
else:
    print('No matching restaurant found')



