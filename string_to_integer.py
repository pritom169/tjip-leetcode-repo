class Solution:
    # TC: O(n)
    # SC: O(1)
    def myAtoi(self, s: str) -> int:
        NUM_MAX = pow(2, 31) - 1
        NUM_MIN = -pow(2, 31)
        INPUT_LEN = len(s)
        IS_POSITIVE = True
        index = 0
        result = 0

        # Reducing the white spaces
        while (index < INPUT_LEN) and (s[index] == " "):
            index += 1

        # Checking the sign of digit.
        if (index < INPUT_LEN) and (s[index] == "+"):
            IS_POSITIVE = True
            index += 1
        elif (index < INPUT_LEN) and (s[index] == "-"):
            IS_POSITIVE = False
            index += 1

        # Checking the digit is number
        while (index < INPUT_LEN) and (s[index].isdigit()):
            digit = int(s[index])

            # Chcking the overflow of the number. If it is, then we clamp the
            # number to the nearest ceiling and returning it.
            if (result >= NUM_MAX // 10) and (digit > NUM_MAX % 10):
                return NUM_MAX if IS_POSITIVE else NUM_MIN

            result = 10 * result + digit
            index += 1

        return result if IS_POSITIVE else (-1 * result)