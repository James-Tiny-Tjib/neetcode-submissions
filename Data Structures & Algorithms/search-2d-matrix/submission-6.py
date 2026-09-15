class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        len_R = len(matrix[0]) # 4
        len_C = len(matrix) # 3
        l = 0 
        r = len_R * len_C - 1

        while l <= r:

            mid = (l + r) // 2

            mid_x = mid % len_R
            mid_y = mid // len_R

            if matrix[mid_y][mid_x] == target:
                return True
            elif matrix[mid_y][mid_x] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False

