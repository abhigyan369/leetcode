class Solution:
    def check(self, piles, mid, h):
        hr = 0
        for pile in piles:
            hr += math.ceil(pile / mid)
        return hr <= h


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans  = 0

        while low <= high:
            mid = low + (high-low) // 2
            if self.check(piles,mid,h):
                ans = mid
                high = mid -1
                
            else:
                low = mid + 1
        return ans