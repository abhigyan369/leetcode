class Solution:
    def countDistinct(self, arr):
        # code here
        mp = {}
        for num in arr:
            mp[num] = mp.get(num,0) + 1
        
        count = 0  
        for key in mp.keys():
            count += 1
        return count