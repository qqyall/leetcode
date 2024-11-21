class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(len(board)):
            hashtableRows = {}
            hashtableColumns = {}
            for j in range(len(board[i])):
                if board[i][j].isdigit():
                    hashtableRows[board[i][j]] = hashtableRows.get(board[i][j], 0) + 1
                if board[j][i].isdigit():
                        hashtableColumns[board[j][i]] = hashtableColumns.get(board[j][i], 0) + 1
                if hashtableRows.get(board[i][j]) == 2 or hashtableColumns.get(board[j][i]) == 2 :
                        return False
            
        for i in range(3):
            for j in range(3):
                rows = range(i * 3, (i + 1) * 3)
                columns = range(j * 3, (j + 1) * 3)
                hashtableSubBoxes = {}
                for r in rows:
                    for c in columns:
                        if board[r][c].isdigit():
                            hashtableSubBoxes[board[r][c]] = hashtableSubBoxes.get(board[r][c], 0) + 1
                        if hashtableSubBoxes.get(board[r][c]) == 2:
                            return False
        return True
    
        
board = [[".","4",".",".",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."],
         [".",".",".","1",".",".","7",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".","3",".",".",".","6","."],
         [".",".",".",".",".","6",".","9","."],
         [".",".",".",".","1",".",".",".","."],
         [".",".",".",".",".",".","2",".","."],
         [".",".",".","8",".",".",".",".","."]]
sol = Solution()
print(sol.isValidSudoku(board))

