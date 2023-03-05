class Solution:
    # TC: O(2NlogM + 2MlogN) -> O(NlogM + MlogN)
    # N = Number of rows, M = Number of columns
    # Searching for top and bottom takes 2NlogM time
    # Searching for left and right takes 2MlogN time

    # SC: O(1), because it is using constant space
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        def searchRows(top: int, bottom: int, condition: bool) -> int:
            while (top != bottom):
                mid = (top + bottom) // 2
                if ('1' in image[mid]) == condition:
                    bottom = mid
                else:
                    top = mid + 1
            return top
        
        def searchColumns(top: int, bottom: int, left: int, right: int, condition: bool) -> int:
            while (left != right):
                mid = (left + right) // 2
                if any('1' in image[row][mid] for row in range(top, bottom)) == condition:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        # Find the first row where at least one of the cell is one.
        top = searchRows(0, x, True)
        # Find the first row where all of the cells are 0.
        bottom = searchRows(x+1, len(image), False)
        # Find the first column where at least one of the cell is one.
        left = searchColumns(top, bottom, 0, y, True)
        # Find the first column where all of the cells are 0.
        right = searchColumns(top, bottom, y+1, len(image[0]), False)

        return (right - left) * (bottom - top)
