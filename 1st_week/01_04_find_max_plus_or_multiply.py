def find_max_plus_or_multiply(array):

    # 내가 작성한 풀이
    # 10분 정도 소요됨.

    # 0 + 3
        # 3 + 5
        # 3 x 5
    # 0 x 3
        # 0 + 5
        # 0 x 5

    # sum = 0
    # for num in array:
    #     if num <= 1:
    #         sum += num
    #     else:
    #         if sum + num >= sum * num:
    #             sum += num
    #         else:
    #             sum *= num
    # return sum

    # 실제 답안
    sum = 0
    for num in array:
        if num <= 1 or sum <= 1:
            sum += num
        else:
            sum *= num
    return sum

result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))