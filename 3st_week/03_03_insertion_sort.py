input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i):
            if array[i-j-1] > array[i-j]:
                array[i-j-1], array[i-j] = array[i-j], array[i-j-1]
            else: # 자리를 바꾸지 않으면 이미 가장 큰 수이기 때문에, break ( O(N^2) 이지만, break 덕분에 Ω(N) 이기도 합니다. )
                break
    return array


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))