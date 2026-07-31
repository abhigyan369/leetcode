class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        alice = []
        bob = []
        res = []
        for i in range(len(nums)):
            if i % 2 == 0:
                alice.append(nums[i])
            else:
                bob.append(nums[i])
        for i in range(len(nums)//2):
            res.append(bob[i])
            res.append(alice[i])
            
        return res
