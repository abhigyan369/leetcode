class Solution:
    def longestSubarray(self, arr, k):  
        
        # code here
        mp = {0:-1}
        n = len(arr)
        summ = 0
        maxi = 0
        for i in range(n):
            summ += arr[i]
            rem = summ - k
            if rem in mp:
                length = i - mp[rem]
                maxi = max(maxi,length)
            if summ not in mp:
                mp[summ] = i
        return maxi
