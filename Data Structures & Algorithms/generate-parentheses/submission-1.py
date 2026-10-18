class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        open_count=0
        close_count=0
        res = []
        def backtracking(open_count,close_count):
            if len(path) == 2*n:#Is complete
                    #Creo que no hace falta la condicion pq no 
                    #permitimos en la creacion
                    res.append("".join(path))
                    return
            else:
                    #Si hay el msimo numero solo pdoemos seguir abriendo significandao que habiendolo hecho bien el resto estan cerradas

                if open_count < n:
                    path.append("(")
                    backtracking(open_count+1,close_count)
                    path.pop()

                if open_count> close_count:
                    path.append(")")
                    backtracking(open_count,close_count+1)
                    path.pop()
        
        backtracking(0,0)
        return res