class Solution:
    # TC: O(n)
    # SC: O(1)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # If the array is empty, we do not need to progress any further
        if len(strs) == 0: return ""

        # We will iterate through the first string
        for i in range(len(strs[0])):
            char = strs[0][i]

            # We will iterate through rest of the strings in the array
            for j in range(1, len(strs)):
                # If the index of the first string crosses the length or if the char does not match
                # the current character, we will just return every character before this character.
                if i == len(strs[j]) or char != strs[j][i]:
                    return strs[0][:i]

        return strs[0]