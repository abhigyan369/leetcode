class Solution:
    def getSecondLargest(self, arr):
        # code here
        largest = -1
        sLarge = 0
        
        for i in range(len(arr)):
            if arr[i] > largest:
                slarge = largest
                largest = arr[i]
            elif arr[i] > slarge and arr[i] != largest:
                slarge = arr[i]
        return slarge