class Solution:
    # TC: O(N), N = number of items in the nums array
    # SC: O(1), we just declared three variable in 
    # order to do operationw which stays constant as
    # the input increases. Hence the space complexity
    # is O(1)
    def jump(self, nums: List[int]) -> int:
        jump_count, current_far, current_end = 0, 0, 0

        for i in range(len(nums) - 1):
            current_far = max(current_far, i + nums[i])

            if i == current_end:
                jump_count += 1
                current_end = current_far
        return jump_count
