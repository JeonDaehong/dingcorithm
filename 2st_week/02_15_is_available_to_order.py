shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

# 25.07.30 21:16 ~
def is_available_to_order(menus, orders):
    menus.sort()
    orders.sort()



    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)