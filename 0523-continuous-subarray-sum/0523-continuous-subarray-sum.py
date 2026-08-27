class Solution:
    
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        summ = 0
        mp = {0:-1}
        for i in range(n):
            summ += nums[i]
            rem = summ % k
            if rem in mp:
                if i - mp[rem] >= 2:
                    return True
            else:
                mp[rem] = i
        return False