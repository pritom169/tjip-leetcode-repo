class Solution:
    # TC: O(M) + O(M * 4*3^(L-1)) -> O(M * 4*3^(L-1))
    # M = Total number of Alphabets in the board
    # L = Maximum lenth of the words

    # Here it is difficult to give the exact time complexity.
    # So I will provide the worst possible one.
    # When we are back tracking, in the first step we will look
    # into maximum of 4 direction. In the next step we will, go
    # search in all the 3 direction except the previous one. Hence,
    # it will be 4*3 for the first two step. But in the worst case,
    # if we find a matching word in each step of one of the 3 directions.
    # Hence, we have to do the 3 direction
    # computation for L-1 times. Which makes the time complexity 3^(L-1).
    # Likewise, the worst time complexity becomes O(M * 4.3^(L-1)).
    
    # P.S: The time complexity will be lesser than the mentioned becasue
    # every time we find a matching word we remove the letter from the trie.
    # It is impossible to predict the reduction for that time complexity. Hence,
    # it was not mentioned.

    # SC: O(M),  M = Total number of Alphabets in the board
    # In the worst case, we have to store every character on the board
    # to the map.
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        word_mapper = {}

        for word in words:
            current_node = word_mapper
            for char in word:
                current_node = current_node.setdefault(char, {})
            current_node[WORD_KEY] = word
        
        row_count = len(board)
        col_count = len(board[0])
        matched_words = []

        def backTracking(row, col, parent):
            current_letter = board[row][col]
            current_node = parent[current_letter]

            is_word = current_node.pop(WORD_KEY, False)
            if is_word:
                matched_words.append(is_word)
            
            board[row][col] = '#'
            for (row_offset, col_offset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                current_row, current_col = row + row_offset, col + col_offset
                if current_row < 0 or current_col < 0 or current_row >= row_count or current_col >= col_count:
                    continue
                if board[current_row][current_col] not in current_node:
                    continue
                backTracking(current_row, current_col, current_node)
            
            board[row][col] = current_letter
            if not current_node:
                parent.pop(current_letter)

        for row in range(row_count):
            for col in range(col_count):
                if board[row][col] in word_mapper:
                    backTracking(row, col, word_mapper)
        
        return matched_words
