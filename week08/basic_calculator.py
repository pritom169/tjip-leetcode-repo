class Solution:
    # TC: O(N), N = Number of characters in the string.
    # SC: O(1) Because it requires a constant amount of time.
    def calculate(self, s: str) -> int:
        current_result, result, number = 0, 0, 0
        PLUS, MINUS, MULTIPLICATION, DIVISION = '+', '-', '*', '/'
        operator = PLUS

        # Iterating through every character in the string.
        # In the end, we add + in order to compute the
        # last character.
        for char in itertools.chain(s, '+'):
            # First we check it it a digit or not. If it is,
            # we add it to the number.
            if char.isdigit():
                number = number * 10 + int(char)
            
            # If it has any operators in the characters, we
            # do the operation.
            if char in (PLUS, MINUS, MULTIPLICATION, DIVISION):
                if operator == PLUS:
                    current_result += number
                elif operator == MINUS:
                    current_result -= number
                elif operator == MULTIPLICATION:
                    current_result *= number
                elif operator == DIVISION:
                    current_result = int(current_result / number)
                
                # If current character is PLUS, or MINUS, that means
                # we can store it in the result part and move forward.
                if char in (PLUS, MINUS):
                    result += current_result
                    current_result = 0
                
                # Since, it is a operator, we should assign number to
                # zero, because on the next character there will be a
                # new number.
                operator = char
                number = 0
        return result
