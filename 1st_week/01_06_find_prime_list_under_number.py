input = 16

def find_prime_list_under_number(number):

    prime_list = [True] * (number+1)
    prime_list[0] = False
    prime_list[1] = False

    # 16을 예시로 들어 봅시다.
    # 0, 1 은 소수가 아니니 강제 False
    # 16 ** 0.5 이기 때문에 4. 2 ~ 4까지 반복
        # 제곱근까지만 반복문을 검사해도 되는 이유는?
        # 예를 들어 어떤 수가 2 × 8 = 16처럼 두 수의 곱으로 만들어질 수 있다면,
        # 작은 쪽(2)이 반드시 √16보다 작거나 같기 때문입니다.
        # 큰 수(8)는 나중에 나오는 거라서 이미 작은 수에서 검사한 것입니다.
        # 즉, 두 수를 곱해서 어떤 수가 만들어질 수 있는지 확인하려면
        # 작은 수만 보면 충분하다는 뜻입니다.
        # 그래서 제곱근까지만 검사해도 모든 합성수를 걸러낼 수 있습니다!
    # i == 2 일 때,
        # 2 = True 로 남음
        # 4, 6, 8, 10, 12, 14, 16 = False 가 됩.
    # i == 3 일 때,
        # 3 = True 로 남음
        # 9, 12, 15 = False 가 됨.
    # i == 4 일 때,
        # 4 = 이미 False 인 상태임. 그러므로 아래 2번째 for 문이 동작하지 않음.
    # 최종적으로 2, 3, 5, 7, 11, 13 이 True 로 소수임.
    for i in range(2, int(number**0.5)+1):
        if prime_list[i]:
            for j in range(i*i, number+1, i):
                prime_list[j] = False

    # True로 남아 있는 숫자는 소수니까, 그 인덱스만 뽑아서 리스트로 반환합니다
    return [i for i, prime in enumerate(prime_list) if prime]

result = find_prime_list_under_number(input)
print(result)