class Solution:
    # TC: O(logN), N = The integer
    # SC: O(1) because we are using constant space.
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        x0 = x
        x1 = (x0 + x/x0) / 2

        while (x0 - x1) >= 1:
            x0 = x1
            x1 = (x0 + x/x0) / 2
        return int(x1)
