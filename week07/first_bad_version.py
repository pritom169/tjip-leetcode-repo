# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    # TC: O(NlogN), N = Size of the array.
    # Since we are reducing the array half every time,
    # the time complexity will be NLogN.

    # SC: O(1), because are not using any additional
    # space.
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n - 1

        while (left <= right):
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
