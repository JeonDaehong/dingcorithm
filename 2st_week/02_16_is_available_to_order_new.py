# `in` 연산자는 어떤 자료형을 탐색하느냐에 따라 시간복잡도의 차이가 발생합니다.시간복잡도의 차이가 생기는 이유는 다음과 같습니다.
# list인 menus를 in 연산으로 순회하고 있습니다.
# 내부적으로 파이썬은 list에 대해서 in연산을 O(N)의 시간복잡도로 처리합니다
# menus를 set으로 바꿔서 in 연산을 진행합니다.
# 내부적으로 파이썬은 set에 대해서 in 연산은 O(1)의 시간복잡도로 처리합니다.

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

def is_available_to_order(menus, orders):

    set_menus = set(menus)

    for order in orders:
        if order not in set_menus:
            return False

    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)