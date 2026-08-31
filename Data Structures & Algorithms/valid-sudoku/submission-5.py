class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        square_set = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):

                char = board[r][c]

                if char != ".":
                    if char in row_set[r]:
                        return False
                    else:
                        row_set[r].add(char)

                    if char in col_set[c]:
                        return False
                    else:
                        col_set[c].add(char)
                        
                    if char in square_set[3 * (r//3) + (c//3)]:
                        return False
                    else:
                        square_set[3 * (r//3) + (c//3)].add(char)

        return True