class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        oddCnt = 0
        for num in arr:
            if num%2 != 0:
                oddCnt += 1
                if oddCnt == 3:
                    return True
            else:
                oddCnt = 0
        return False