class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        end = arr[-1] + k
        check = [0] * (end + 1)

        for num in arr:
            check[num] = 1

        for i in range(1, end + 1):
            if check[i] == 0:
                k -= 1
                if k == 0:
                    return i