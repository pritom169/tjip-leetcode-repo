class Solution:
    # TC: O(N * 4ˆN), N = Number of digits
    # Here, if we consider the whole problem in a graph manner.
    # A possible number from the first digit will have maximum
    # 4 other possiblities(maximum) and so on. Which makes the total
    # time complexity as 4ˆN.
    # We have to do the operation N times which makes the total time
    # complexity as (N * 4ˆN).

    # SC: O(N + N), N = Number of digits
    # Two space complexities are responsbile here. O(N) for the
    # number of characters will be in the string and another O(N)
    # the recusion stack. 

    # The size of the return combination array has been avoided in
    # the space complexity. If the this size was included, another 4ˆN
    # space complexity needed to be added. 
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        letter_map = {
            '2' : ['a', 'b', 'c'], 
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }

        def back_tracking(index = 0, current_str = []):
            if len(current_str) == len(digits):
                combinations.append("".join(current_str))
                return
            for char in letter_map[digits[index]]:
                current_str.append(char)
                back_tracking(index + 1, current_str)
                current_str.pop()
        combinations = []
        back_tracking()
        return combinations
