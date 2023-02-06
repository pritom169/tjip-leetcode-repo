class Solution:
    # TC: O(log(m*n)), m = size of rows, n = size of columns
    # SC: O(1), we are not using any extra space. Hence, the
    # the space complexity is O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if (m == 0): return False
        n = len(matrix[0])

        left, right = 0, m * n - 1
        while left <= right:
            pivot = (left + right) // 2
            pivot_element = matrix[pivot // n][pivot % n]

            if pivot_element == target: return True

            if target < pivot_element:
                right = pivot - 1
            else:
                left = pivot + 1
        return False
