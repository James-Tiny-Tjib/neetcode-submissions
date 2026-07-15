class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row_lists = [{} for _ in range(9)]
        col_lists = [{} for _ in range(9)]
        square_lists = [{} for _ in range(9)]

        for i in range(0, 9):
            for j in range(0, 9):

                val = board[i][j]
            
                if val != ".":


                    if row_lists[i].get(val,0) == 0:
                        row_lists[i][val] = 1
                    else:
                        return False
                    
                    if col_lists[j].get(val,0) == 0:
                        col_lists[j][val] = 1
                    else:
                        return False
                    
                    

                    if square_lists[3*(i//3) + (j//3)].get(val, 0) == 0:
                        square_lists[3*(i//3) + (j//3)][val] = 1
                    else:
                        return False
        
        return True


        