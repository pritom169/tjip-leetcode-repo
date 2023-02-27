class RandomizedSet:
    def __init__(self):
        self.list = []
        self.dict = {}
    
    # TC: O(1), for insert(), remove() and getRandom()
    # SC: O(N + N) -> O(N), N = Number of items present in the hashmap
    # We need O(N) space for storing elements in dictionary.
    # We also need another O(N) space for storing the same elements
    # in the list. Hence, both of them accounts for O(N + N) space.
     
    def insert(self, val: int) -> bool:
        if val in self.dict: return False

        self.dict[val] = len(self.list)
        self.list.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.dict: return False

        last_element, index = self.list[-1], self.dict[val]
        self.list[index], self.dict[last_element] = last_element, index
        self.list.pop()
        del self.dict[val]
        return True
        
    def getRandom(self) -> int:
        return choice(self.list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
