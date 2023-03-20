class Solution:
    # TC: O(N * 3 ^L), N = Number of cells in the board, L = Length of the word
    # When we talk about (3ˆL) complexity, we are talking about traversing the 
    # board in the 3 directions. One can raise objection about it goes to 4 direction.
    # but actully it block the previous way by putting # in the board. So we can say
    # if the structure is like a tree, every root will have 3 leafs to check.

    # In the worst case it will do the 3 way checking for all the N cells, which makes
    # the time complexity O(N * 3 ^L)

    # SC: O(L), L = Length of the word
    # In the worst case, if the word does exist, the lenth of the recusion stack will be
    # L.

    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLUMNS = len(board[0])

        def back_tracking(row: int, col:int, word: str):
            # If the length of the word is 0, it means the word has been found.
            # So it will return 0
            if len(word) == 0: return True

            # It the cell is out of the board or the word does not matches, it will
            # return False.
            if row < 0 or col < 0 or row == ROWS or col == COLUMNS or board[row][col] != word[0]:
                return False
            
            # Means the word is in the board. As we go forward we have to make sure
            # we do not check a single cell twice. For that reason, we will mark this
            # board as #.
            board[row][col] = '#'
            # Now we will iterate through via 4 direction and check.
            for (row_offset, col_offset) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                current_row = row + row_offset
                current_col = col + col_offset
                if back_tracking(current_row, current_col, word[1:]):
                    return True
            
            board[row][col] = word[0]
            return False
        
        # We will check through every item in the cell.
        for row in range(ROWS):
            for col in range(COLUMNS):
                if back_tracking(row, col, word):
                    return True
        # It has came to this point means it does not have any
        # matches.             
        return False

