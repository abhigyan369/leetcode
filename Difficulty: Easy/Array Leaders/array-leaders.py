class Solution:
    def leaders(self, arr):
        # code here
        n = len(arr)
        mini = -1
        ans = []
        for i in range(n-1,-1,-1):
            if arr[i] >= mini:
                ans.append(arr[i])
                mini = arr[i]
        
        ans.sort(reverse=True)
        return ans
        
        


## [16, 17, 4, 3, 5, 2]
##  17    17    5    5    5 2- isko set me dal 