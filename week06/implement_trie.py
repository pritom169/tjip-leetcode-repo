class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # TC: O(M), M = Length of words
    # In the worst case, none of the character matches
    # with already existing character at any given 
    # node and we have to create a new node for every
    # char. So the time complexity is O(M)

    # SC: O(M), M = Length of word
    # Aagin, in the worst case none of the characters
    # existes in any given node. So the space complexity
    # is O(M)
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    # TC: O(M), M = lenth of word
    # In the worst case, the word exists. So we have
    # to go through each char and in the end return 
    # true. So the time complexity is O(M)

    # SC: O(1) becasue we are not using any extra memory.
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    # TC: O(M), M = lenth of prefix
    # Just explained before, if the prefix exists
    # each character will be visited. So, the time
    # complexity is O(M)

    # SC: O(1), because constant space has been used.
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
