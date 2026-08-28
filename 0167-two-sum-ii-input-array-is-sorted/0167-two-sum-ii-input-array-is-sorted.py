class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = {}
        n = len(numbers)
        for i in range(n):
            rem = target - numbers[i]
            if rem in mp:
                return [mp[rem]+1,i+1]
            mp[numbers[i]] = i
        return [-1,-1]
