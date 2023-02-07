class Solution:
    # TC: O(NlogN + N) -> O(NlogN), N = Number of sticks
    # For converting the sticks array to a priority queue
    # it will take O(NlogN) time.
    # Going through (N - 1) number of sticks will also take
    # O(N) complexity.

    # SC: O(N), N = Number of sticks
    # Because we have to store all the sticks in the priority
    # queue, we will need O(N) space complexity.

    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        total_cost = 0

        while len(sticks) > 1:
            stick_1 = heapq.heappop(sticks)
            stick_2 = heapq.heappop(sticks)

            total_cost += (stick_1 + stick_2)
            heapq.heappush(sticks, stick_1 + stick_2)
        return total_cost
