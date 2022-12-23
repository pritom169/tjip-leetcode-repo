# TC: O(1) for both put and get function
# SC: 0(capacity) capacity = The maximum number of items in the hashmap
class DoubleLinkNode:
    def __init__(self) -> None:
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache:
    def _add_node(self, node):
        # When we add a node we have to add it next to the head node
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node):
        #Removing a node is just deleting the references
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node):
        # When we move an item to the front, we first delete the
        # node. Than we add the node to the front.
        self._remove_node(node)
        self._add_node(node)
    
    def _remove_tail(self):
        result = self.tail.prev
        self._remove_node(result)
        return result

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.count = 0
        self.head, self.tail = DoubleLinkNode(), DoubleLinkNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if not node:
            new_node = DoubleLinkNode()
            new_node.key = key
            new_node.value = value
            self.cache[key] = new_node
            self._add_node(new_node)
            self.count += 1

            if self.count > self.capacity:
                tail = self._remove_tail()
                del self.cache[tail.key]
                self.count -= 1
        else:
            node.value = value
            self._move_to_head(node)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
