class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows first
        for i in range(9):
            unique_rows = set()
            unique_cols = set()
            unique_squares = set()
            for j in range(9):
                if board[i][j].isnumeric():
                    if board[i][j] in unique_rows:
                        return False
                    unique_rows.add(board[i][j])
                if board[j][i].isnumeric():
                    if board[j][i] in unique_cols:
                        return False
                    unique_cols.add(board[j][i])
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])        
        return True
