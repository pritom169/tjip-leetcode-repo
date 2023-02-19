class Solution:
    # TC: O(5^log(base10)N), N = size of the number
    # For every 5 number which are rotating in every 10 number,
    # we are doing log(base10)N iterations.

    # SC: O(log())
    def confusingNumberII(self, n: int) -> int:
        rotated_digits = [(0, 0), (1, 1), (6, 9), (8, 8), (9, 6)]
        self.result = 0

        def depthFirstSearch(number, rotated_number, multiplier):
            if number != rotated_number:
                self.result += 1
            
            for (con, con_rotated) in rotated_digits:
                if number == 0 and con == 0: continue
                if (number * 10 + con) > n: break
                depthFirstSearch(number * 10 + con, con_rotated * multiplier + rotated_number, multiplier * 10)
        depthFirstSearch(0, 0, 1)
        return self.result
