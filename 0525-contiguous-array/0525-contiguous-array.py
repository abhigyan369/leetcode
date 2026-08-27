class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        summ = 0
        maxi = 0
        mp = {0:-1} ## current sum starting me 0 hai jiska index -1 hai

        for i in range(n):
            if nums[i] == 0:
                nums[i] = -1
        ## ab question ban gya hai subarray sum == 0 -> find max subarray
        for i in range(n):
            summ += nums[i]
            if summ in mp:
                length = i - mp[summ]
                maxi = max(maxi, length)
            else:
                mp[summ] = i
        return maxi