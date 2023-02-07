class Solution:
    # TC: O(N), N = Number of ratings
    # SC: O(1) because we are just using 3 variables
    # to do the operations.
    def candy(self, ratings: List[int]) -> int:
        up, candies = 1, 1
        down, peak = 0, 0

        for i in range(1, len(ratings)):
            # We are increasing the number of candies by one if
            # it has higer rating than the neighbour
            if ratings[i] > ratings[i - 1]:
                up += 1
                peak = up
                candies += up
                down = 0
            # If it has same rating we just give them just
            # one candy.
            elif ratings[i] == ratings[i - 1]:
                up = 1
                peak = 0
                candies += 1
                down = 0
            # If it has lowe rating we also increase the candy
            # count as the previous one will have one more cany.

            # One more thing we have to keep in mind that. If the downward
            # slope suprpasses the up slope that means, the child that was
            # that has the highest rating will need to have 1 more candy.
            else:
                up = 1
                down += 1
                candies += down
                if peak <= down: candies += 1
        return candies
