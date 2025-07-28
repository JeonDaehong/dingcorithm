# ["시멘트"]
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked list
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)

    def get_all(self):
        current = self.head
        print(f"[{current.data}]", end=" - ")
        while current.next is not None:
            current = current.next
            if current.next is None:
                print(f"[{current.data}]")
            else :
                print(f"[{current.data}]", end=" - ")

    def get_node(self, index):
        current = self.head
        now_index = 0
        while now_index != index:
            current = current.next
            now_index += 1
        return current

# Add
linked_list = LinkedList(5) # Head 생성
linked_list.append(7)
linked_list.append(9)
linked_list.append(11)
linked_list.append(15)

# 특정 인덱스 조회
print(linked_list.get_node(0).data)
print(linked_list.get_node(1).data)
print(linked_list.get_node(2).data)
print(linked_list.get_node(3).data)
print(linked_list.get_node(4).data)