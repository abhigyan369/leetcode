class Solution:
    def trap(self, height: list[int]) -> int:
        leftmaxArr = []
        rightmaxArr = []
        ans = 0

        maxleft = float('-inf')
        for i in range(len(height)):
            maxleft = max(maxleft, height[i])
            leftmaxArr.append(maxleft)

        maxright = float('-inf')
        for i in range(len(height) - 1, -1, -1):
            maxright = max(maxright, height[i])
            rightmaxArr.append(maxright)
        rightmaxArr.sort(reverse=True)

        for i in range(len(height)):
            ans += min(rightmaxArr[i], leftmaxArr[i]) - height[i]
        return ans
        
