class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0]*n
        if k == 0:
            return res

        if k > 0:
            left,right = 1,k
        else:
            left, right = n-abs(k), n-1
        
        window_sum = 0
        for i in range(left,right+1):
            window_sum += code[i%n]
        # slide
        for i in range(n):
            res[i] = window_sum
            window_sum -= code[left%n]
            window_sum += code[(right+1)%n]
            left += 1
            right += 1
        return res