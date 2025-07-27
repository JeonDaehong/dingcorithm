# 25.07.27 10:02 ~ 10:07
def summarize_string(input_str):
    alphabet_map = dict()

    if len(input_str) == 0:
        return ""

    return_string = ""
    for char in input_str:
        if char.isalpha():
            alphabet_map.setdefault(char, 0)
            alphabet_map[char] += 1

    for char, count in alphabet_map.items():
        return_string += str(char) + str(count) + "/"

    return return_string[:-1]


input_str = "abcdefghijklmnopqrstuvwxyz"
print(summarize_string(input_str))