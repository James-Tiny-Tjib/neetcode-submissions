class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        row_list = [set() for _ in range (0,9)]
        col_list = [set() for _ in range (0,9)]
        square_list = [set() for _ in range (0,9)]


        for r in range (0,9):

            for c in range (0, 9):

                char = board[r][c]

                if (char in row_list[r] and char != "."):
                    return False
                else:
                    row_list[r].add(char)

                if (char in col_list[c] and char != "."):
                    return False
                else:
                    col_list[c].add(char)

                square_index = 3 * (r//3) + c//3

                if (char in square_list[square_index] and char != "."):
                    return False
                else:
                    square_list[square_index].add(char)
        
        return True

            
            
            

            

        
        