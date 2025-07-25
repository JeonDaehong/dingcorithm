input = "0111101110000110101010100000"


def find_count_to_turn_out_to_all_zero_or_all_one(string):

    cnt_list = [0, 1]
    now_num = -1
    for char in string:
        if now_num != char:
            cnt_list[int(now_num)] += 1
            now_num = char

    return cnt_list[0] if cnt_list[0] < cnt_list[1] else cnt_list[1]

result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)