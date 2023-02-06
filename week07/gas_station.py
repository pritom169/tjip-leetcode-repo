class Solution:
    # TC: O(N), N = Number of gas stations
    # Because we are iterating through every gas - cost situation
    # hence it has a linear time complexity.

    # SC: O(1). Just three variables have been used to do the operations.
    # Hence the space complexity is constant.

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas, current_gas, starting_station = 0, 0, 0

        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            current_gas += gas[i] - cost[i]

            # We are keeping track of the current_gas. If the current
            # difference is negative we just hope that the next one 
            # will have the positive difference. Actually it is the 
            # nature of some greedy problems.
            while current_gas < 0:
                starting_station = i + 1
                current_gas = 0
        return starting_station if total_gas >= 0 else -1
