class Bucket:
    # O(N/K): N is the number of all possible keys and K is the number of 
    # predifined buckets.

    # O(K + M): K = Number of predifined buckets and M is the number of
    # unique keys.
    def __init__(self) -> None:
        self.bucket_list = []
    
    def get(self, key) -> int:
        for (k,v) in self.bucket_list:
            if k == key:
                return v
        return -1
    
    def update(self, key, value):
        is_present = False
        for (i, kv) in enumerate(self.bucket_list):
            if key == kv[0]:
                self.bucket_list[i] = (key, value)
                is_present = True
                break
        if not is_present:
            self.bucket_list.append((key, value))
    
    def remove(self, key):
        for (i, kv) in enumerate(self.bucket_list):
            if key == kv[0]:
                del self.bucket_list[i]

class MyHashMap:
    def __init__(self):
        self.hash_prime = 2069
        self.hash_map = [Bucket() for i in range(self.hash_prime)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.hash_prime
        self.hash_map[hash_key].update(key, value)

    def get(self, key: int) -> int:
        hash_key = key % self.hash_prime
        return self.hash_map[hash_key].get(key)

    def remove(self, key: int) -> None:
        hash_key = key % self.hash_prime
        self.hash_map[hash_key].remove(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
