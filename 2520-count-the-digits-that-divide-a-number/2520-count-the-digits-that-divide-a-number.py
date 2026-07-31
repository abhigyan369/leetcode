class Solution:
    def countDigits(self, num: int) -> int:
        check = []
        cnt = 0
        temp = num
        # extracting all number
        while temp > 0:
            digit = temp % 10
            check.append(digit)
            temp = temp // 10
        for i in check:
            if num % i == 0:
                cnt += 1
        return cnt
