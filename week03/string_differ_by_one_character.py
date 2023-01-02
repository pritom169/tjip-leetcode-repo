class Solution:
    # TC: O(N*M), N = Number of words, M = Lenth of words
    # SC: O(N*M), N = Number of words, M = Lenth of words
    def differByOne(self, dict: List[str]) -> bool:
        number_of_words = len(dict)
        lenth_of_words = len(dict[0])
        hash = [0] * number_of_words

        # The intuition behind it is that, we want to create
        # a unique hash for every word in the dictionary.
        for i in range(number_of_words):
            for j in range(lenth_of_words):
                hash[i] = (26 * hash[i]) + (ord(dict[i][j]) - ord('a'))
        
        # Since we have a hash value for every character, we
        # want to go by every character of every string in
        # reverse order. 

        # As the problem states, it has to differ by only one character.
        # So, after deducting the hash value of the current chracter from
        # the total hash, if two words has the same value, means they are just off
        # by one character

        # For example, if abc = 140, abd = 170. let say c has hash value of 40, and
        # d has 70. If we deducut the hash values of c and d from the respective characters
        # we have 100. Means both words are off by one character.
        base = 1
        for j in range(lenth_of_words - 1, -1, -1):
            seen = set()
            for i in range(number_of_words):
                new_hash = hash[i] - base * (ord(dict[i][j]) - ord('a'))
                if new_hash in seen:
                    return True
                seen.add(new_hash)
            base = 26 * base
        return False 
