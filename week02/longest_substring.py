class Solution:
    # TC: O(n + n) or O(n)
    # SC: O(min(m,n))
    def lengthOfLongestSubstring(self, s: str) -> int:

        length_of_string = len(s)
        ans = 0
        char_mapper = {}

        i = 0

        for j in range(length_of_string):
            if s[j] in char_mapper:
                i = max(char_mapper[s[j]], i)

            ans = max(ans, j - i + 1)
            char_mapper[s[j]] = j + 1
        return ans