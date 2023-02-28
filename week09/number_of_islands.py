class Solution:
    # TC: O(N * M) , N = Number of rows, M = Number of columns
    # In this manner, we are checking evvery index, hence the
    # time complexity is O(N*M)

    # SC: O(N * M), N = Number of rows, M = Number of columns
    # In the worst case, every item on this matrix is filled with
    # land. Hence the stack will grow O(M*N) size.
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)
