class Solution:
    # TC: O(N * M), N = Number of rows, M = Number of columns
    # SC: O(1), because we are using constant space.
    def countBattleships(self, board: List[List[str]]) -> int:
        BATTLESHIP = 'X'
        count = 0
        for row in range(len(board)):
            for col in range(len(board[0])):
                # Step 1: If the element is not a notation of 
                # of a spaceship, we will not bother, will proceed
                # to the next cell.
                if board[row][col] != BATTLESHIP: continue
                # Step 2: Now we check the left one, if it's a battleship
                if row > 0 and board[row - 1][col] == BATTLESHIP: continue
                # Step 3: Now we check the upper one, if it's a battleship
                if col > 0 and board[row][col - 1] == BATTLESHIP: continue
                # If none of that happened, means we should increase the count
                count += 1
        return count
