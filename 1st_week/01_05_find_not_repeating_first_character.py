# 파이썬 3.7 부터는 dictionary 도 순차적 임을 보장함.
# 이런 문제는 list 형식 말고 dictionary 형식을 활용 하면 좋다.
def find_not_repeating_first_character(string):

    alphabet_dict = dict()
    lower_string = string.lower() # O(N)

    # O(N)
    for char in lower_string:
        if not char.isalpha():
            continue
        else:
            alphabet_dict[char] = alphabet_dict.get(char, 0) + 1

    # O(N)
    for char in lower_string:
        if alphabet_dict[char] == 1:
            return char

    return "_"

result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 = _ 현재 풀이 값 =", result("aaaaaaa"))