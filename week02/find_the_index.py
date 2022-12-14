class Solution:
    # TC: O(n)
    # SC: O(1)
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        if len(haystack) == 0 or len(needle) == 0:
            return -1

        # If needle matches the exactly the last strings of haystack (in the worst case), for example
        # haystack = "happybutsad", needle = "sad", we just need to iterate upto "s"
        for i in range((len(haystack) + 1) - len(needle)):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i

        return -1
