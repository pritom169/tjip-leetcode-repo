class Solution:
    # TC: O(n + n) or O(n)

    # SC: O(26) or O(1) for all lowercase English characters.
    # For unicode characters, it will be O(k), where k is
    # the number of all unique unicode characters.

    def isAnagram(self, s: str, t: str) -> bool:
        # If two strings are not equal, it's obviously not an anagram.
        if len(s) != len(t):
            return False

        # We are keeping the count of every lowercase characters into the
        # hashmap
        s_char_counts = collections.Counter(s)

        # If the string t has the same charater more, or
        # has a new chracter which is not present in the string s,
        # the count will be 0 or less than zero.

        # For example: s = "rat", t = "car", c doesn't exist on s, so the count will
        # be -1. Hence, it is not a vaild anagram.

        for char in t:
            if s_char_counts[char] <= 0:
                return False

            s_char_counts[char] -= 1
        return True