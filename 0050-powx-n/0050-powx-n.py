class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1.0

        if n < 0:
            x = 1 / x
            n = -n

        half = self.myPow(x, n//2)
        result = half * half

        ## if the power is odd then we have add an extra x
        if n % 2 == 1:
            result = x * result
        return result




## binary exponentiation
## 3^ 18 = 3^9 * 3^9 // n == even
##.      = (3 * 3^4 * 3^4) * (3 * 3^4 * 3^4 ) // n == odd 
##       = (3 * 3^2 * 3^2 * 3^2 * 3^2) * (3 * 3^2 * 3^2 * 3^2 * 3^2) // n == even
##.      = (3 * 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3) *  (3 * 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3) // n == even
## base conditon - here x is not changing but the n is changing so when n == 0 -> 3^0 = 1