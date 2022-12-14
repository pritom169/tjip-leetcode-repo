from functools import cmp_to_key

class Solution:
    # TC: O(nlogn) because there is a built in sort we are using which has O(nlong) complexity.
    # SC: O(n) because we are storing the integer numbers into a string array.

    def largestNumber(self, nums: List[int]) -> str:
        #We are creating a string array with the same integers
        string_numbers = ['a'] * len(nums)
        for i, n in enumerate(nums):
            string_numbers[i] = str(nums[i])
        
        # A compare function compares the best possible combination for two integers.
        # For example: In array [30, 9], 930 will be greater than 309
        def compare(n1, n2):
            if n1 + n2 > n2+ n1:
                return -1
            else:
                return 1
        
        # Sorting the array according to the compare function
        string_numbers = sorted(string_numbers, key = cmp_to_key(compare))

        # We are appending all the elements from the sorted array and returning the number
        # in integer format.
        return str(int("".join(string_numbers)))
