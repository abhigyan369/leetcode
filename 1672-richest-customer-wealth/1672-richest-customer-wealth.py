class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = 0
        for i in range(len(accounts)):
            wealth = 0
            for j in range(len(accounts[0])):
                wealth += accounts[i][j]
                maxi = max(maxi,wealth)
        return maxi