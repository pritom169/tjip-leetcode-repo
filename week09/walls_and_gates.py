class Solution:
    # TC: O(MN + MN) -> O(MN), M = Number of rows, N = Number of columns
    # For appending the gates in the queue takes O(MN) time complexity.
    # In addition for checking on the 4 side from a gate cell will account
    # for O(MN) time complexity in the worst case

    # SC: O(MN) M = Number of rows, N = Number of columns
    # In the initial stage, in the worst case if all the cells
    # are gate cells, it will have O(MN) time complexity.
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        INF = 2147483647
        queue = deque([])
        for i in range(len(rooms)):
           for j in range(len(rooms[0])):
               if rooms[i][j] == 0:
                   queue.append([i, j])
        
        while queue:
            i, j = queue.popleft()
            for (row, col) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= row < len(rooms) and 0 <= col < len(rooms[0]) and rooms[row][col] == INF:
                    rooms[row][col] = rooms[i][j] + 1
                    queue.append([row, col])
