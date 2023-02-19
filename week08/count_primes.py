class Solution:
    # TC: O(sqrt(N) *log(logN)), N = The size of the Integer
    # First we are searching through sqrt(n) number in the 
    # outer loop which stands for O(sqrt(n)) complexity.

    # After that, we are going to reduce our search some sort
    # logarithmic fashion. Let's see how that works. 
    # In the first iteration we are going to reduce all the 
    # n/2 numbers, in the second n/3 and then on the third n/5.
    
    # This series goes like, (n/2 + n/3 + n/5 + ........ + n(The last
    # prime number in the series)).

    # This whole proces takes around log(logN) times.
    # Hence the total time complexity is O(n(log(logN))) times.

    # SC: O(N), N = Size of the Integer
    # Because the array which tracks the prime numbers has a size of N

    def countPrimes(self, n: int) -> int:
        if n < 2: return 0

        prime_tracker = [True] * n
        prime_tracker[0], prime_tracker[1] = False, False

        for number in range(2, int(sqrt(n)) + 1):
            if prime_tracker[number]:
                for multiplier in range(number * number, n, number):
                    prime_tracker[multiplier] = False
        
        return sum(prime_tracker)
