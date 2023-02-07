class Solution:
    # TC: O(N + logN) -> O(N), N = Number of weights
    # In the first part, when we are calculating the
    # prfix sum, we have to go though every element of
    # the array. Hence, the time complexity is O(N)

    # In the second part, when we are searching through
    # the prefix sum array which take O(logN) time

    # SC: O(N) + O(1) -> O(N), N = Number of weights
    # In the first part we need another array of size N
    # to store all the prefix sums. That makee the space
    # complexity O(N).
    
    # In the second part, we using constant space.
    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        low, high = 0, len(self.prefix_sums) - 1
        while low <= high:
            mid = low + ((high - low) // 2)
            if target < self.prefix_sums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low
