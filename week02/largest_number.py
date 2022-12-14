class Solution:
    #TC: O(nlogn) because we are utilizing the sort in python which has nlogn complexity
    #SC: O(n) because we are we are storing the copied version of nums.
    def largestNumber(nums: [int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        nums = sorted(nums, key = cmp_to_key(compare))
        return str(int("".join(nums)))