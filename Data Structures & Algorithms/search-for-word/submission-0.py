class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ACTIONS = [(0, 1), (1, 0), (-1, 0), (0 , -1)]
        # find the first letter
        start = word[0]
        visited = []
        def dfs(x, y, i):
            for px, py in ACTIONS:
                if i == len(word):
                    return True
                if 0 <= x + px < len(board) and 0 <= y + py < len(board[0]) and (x + px, y + py) not in visited and board[x + px][y + py].upper() == word[i].upper():
                    visited.append((x + px, y + py))
                    if dfs(x + px, y + py, i + 1):
                        return True
                    visited.pop()
            return False



        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j].upper() == start.upper():
                    if dfs(i, j, 1):
                        return True
        return False