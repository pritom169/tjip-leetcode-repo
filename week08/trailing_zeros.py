class Solution:
    # TC: O(logN), N = The Integer
    # Here the log has a 5 base

    # SC: O(1) because we are using constant space.

    def trailingZeroes(self, n: int) -> int:
        zero_count = 0
        while n > 0:
            n //= 5
            zero_count += n
        return zero_count
