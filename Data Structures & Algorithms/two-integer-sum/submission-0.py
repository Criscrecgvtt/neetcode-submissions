class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        aux = {}

        for i, num in enumerate(nums):
            aux[num] = i

        for i, num in enumerate(nums):
            resta = target - num
            if resta in aux and aux[resta] != i:
                return [i, aux[resta]]



        