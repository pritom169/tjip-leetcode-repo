class Solution:
    #TC: O(nˆ2), n = Number of points
    #SC: O(n), n = Number of values stored in the hashmap in the worst case.
    def maxPoints(self, points: List[List[int]]) -> int:
        number_of_points = len(points)
        if number_of_points == 1:
            return 1
        
        # Two points or more can be considered on the same line if all
        # of them has the same tangent. So, we take a hashmap, where
        # we put tangent as the key, and increase the values according 
        # to the tangent. In the end, we return the maximum.
        result = 2
        for i in range(number_of_points):
            tan_count = collections.defaultdict(int)
            for j in range(number_of_points):
                if i != j:
                    tan_count[math.atan2(points[j][1] - points[i][1], points[j][0] - points[i][0])] += 1
            result = max(result, max(tan_count.values()) + 1)
        return result
