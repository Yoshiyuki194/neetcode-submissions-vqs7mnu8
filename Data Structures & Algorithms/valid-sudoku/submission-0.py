class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        diags = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                    
                if board[i][j] in rows[i] or board[i][j] in cols[j]:
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])

                if board[i][j] in diags[3 * (i // 3) + j // 3]:
                    return False
                diags[3 * (i // 3) + j // 3].add(board[i][j])
        return True
                