class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        
        for val in freq.values():
            if val >= 2:
                return True
        return False

## we are using hashmap- S.C = 0(n)
## T.C = 0(n)