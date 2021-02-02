class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if (index < 0 or index > self.length or not self.head):
            return -1

        if (index == 0):
            return self.head.val

        if (index == self.length):
            return self.tail.val

        node = self.head
        for i in range(index):
            node = node.next

        return node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if (not self.head):
            self.head = Node(val)
            self.tail = self.head
        else:
            new_head = Node(val)
            new_head.next = self.head
            self.head = new_head

        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if (self.length == 0):
            self.addAtHead(val)
        else:
            new_tail = Node(val)
            self.tail.next = new_tail
            self.tail = new_tail
            self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if (index < 0 or (index > self.length -1 and self.length > 0)):
            return None
        if (index == 0):
            self.addAtHead(val)
        elif (index == self.length):
            self.addAtTail(val)
        else:
            node = self.head
            prev = node
            for i in range(1, index):
                prev = node
                node = node.next

            new_node = Node(val)
            new_node.next = node.next
            prev.next = new_node
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if (index < 0 or index > self.length - 1):
            return None
        if (index == 0):
            self.head = self.head.next
            self.length -= 1                    
        else:
            node = self.head
            prev = node
            for i in range(1, index+1):
                prev = node
                node = node.next

            prev.next = node.next
            self.length -= 1
            if (self.length == index):
                self.tail = prev
