def find_max_num(array):

    # 1. 값을 하나 하나 조회 하며 순회 하여 비교
    # 이중 for 문이기 때문에, O(n^2) 임.
    #    for number in array:
    #       is_max_num = True
    #        for compare_number in array:
    #            if number < compare_number:
    #                is_max_num = False
    #        if is_max_num:
    #            return number

    # 2. 하나의 변수를 잡아서 그 변수와 비교하며 가장 큰 수를 찾는 방법
    # O(n) 으로 빠름
    is_max_num = array[0]
    for number in array:
        if is_max_num < number:
            is_max_num = number
    return is_max_num

    # 3. 내장 함수 max 활용
    # 파이썬 내장 함수로, C로 구현된 O(n) 임.
    # return max(array)


print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3,5,6,1,2,4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6,6,6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6,9,2,7,1888]))