class Solution:
    def solve(self, arr, i, x, dp):
        if x == 0:
            return True

        if i >= len(arr):
            return False

        if dp[i][x] != -1:
            return dp[i][x]

        take = False
        if arr[i] <= x:
            take = self.solve(arr, i + 1, x - arr[i], dp)

        not_take = self.solve(arr, i + 1, x, dp)

        dp[i][x] = take or not_take
        return dp[i][x]

    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 2 != 0:
            return False

        x = s // 2
        n = len(nums)

        dp = [[-1] * (x + 1) for _ in range(n)]

        return self.solve(nums, 0, x, dp)