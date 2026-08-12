class Solution:
    MOD = 10**9 + 7
    def findPow(self, x, n):
        if n == 0: return 1
        half = self.findPow(x, n//2) 
        result = (half * half) % self.MOD
        if n % 2 != 0: ## odd power, so we will multiply with extra x
            result = (x * result) % self.MOD
        return result

    def countGoodNumbers(self, n: int) -> int:
        
        ## the choices for even indices are -> 0,2,4,6,8 -> total = 5
        ## the choices for odd indices are -> prime no i.e -> 2,3,5,7 -> total = 4
        ## total even_indices are = (n+1) // 2
        ## total odd_indices are = n // 2


        a = self.findPow(5,(n+1)//2)
        b = self.findPow(4, n//2)
        return (a*b) % self.MOD