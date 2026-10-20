class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def backtracking(fila,columna,k):
            
            if (fila<0 or fila>=len(board) or columna<0 or columna>=len(board[0])):
                return False

            if (fila,columna) in visited:
                return False

            if board[fila][columna] != word[k]:
                return False

            if k == len(word)-1:
                return True
            
            visited.add((fila,columna))
            encontrado =(
                backtracking(fila+1,columna,k+1) or
                backtracking(fila,columna+1,k+1) or
                backtracking(fila,columna-1,k+1) or
                backtracking(fila-1,columna,k+1)
            )
            visited.remove((fila,columna))
            return encontrado

        for fila in range(0,len(board)):
            for columna in range(0,len(board[0])):
                if backtracking(fila,columna,0):
                    return True
        return False