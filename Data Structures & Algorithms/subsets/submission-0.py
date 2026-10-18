class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path=[]
        def backtracking(i):
            if i == len(nums):
                res.append(path.copy())
                return
            else:
                #No seleccionamos nums[i]
                backtracking(i+1)

                #Seleccionamos el elemento
                path.append(nums[i])
                backtracking(i+1)
                path.pop()

        backtracking(0)
        return res