class Solution:

    def maxSubarraySum(self, arr, k):
        # code here 
        i = 0
        j = 0
        n = len(arr)
        summ = 0
        maxi = 0
        while j < n:
            summ += arr[j]
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                maxi = max(maxi,summ)
                summ -= arr[i]
                j += 1
                i += 1
        return maxi
                
            
        
            
        