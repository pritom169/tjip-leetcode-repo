class Solution:
    #TC: O(NlogN + N) -> O(NlogN), N = Number of points in the array
    #SC: O(2N) -> O(N), N = Number of points in the array 
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        angles_array, extra, answer = [], 0, 0
        x_position, y_position = location

        # Step 1: Find the slope between the given points and 
        # the reference points and sorting them.
        for (x,y) in points:
            if x == x_position and y == y_position:
                extra += 1
                continue
            angles_array.append(math.atan2(y - y_position, x - x_position))
        angles_array.sort()

        # Step 2: Add 2 * pie and add it to the array. The reason is if an slope
        # is negative it may be in same field of view, but because of the sorting
        # it was not included.
        angles_array = angles_array + [ (x + 2 * math.pi) for x in angles_array]
        angle = (math.pi / 180) * angle

        # Step 3: Now perform a sliding window operation to find the maximum amount
        # of points.
        left = 0
        for right in range(len(angles_array)):
            while (angles_array[right] - angles_array[left]) > angle:
                left += 1
            answer = max(answer, right - left + 1)
        return answer + extra
