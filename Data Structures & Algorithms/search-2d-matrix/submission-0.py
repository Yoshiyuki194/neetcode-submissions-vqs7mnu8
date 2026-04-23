class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, h = 0, m * n - 1

        while l <= h:
            mid = (l + h) // 2

            r = mid // n
            c = mid % n

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                l = mid + 1
            else:
                h = mid - 1
        
        return False