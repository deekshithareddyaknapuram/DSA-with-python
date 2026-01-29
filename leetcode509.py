class Solution:
    def fib(self,n):
        memo={}
        return self.fib_memo(n,memo)
    def fib_memo(self,n:init,memo:dict)->int:
        if n in memo:
            return memo[n]
        return n
    return def.fib_memo(self,n:int,memo:dict)
