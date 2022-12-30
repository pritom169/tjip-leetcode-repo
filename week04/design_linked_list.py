# Solution 1 using Doubly linked list.
# TC: O(1) for addAtHead and for addAtTail.
# O(min(K, N -K)) for get, addAtIndex, deleteAtIndex
# k = The index to be navigated
# N = The current size of the linked List

# SC: O(1) for all operations because we are using constant space.
class DoubleLinkedNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head, self.tail = DoubleLinkedNode(0), DoubleLinkedNode(0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        # Returning -1 for invalid index
        if index < 0 or index >= self.size:
            return -1
        
        # If we want to get the value, we will
        # try to find the shortest path from head 
        # or tail. 
        if index + 1 < self.size - index:
            current = self.head
            for _ in range(index + 1):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.size - index):
                current = current.prev
        return current.value

    def addAtHead(self, val: int) -> None:
        pred, succ = self.head, self.head.next

        self.size += 1
        to_add = DoubleLinkedNode(val)
        to_add.next = succ
        to_add.prev = pred
        pred.next = to_add
        succ.prev = to_add
        
    def addAtTail(self, val: int) -> None:
        succ, pred = self.tail, self.tail.prev

        self.size += 1
        to_add = DoubleLinkedNode(val)
        to_add.next = succ
        to_add.prev = pred
        pred.next = to_add
        succ.prev = to_add
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        
        if index < 0: index = 0

        # Adding at an index, if we are going from head we will try
        # to set pred at the same index we trying to put the new item in. 
        # When going from tail, we will
        # do the same with successor.
        if index < self.size - index:
            pred = self.head

            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev
        
        self.size += 1
        to_add = DoubleLinkedNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def deleteAtIndex(self, index: int) -> None:        
        if index < 0 or index >= self.size:
            return
        
        # When we will delete an element, we have to be a bit careful,
        # We have to keep one index gap between the pred and succ. The index
        # in between will be the index, we want to delete.
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev
        
        self.size -= 1
        succ.prev = pred
        pred.next = succ

# Solution 2 for singly linked list 
# TC: O(1) for addAtHead, O(K) for get, addAtIndex, deleteAtIndex where
# k = The index to be navigated,
# O(N)for addAtTail = N is the size of the linked list.

# SC: O(1) for all operations because we are using constant space.

class SingleLinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.node_count = 0
        self.head = SingleLinkedNode(0)

    def get(self, index: int) -> int:
        # Returning -1 for invalid index
        if index < 0 or index >= self.node_count:
            return -1

        node = self.head
        # Navigating to the index where it said to be deleted
        for _ in range(index + 1):
            node = node.next
        return node.value

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.node_count, val)
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.node_count:
            return

        if index < 0:
            index = 0
        
        # Navigating to the predecessor of node which said to be deleted.
        previous = self.head
        for _ in range(index):
            previous = previous.next
        
        note_to_add = SingleLinkedNode(val)
        note_to_add.next = previous.next
        previous.next = note_to_add
        self.node_count += 1

    def deleteAtIndex(self, index: int) -> None:        
        # Navigating to the predecessor of node which said to be deleted.
        # if the index is invalid, do nothing
        if index < 0 or index >= self.node_count:
            return
        
        # find predecessor of the node to be deleted
        pred = self.head
        for _ in range(index):
            pred = pred.next
            
        # delete pred.next 
        pred.next = pred.next.next
        self.node_count -= 1
