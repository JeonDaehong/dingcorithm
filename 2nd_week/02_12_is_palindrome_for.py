input = "azbcbza"

def is_palindrome(string):
    # 첫 문자와, 마지막 문자를 비교하고 자른다.
    # 문장을 가지고 재귀를 돌린다
    # 남은 단어가 하나면 그냥 True 반환
    # 다른게 하나라도 있으면 False 반환
    print(string)
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])

print(is_palindrome(input))