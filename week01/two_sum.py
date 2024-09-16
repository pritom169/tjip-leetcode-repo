class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_map = {}

        for i in range(len(nums)):
            comp_num = target - nums[i]

            if comp_num in number_map:
                return [i, number_map[comp_num]]
            
            number_map[nums[i]] = i
