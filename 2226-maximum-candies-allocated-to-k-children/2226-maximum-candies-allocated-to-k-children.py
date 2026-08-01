class Solution:
    def canAllocate(self, candies, k, x):
        children = 0

        for pile in candies:
            children += pile // x

        return children >= k

    def maximumCandies(self, candies, k):
        if sum(candies) < k:
            return 0

        left = 1
        right = max(candies)
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2

            if self.canAllocate(candies, k, mid):
                ans = mid          # mid works, try larger
                left = mid + 1
            else:
                right = mid - 1    # mid too large

        return ans