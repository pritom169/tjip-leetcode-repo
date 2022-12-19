class Solution:
    def decodeString(self, s: str) -> str:
        # TC: O(n) where n is the lenth of the character s
        # SC: O(m + n) where m is the number of letters and n
        # is the number of digit.
        char_stack = []
        current_string = ""
        k = 0
        for char in s:
            if char == "[":
                # When we encounter a closing bracket, we are sure that
                # we have just passed a digit which we need to multiply
                # the current digit with. Hence, we are storing it in the
                # stack.
                char_stack.append((current_string, k))
                current_string, k = "", 0
            elif char == "]":
                # It is closing bracket, hence we can be sure the charaters
                # that were inside, needs to be multiplied by the number k.
                # We can access the numbers and the multiplier via the stack.
                last_string, last_digit = char_stack.pop(-1)
                current_string = last_string + current_string * last_digit
            elif char.isdigit():
                # If it's a single digit k will be the digit, otherwise
                # we need to multiply the result by 10 and add the current digit.
                k = k * 10 + int(char)
            else:
                # If it came to this block, it means it a english letter, which
                # we can easily add to the current string.
                current_string += char
        return current_string


