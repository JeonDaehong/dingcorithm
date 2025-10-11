# ["시멘트"]
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(3)
print("Node 란 : {}, {}".format(node.data, node.next))

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

# Add
linked_list = LinkedList(5) # Head 생성
linked_list.append(7)
linked_list.append(9)
linked_list.append(11)
linked_list.append(15)

# 조회
linked_list.get_all()