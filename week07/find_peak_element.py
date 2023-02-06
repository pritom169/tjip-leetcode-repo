class Solution:
    # TC: O(logN), N = Size of the array
    # SC: O(1), because constant space has been used.
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
