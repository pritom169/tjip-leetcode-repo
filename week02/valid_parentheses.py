class Solution:
    # TC: O(n)
    # SC: O(n)
    def isValid(self, s: str) -> bool:
        char_tracker_stack = []
        parentheses_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        # We need to go through every character in the string in order to find,
        # whether it's a valid parentheses or not.
        for char in s:
            # We are checking if the char is a closing parentheses or not. If
            # it's a closing parentheses, we pop the character from the stack.
            # If it's a opening parentheses, we push it to the stack.
            if char in parentheses_map:
                # Here we are assigning char which we will pop, to the variable
                # top_char. If the stack is empty we need to tackle that.

                # For example: if the given string is "]]](", where the first character
                # is ], but the stack is empty. So we assign a different character
                # to top_char.

                top_char = char_tracker_stack.pop() if char_tracker_stack else '#'

                # Now we are checking if the popped character is a opening parentheses
                # or not. If it's not a opening parentheses, we will return False.

                # For example: If input is "[{)]" and  current character is ")",
                # even though it is a closing character, it it not the desired closing
                # character.
                if parentheses_map[char] != top_char:
                    return False
            else:
                char_tracker_stack.append(char)

        return not char_tracker_stack