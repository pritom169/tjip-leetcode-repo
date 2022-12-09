class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def singleNumber(self, nums: List[int]) -> int:
        odd_number = 0

        for num in nums:
            odd_number ^= num
        
        return odd_number
