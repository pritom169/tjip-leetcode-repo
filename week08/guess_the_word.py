# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    # TC: O(10N) -> O(N), N = Number of words in the list
    # SC: O(N), N = Number of words in the list
    def getMatches(self, word1: str, word2: str) -> int:
        count = 0
        for (char1, char2) in zip(word1, word2):
            if (char1 == char2):
                count += 1
        return count

    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        i = 0
        matches = 0
        # The intuition behind solving the problem is to narrow the guess
        # window. First we randomly choose a word and then check how many
        # characters matches with the secret word and we exactly store those
        # words in the array. So we have passed just one pass and continue
        # the work again.
        while i < 10 and matches != 6:
            index = random.randint(0, len(words) - 1)
            choosen_word = words[index]
            matches = master.guess(choosen_word)
            candidates = []
            for word in words:
                if matches == self.getMatches(word, choosen_word):
                    candidates.append(word)
            words = candidates
        return choosen_word
