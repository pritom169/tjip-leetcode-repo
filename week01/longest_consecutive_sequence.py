class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        number_set = set(nums)
        longest_streak = 1

        for number in nums:
            if number - 1 not in number_set:
                current_streak = 0

                while(number + current_streak) in number_set:
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak
