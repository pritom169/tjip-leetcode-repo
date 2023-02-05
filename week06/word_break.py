class Solution:
    # TC: O(N^3), N = Number of character in the S string
    # Nˆ2 for two nested operations on the same string.
    # Another, N opetion inside to slice the string. That
    # accumulates to the whole time complexity as O(Nˆ3)

    # SC: O(N), N = Number of character in the S string
    # In the worst case, every character in s will be a 
    # word in wordDict.
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        word_tracker = [False] * (len(s) + 1)
        word_tracker[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if word_tracker[j] and s[j:i] in word_set:
                    word_tracker[i] = True
                    break
        return word_tracker[len(s)]
