# Insertion of a node - **Front**

![[insertion_of_a_node_front_ll.excalidraw|500]]

---
# Time Complexity

- $O(1)$ - Constant Time Complexity

---
# Code

``` python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # insert at the front of the Linked List
    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)
        # insertion
        new_node.next = self.head
        self.head = new_node

    # print the linked List
    def print_list(self):
        temp = self.head
        while temp:
            print(str(temp.data) + " ", end=" ")
            temp = temp.next


llist = LinkedList()
llist.insert_at_beginning(12)
llist.insert_at_beginning(8)
llist.insert_at_beginning(9)
llist.insert_at_beginning(10)

llist.print_list()
```

---
