class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        summ = 0
        remain1 = []
        remain2 = []

        for num in nums:
            summ += num
            if num % 3 == 1:
                remain1.append(num)
            elif num % 3 == 2:
                remain2.append(num)

        if summ % 3 == 0:
            return summ

        remain1.sort()
        remain2.sort()

        INF = float("inf")

        if summ % 3 == 1:
            remove1 = remain1[0] if len(remain1) >= 1 else INF
            remove2 = remain2[0] + remain2[1] if len(remain2) >= 2 else INF
        else:  # summ % 3 == 2
            remove1 = remain2[0] if len(remain2) >= 1 else INF
            remove2 = remain1[0] + remain1[1] if len(remain1) >= 2 else INF

        return summ - min(remove1, remove2)