class Solution:

    def maxSubarraySum(self, arr, k):
        # code here 
        
                
        maxi = float("-inf")
        window_sum = 0
        n = len(arr)
        
        for i in range(n):
            window_sum += arr[i]
            if i >= k-1: ## window complete 
                maxi = max(maxi, window_sum)
                window_sum = window_sum - arr[i-k+1]
        return maxi
                
                
        
        
            
        