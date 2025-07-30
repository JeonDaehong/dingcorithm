finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):

    array_len = len(array)
    min_idx = 0
    max_idx = array_len - 1
    now_idx = (min_idx + max_idx) // 2

    while min_idx <= max_idx:
        if now_idx == target:
            return True
        elif now_idx > target:
            max_idx = now_idx - 1
        else:
            min_idx = now_idx + 1
        now_idx = (min_idx + max_idx) // 2

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)