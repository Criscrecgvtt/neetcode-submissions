class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path =[]
        candidates.sort()

        def backtracking(start,target):
            if target ==0:
                res.append(path.copy())
                return
            
            for i in range(start,len(candidates)):
                #Si añadir este numero hace que el target sea menor que 0 no lo añadimos y pasamos al siguiente
                if i>start and (candidates[i] == candidates[i-1]):
                    continue
                if target-candidates[i]<0:
                    continue
                #Si si que lo podemos añadir
                else:
                    path.append(candidates[i])
                    backtracking(i+1,target-candidates[i])
                    path.pop()#deshacemos

        backtracking(0,target)
        return res