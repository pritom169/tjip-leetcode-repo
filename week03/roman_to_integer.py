class Solution:
    # TC: O(1) since a constant number of characters can be present in string s as
    # the highest number is 3999.
    # SC: O(1), because we do not store additional information as we go through the 
    # symbols.
    def romanToInt(self, s: str) -> int:
        symbol_dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        prev_number, number = 0, 0

        for char in reversed(s):
            # We just implement a hack solution by traversing from back.
            # If it is smaller number than the previous, we subtract.
            # If not, we just add the number.
            if symbol_dict[char] < prev_number:
                number -= symbol_dict[char]
            else:
                number += symbol_dict[char]

            prev_number = symbol_dict[char]
        
        return number
