# Q.
# 다음과 같이 숫자로 이루어진 배열이 두 개가 있다.
# 하나는 상품의 가격을 담은 배열이고, 하나는 쿠폰을 담은 배열이다.
# 쿠폰의 할인율에 따라 상품의 가격을 할인 받을 수 있다.
# 이 때, 최대한 할인을 많이 받는다면 얼마를 내야 하는가?
# 단, 할인쿠폰은 한 제품에 한 번씩만 적용 가능하다.

# 25.10.07 : 0945 ~ 0955
shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

def get_max_discounted_price(prices, coupons):
    sorted_prices  = sorted(prices, reverse=True)
    sorted_coupons = sorted(coupons, reverse=True)

    total_discount = 0
    coupon_length = len(sorted_coupons)

    for i in range (0, len(sorted_prices)):
        price = sorted_prices[i]

        if coupon_length - 1 >= i:
            coupon = sorted_coupons[i]
            discount = price * ( 1 - coupon / 100 )
            total_discount += discount
        else:
            total_discount += price


    return int(total_discount)

print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))