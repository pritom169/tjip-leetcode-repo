class Solution:
    # Time Complexity: O(nlogn + n^2) which can be wriiten as O(n^2)
    # Space Complexity: O(n), because sorting algorithms comes with O(n) complexity.
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i == 0 or nums[i - 1] != nums[i]:
                self.two_sum_second(nums, i, result)

        return result

    def two_sum_second(self, nums:List[int], i: int, result: List[List[int]]):
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = (nums[i] + nums[left] + nums[right])
            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1 
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while (left < right) and (nums[left] == nums[left-1]):
                    left += 1 
