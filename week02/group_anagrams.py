class Solution:
    #TC: O(NK), n is the lenth of the input and K is the max lenth of a string
    #SC: O(NK)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dictionary = collections.defaultdict(list)

        for string in strs:
            char_count = [0] * 26

            for char in string:
                char_count[ord(char) - ord('a')] += 1
            result_dictionary[tuple(char_count)].append(string)

        return result_dictionary.values()