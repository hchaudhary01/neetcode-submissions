class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        l = 0
        r = (row*col)-1

        while l<=r:
            m = (l+(r-l)//2)

            m_row = m//col
            m_col = m%col

            if matrix[m_row][m_col] == target:
                return True
            elif target < matrix[m_row][m_col]:
                r = m-1
            else:
                l = m+1
        return False
        