class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        last_found_zero = 0

        for i in range(len(nums)):
            if (nums[i] != 0):
                nums[i], nums[last_found_zero] = nums[last_found_zero], nums[i]
                last_found_zero += 1
