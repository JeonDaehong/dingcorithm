def find_max_occurred_alphabet(string):

    max_num_alphabet = 'a'
    max_num = 0
    idx = 0
    for num in find_alphabet_occurrence_array(string):
        if max_num < num:
            max_num = num
            max_num_alphabet = chr(idx + 97)
        idx += 1

    return max_num_alphabet

# 문자 -> ASCII Code 로 변환
# print(ord('a')) # 97
# ASCII Code -> 문자
# print(chr(97)) # 'a'
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        alphabet_occurrence_array[ord(char) - 97] += 1

    return alphabet_occurrence_array

result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))