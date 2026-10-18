class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1
        maxi = 0

        while i <= j:
            ht = min(height[i], height[j])
            width = j - i
            area = ht * width
            maxi = max(maxi, area)

            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
    
        return maxi