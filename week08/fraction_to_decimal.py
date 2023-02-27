class Solution:
    # TC: O(N + N) -> O(N), N = Here it is very debatable what will be the
    # N because no one can predict how big the number will be, but in the
    # question it is written that the maximum size will be 10^4. Hence,
    # in the worst case we the size of the remainder will be N

    # In addition, if the repeating numbers after the decimal can also be
    # N size. In order to replace it with parenthesis '()', the insertation
    # operation also has to work O(N) times. 

    # So, the total time complexity is O(N)

    # SC: O(N), N = Size of the remainder.
    # In the worst case we have to store all the remainder
    # in the hashmap which has the size N.


    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '' if (numerator * denominator) >= 0 else '-'
        result = [sign + str(n), '.']
        remainders = {}

        while remainder > 0 and remainder not in remainders:
            remainders[remainder] = len(result)
            n, remainder = divmod(remainder * 10, abs(denominator))
            result.append(str(n))
        
        if remainder in remainders:
            index = remainders[remainder]
            result.insert(index, '(')
            result.append(')')
        return ''.join(result).rstrip('.')
