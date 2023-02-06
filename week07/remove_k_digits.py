class Solution:
    # TC: O(N + N + N), -> O(N) N = Number of characters in the number string
    # O(N) time complexity for going through each character in the number
    # string.
    # Another O(N) complexity, in the worst case for slicing the number_stack
    # Finally, appending all the numbers in the number stack have to be
    # appended in the string, which will require another O(N) time complexity.

    # SC: O(N + N) -> O(N), N = Number of characters in the number string
    # In the worst case, we will store N characters in the number stack.
    # In additiona, another varialble final_stack will require another N space
    # in the worst case. Hence the space complexity is O(N + N) -> O(N)
    
    def removeKdigits(self, num: str, k: int) -> str:
        number_stack = []
        for number in num:
            while k and number_stack and number < number_stack[-1]:
                number_stack.pop()
                k -= 1
            number_stack.append(number)
        final_stack = number_stack[:-k] if k else number_stack
        return "".join(final_stack).lstrip('0') or "0"
