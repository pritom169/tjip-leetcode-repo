class Solution:
    # TC: O(logN), N = The power
    # Since, the interval is decreasing at half speed hence
    # the complexity is O(logN)

    # SC: O(1) because we are using constant space.
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        answer = 1
        current_product = x

        while n > 0:
            if (n % 2) == 1:
                answer = answer * current_product
            current_product *= current_product
            n = n // 2
        return answer
