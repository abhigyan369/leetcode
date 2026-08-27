class Solution:
   
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
       ## modulo is the god
        mp = {0:1}
        summ = 0
        n = len(nums)
        result = 0
        for i in range(n):
            summ += nums[i]
            rem = summ % k
            if rem < 0: rem = rem + k
            if rem in mp:
                result += mp[rem]
            mp[rem] = mp.get(rem,0) + 1
        return result





## a b c d e f g h
## from a to e and a to c = the modulo is same for some number k- i.e same remainder
## toh d e is divisible by k
# a to e = s1 = k*n1 + rem
# a to c = s2 = k*n2 + rem
# d to e = s1 - s2 = k(n1-n2) -> hence divisible by k