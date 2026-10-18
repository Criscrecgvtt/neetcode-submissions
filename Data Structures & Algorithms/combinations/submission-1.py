class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        res = []
        def backtracking(start):
            if len(path) == k: #si es completa 
                res.append(path.copy())
                return
            else:
                for num in range(start,n+1):#branches
                    path.append(num)
                    backtracking(num+1)
                    path.pop()
        
        backtracking(1)
        return res
        