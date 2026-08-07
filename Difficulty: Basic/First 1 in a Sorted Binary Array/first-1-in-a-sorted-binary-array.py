class Solution:
    def firstIndex(self, arr):
        # code here
        left = 0
        right = len(arr) -1
        while left <= right:
            mid = left + (right-left)//2
            if arr[mid] != 1:
                left = mid + 1
            elif arr[mid] == 1:
                right = mid - 1
            
        if left == len(arr):
            return -1
        return left 
            
            
            
            
            
'''
 0, 0, 0, 0, 0, 0, 1, 1, 1, 1
 0. 1. 2. 3. 4  5  6. 7. 8. 9
 l           m.             r
                l     m     r
                l  r
                   m
 m != 1 return l = mid + 1
 yaha par nhi hai
 if m == 1 -> toh left side bhi 1 ho skta hai toh r = mid -1
 
 

'''

