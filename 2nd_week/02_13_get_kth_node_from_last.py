# Q. 링크드 리스트의 끝에서 K번째 값을 반환하시오.
# 25.07.30 21:02 ~ 21:08
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

    def list_size(self):
        cur = self.head
        count = 1
        while cur.next is not None:
            cur = cur.next
            count += 1
        return count

    def get_kth_node_from_last(self, k):
        list_size = self.list_size()
        cur = self.head
        for i in range(list_size - k):
            cur = cur.next
        return cur


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!