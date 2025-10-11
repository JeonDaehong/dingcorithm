# Q. 음이 아닌 정수들로 이루어진 배열이 있다. 이 수를 적절히 더하거나 빼서 특정한 숫자를 만들려고 한다.
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들기 위해서는 다음 다섯 방법을 쓸 수 있다.
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target_number이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 반환하시오.
numbers = [1, 1, 1, 1, 1]
target_number = 3

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):

    # 경우의 수는 2^array-1 임.
    # 재귀함수를 통해서 모든 경우의 수의 합을 가지고 와야 함.
    # target 값이 나오면, 1 을 아니면 0을 리턴해서 합을 구해야 함.

    len_array = len(array)
    rtn_array = []

    def execute(cur_sum, cur_idx):

        # 더 할 거 없으면 리턴
        # 매개 변수로 들어온 어레이 길이랑 전체 어레이 길이를 비교
        if cur_idx == len_array:
            if cur_sum == target:
                rtn_array.append(1)
                return
            else:
                return

        # 있으면, + 하나 1 하나씩 재귀
        execute(cur_sum + array[cur_idx], cur_idx + 1)
        execute(cur_sum - array[cur_idx], cur_idx + 1)

    execute(0, 0)

    return len(rtn_array)


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!