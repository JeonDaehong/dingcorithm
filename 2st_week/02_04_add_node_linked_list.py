# ["시멘트"]
from encodings import normalize_encoding


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

    def add_node(self, index, value):
        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        prev_node = self.get_node(index-1)

        if prev_node is None:
            print("Index out of range")
            return

        next_node = prev_node.next
        prev_node.next = new_node
        new_node.next = next_node




# Add
linked_list = LinkedList(5) # Head 생성
linked_list.append(7)
linked_list.append(9)
linked_list.append(11)
linked_list.append(15)

linked_list.add_node(3, 21)

linked_list.get_all()