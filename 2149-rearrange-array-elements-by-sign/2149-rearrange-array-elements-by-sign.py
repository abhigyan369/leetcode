class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] *n
        posidx, negidx = 0,1
        for num in nums:
            if num > 0:
                res[posidx] = num
                posidx += 2
            else:
                res[negidx] = num
                negidx += 2
        return res