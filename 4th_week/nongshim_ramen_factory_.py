# 밀가루를 하루에 1톤
# 고장나서 k일 후에 공급이 가능해서, 해외에서 수입행 됨.
# 날짜, 수량을 알려주었고 최소한의 횟수로 밀가루를 공급 받아야 함.
import heapq

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):

    answer = 0
    last_add_idx = 0
    max_heap = []

    # stock <= k 계속 해줘야함
    while stock <= k:
        while last_add_idx < len(dates) and dates[last_add_idx] <= stock:
            heapq.heappush(max_heap, -supplies[last_add_idx])
            last_add_idx += 1
        heappop = heapq.heappop(max_heap)
        stock += -heappop
        answer += 1

    return answer


print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))