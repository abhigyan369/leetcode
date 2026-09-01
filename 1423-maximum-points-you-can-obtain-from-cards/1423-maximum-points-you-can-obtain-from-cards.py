class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        i = 0
        maxi = 0
        n = len(cardPoints)
        left_sum = 0
        right_sum = 0
        ## first window
        for j in range(k):
            left_sum += cardPoints[j]
        maxi = left_sum
        # slide
        for j in range(k):
            left_sum -= cardPoints[k-1-j]
            right_sum += cardPoints[n-1-j]
            maxi = max(maxi, left_sum+right_sum)
        return maxi