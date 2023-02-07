class Solution:
    # TC: O(NLogN + N) -> O(NlogN), N = Number of intervals
    # Sorting takes O(NlogN) time and going through every interval
    # takes another O(N) time. So the amortized time complexity is
    # O(NlogN)

    # SC: O(1), becasue are are using constant space.
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end_time = -float('inf')
        count = 0

        # Step 1: Sort the interval array with the ending time. 
        intervals.sort(key = lambda x:x[1])

        # Step 2: To check whether starting time is greater or equal
        # to the recent ending time. If it is, we update the ending
        # time again. If this is not the case, we have a overlapping
        # time. Hence, we increase the count.
        for (start, end) in intervals:
            if start >= end_time:
                end_time = end
            else:
                count += 1
        return count
