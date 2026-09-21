class Solution:
    def climbStairs(self, n: int) -> int:
        one,wo=1,1
        for i in range(n-1):
            emp=one
            one = one + wo
            wo = emp
        return one
    
    