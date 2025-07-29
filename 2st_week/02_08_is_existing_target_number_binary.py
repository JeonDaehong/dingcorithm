finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):

    count = 0
    min_idx = 0
    max_idx = len(array) - 1
    chk_idx = (min_idx + max_idx) // 2
    while min_idx <= max_idx:
        count += 1
        print(count)
        if array[chk_idx] == target:
            return True
        elif array[chk_idx] < target:
            min_idx = chk_idx+1
        else:
            max_idx = chk_idx-1
        chk_idx = (min_idx + max_idx) // 2

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)