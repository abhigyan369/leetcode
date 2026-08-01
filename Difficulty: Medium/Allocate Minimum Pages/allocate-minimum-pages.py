class Solution:
    def isValid(self,arr,n,k,mx)->bool:
        student = 1
        summ = 0
        for i in range(len(arr)):
            summ += arr[i]
            if summ > mx:
                student += 1
                summ = arr[i]
            if student > k:
                return False
        return True
    def findPages(self, arr, k):
        
        # code here
        n = len(arr)
        if n < k: return -1
        start = max(arr)
        end = sum(arr)
        result = -1
        while start <= end:
            mid = start + (end-start)//2
            if self.isValid(arr,n,k,mid) == True:
                result = mid
                end = mid - 1
            else:
                start = mid + 1
        return result