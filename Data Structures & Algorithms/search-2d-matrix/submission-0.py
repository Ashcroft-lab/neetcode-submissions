class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, cols = len(matrix), len(matrix[0])

        ls, rs = 0, rows*cols - 1
        while ls <= rs:
            m = ls + (rs-ls) // 2
            row , col = m//cols, m%cols
            if target > matrix[row][col]:
                ls = m+ 1
            elif target < matrix[row][col]:
                rs = m-1
            else:
                return True
        return False