# Q. 링크드 리스트의 끝에서 K번째 값을 반환하시오.
# 25.07.31 22:53 ~ 22:56
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    # 끝에서 K번째 값을 반환하는 대신
    # K-1 만큼 차이가 나는 두개의 포인터를 만들어서, 같이 증가시켜준다.
    # 그러다, 더 뒤에서 시작한 포인터가 끝에 도달하면,
    # 앞에서 시작한 포인터를 반환해주면 된다.
    def get_kth_node_from_last(self, k):
        slow_node = self.head
        fast_node = self.head
        for _ in range(k-1):
            fast_node = fast_node.next
        while fast_node.next is not None:
            slow_node = slow_node.next
            fast_node = fast_node.next
        return slow_node


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!