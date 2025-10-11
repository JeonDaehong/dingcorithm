finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, array):

    array = sorted(array)

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
            min_idx = chk_idx + 1
        else:
            max_idx = chk_idx - 1
        chk_idx = (min_idx + max_idx) // 2

    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)