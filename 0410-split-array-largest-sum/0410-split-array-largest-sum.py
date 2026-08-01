class Solution:
    def isValid(self,arr,n,k,mid)->bool:
        cnt = 1
        summ = 0
        for i in range(len(arr)):
            summ += arr[i]
            if summ > mid:
                cnt += 1
                summ = arr[i]
            if cnt > k:
                return False
        return True
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if len(nums) < k: return -1
        start = max(nums)
        end = sum(nums)
        res = -1
        while start <= end:
            mid = start + (end - start)//2
            if self.isValid(nums,n,k,mid) == True:
                res = mid
                end = mid - 1
            else:
                start = mid + 1
        return res