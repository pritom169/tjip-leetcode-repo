class Solution:
    # TC: O(S.Length + Σ(lengthOf(words[i]))
    # SC: O(LenthOf(words))
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        answer = 0
        word_bucket = [[] for _ in range(26)]

        # We are now assigning the iterrable object for every word
        # on the basis of the first word.

        # For example, if a word starts with 'a', it will be be appended
        # on the first index. If it starts with 'd' it will be on the fourth.
        for word in words:
            it = iter(word)
            word_bucket[ord(next(it)) - ord('a')].append(it)
        
        for char in s:
            # We are storing the heads for the char in old_bucket and emptying
            # the index for next iteration.
            letter_index = ord(char) - ord('a')
            old_bucket = word_bucket[letter_index]
            word_bucket[letter_index] = []

            # The first character has been popped. Now we are checking if the
            # there is next character. If there is we are assigning to the proper
            # index. If not, that means the word is a matching subsequence.
            while old_bucket:
                it = old_bucket.pop()
                nxt = next(it, None)

                if nxt:
                    word_bucket[ord(nxt) - ord('a')].append(it)
                else:
                    answer += 1
        return answer
