class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path= []
        res=[]
        visited = set()
        def backtracking():
            #Contiene lso nuemeros unicamente visitados en la           permutacion actual
            if len(path) == len(nums): #Consideramos completa
                res.append(path.copy())
                return
            else:
                #Recorremos todos los numeros
                for num in nums:#Branch
                    if num in visited:
                        pass
                    else:
                        path.append(num)
                        visited.add(num)
                        backtracking()
                        path.pop()
                        visited.remove(num)
        backtracking()
        return res

        