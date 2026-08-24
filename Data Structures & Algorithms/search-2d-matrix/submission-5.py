class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l = 0
        r = len(matrix) * len(matrix[0]) - 1

        num_rows = len(matrix)
        num_cols = len(matrix[0])
        
        # i = 5: x = 1, y = 1
        while l <= r:

            # Get the Middle
            mid = (l + r) // 2

            # Covert mid to row and col
            row = mid // num_cols
            col = mid % num_cols

            val = matrix[row][col] 
            
            if (target == val):
                return True
            
            if target > val:
                l = mid + 1
            else:
                r = mid - 1
            
        
        return False




        