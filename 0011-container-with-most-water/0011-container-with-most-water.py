class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n - 1
        maxi = 0
        while i <= j:
            ht = min(height[i],height[j])
            wd = j - i
            area = ht * wd
            maxi = max(maxi,area)
            if height[j] > height[i]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:
                j -= 1
        return maxi


# we will use two pointer greedy approach for this problem
# we will not move the pointer with maximum height between i and j
# and move that pointer which is minimum out of i and j elements
# and calculate the area to find the maximum area
