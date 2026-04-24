'''here according to question we are just looking at the board exactly as it is 
right now. Are there any immediate rule breaks? Is there a "5" right next to 
another "5" in the same row? If no immediate rules are broken by the numbers 
currently on the board, it is "valid."'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set) # where key for row would be (r / 3) and for col would be (c / 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[r//3,c//3]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[r//3, c//3].add(board[r][c])
        return True
