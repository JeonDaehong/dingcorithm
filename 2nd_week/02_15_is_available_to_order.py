shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

# 25.08.02 10:30 ~ 10:43
def is_available_to_order(menus, orders):

    # 반드시 Sorting 해주어야 함.
    menus.sort()
    orders.sort()

    return_boolean = True
    for order in orders:

        min_idx = 0
        max_idx = len(shop_menus) - 1
        cur_idx = (max_idx + min_idx) // 2
        while min_idx <= max_idx:
            if shop_menus[cur_idx] == order:
                break
            elif shop_menus[cur_idx] < order:
                min_idx += 1
            else:
                max_idx -= 1
            cur_idx = (max_idx + min_idx) // 2
        else:
            return_boolean = False

        if not return_boolean:
            break

    return return_boolean


result = is_available_to_order(shop_menus, shop_orders)
print(result)