class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def majorityElement(self, nums: List[int]) -> int:
        majority_element = 0
        vote_count = 0

        for i in range(len(nums)):
            if (vote_count == 0):
                majority_element = nums[i]
                vote_count = 1
            elif (vote_count != 0) and (majority_element == nums[i]):
                vote_count += 1
            elif (vote_count != 0) and (majority_element != nums[i]):
                vote_count -= 1

        return majority_element
