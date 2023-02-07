class Solution:
    # TC: O(NlogN + NlogN + N) -> O(NlogN), N = Number of intervals
    # First we are sorting the starting times and ending times which
    # will take total O(NlogN + NlogN) time.

    # Then we are going through the starting times again which will
    # have a linear time complexity.

    # SC: O(N + N) -> O(N), N = Number of intervals
    # Because we need two arrays to store the starting and ending times
    # sorted.
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        starting_times = sorted([i[0] for i in intervals])
        ending_times = sorted([i[1] for i in intervals])

        occupied_rooms = 0
        start_pointer = 0
        end_pointer = 0

        while start_pointer < len(intervals):
            if starting_times[start_pointer] >= ending_times[end_pointer]:
                occupied_rooms -= 1
                end_pointer += 1

            start_pointer += 1
            occupied_rooms += 1
        return occupied_rooms
        """
        if not intervals:
            return 0
        
        empty_rooms = []
        intervals.sort(key = lambda x:x[0])

        heapq.heappush(empty_rooms, intervals[0][1])
        for interval in intervals[1:]:
            if interval[0] >= empty_rooms[0]:
                heapq.heappop(empty_rooms)
            heapq.heappush(empty_rooms, interval[1])
        return len(empty_rooms)
