class Solution:
    # TC: O(NlogK), N = Number of distances
    # K = The difference between the lowest and the highest
    # range of speed.

    # Here it is not necessary to set a highest speed to an very massive
    # number because that will just increase the time of computation. One
    # tip we can use is, to devide the maximum hour with the decimal part
    # of the hour.

    # SC: O(1), because the space is not increasing as the input
    # increases. Hence, it is a constant space.
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def getRequiredTime(speed):
            time = sum([(math.ceil(distance/speed)) for distance in dist[:-1]])
            time += dist[-1]/speed
            return time
        
        result = -1
        decimal = hour % 1 or 1
        low, high = 1, math.ceil(max(dist)/decimal)

        while (low <= high):
            mid = low + (high - low)//2
            time = getRequiredTime(mid)
            if time == hour: return mid

            if time < hour:
                high = mid - 1
                result = mid
            else:
                low = mid + 1
        return result
