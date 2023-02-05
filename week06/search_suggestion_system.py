class TrieNode:
    # TC: O(T + M * L), T = Total number of characters needed to build the Trie.
    # O(T) complexity for inserting a word. In the worst case,
    # on every word a node has to be created.

    # O(M * L), L = The biggest lenth of words.
    # M = Lenth of the search word.
    # In the worst case, for every character in
    # in the L, we have to run the dfs for M times.
    # Hence, here the time complexity is O(M * L)

    # SC: O(T), T = Number of nodes in the worst case 
    # to build the Trie. 
    def __init__(self):
        self.word = None
        self.child = defaultdict(TrieNode)

    def addWord(self,word):
        node = self
        for char in word:
            node = node.child[char]
        node.word = word
    
    def searchWord(self, limit) -> List[str]:
        searched_words = []

        def depthFirstSearch(node):
            if len(searched_words) == limit: return
            if node.word:
                searched_words.append(node.word)
            for char in ascii_lowercase:
                if char in node.child:
                    depthFirstSearch(node.child[char])

        depthFirstSearch(self)
        return searched_words

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        node = TrieNode()
        for product in products:
            node.addWord(product)
        
        searched_products = []
        current = node
        for char in searchWord:
            if current and char in current.child:
                current = current.child[char]
                searched_products.append(current.searchWord(3))
            else:
                current = None
                searched_products.append([])
        return searched_products
