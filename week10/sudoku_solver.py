from collections import defaultdict
class Solution:
    # TC: O(9!)^9
    # Here the time complexity is fixed. The reason, on the first
    # cell there are 9 choices, and for the second we have 8 choices.
    # So that makes the time complexity for the first row 9!. So for
    # total 9 rows it become (9!)^9

    # SC: O(Nˆ2) Here the space complexity is Nˆ2. The recursion stack in the
    # worst case can go upto Nˆ2.
    def solveSudoku(self, board):
        # Declaring a function in order to check whether it
        # is possible to place the number in the board.
        def can_place(d, row, col):
            if d in rows[row]:
                return False
            elif d in columns[col]:
                return False
            elif d in sub_boxes[box_index(row, col)]:
                return False
            return True
        
        # In order to place the number on the board we need first
        # need to input that into the proper dictionaries
        def place_number(d, row, col):
            rows[row][d] += 1
            columns[col][d] += 1
            sub_boxes[box_index(row,col)][d] += 1
            board[row][col] = str(d)
        
        # When we make a mistake while putting a number, we also need
        # to make sure that, there is way to delete the numbers. Hence,
        # also while we are trying to delete, we will first remove the
        # key from the dictionaries and then remove the number from the board
        def delete_number(d, row, col):
            del rows[row][d]
            del columns[col][d]
            del sub_boxes[box_index(row,col)][d]
            board[row][col] = '.'
        
        def place_next_number(row, col):
            # If the backtracking function in on the last cell, we
            # have to mark as the iterations has been completed.
            if row == N - 1 and col == N - 1:
                nonlocal is_completed
                is_completed = True
            else:
                # Since, backtracking happens in the rowwise manner,
                # when we hit the last column in the row, we have to make
                # it continues for the next row.
                new_row = row + 1 if (col == N - 1) else row
                new_col = 0 if (col == N - 1) else col + 1
                back_tracking(new_row, new_col)
        
        def back_tracking(row = 0, col = 0):
            if board[row][col] == '.':
                for d in range(1,10):
                    if can_place(d, row, col):
                        place_number(d, row, col)
                        place_next_number(row, col)

                        # If the running comes to this point, it means
                        # all the numbers from 1 to 9 did not work for that 
                        # cell. In order to resolve this problem, we have to go
                        # back to the cell where it is started. Until that point
                        # occurs, we have to continue to delete the number.
                        if not is_completed: delete_number(d, row, col)
            else:
                place_next_number(row, col)
        
        n = 3
        N = n * n
        box_index = lambda row, col: (row // n) * n + (col // n)

        # Setting up the rows, columns and the sub boxes.
        rows = [defaultdict(int) for i in range (N)]
        columns = [defaultdict(int) for i in range (N)]
        sub_boxes = [defaultdict(int) for i in range (N)]

        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    place_number(d, i, j)

        is_completed = False
        back_tracking()
