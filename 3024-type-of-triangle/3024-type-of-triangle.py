class Solution:
    def triangleType(self, nums: List[int]) -> str:
        ## conditon to form a trainle
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        s = set()
        for num in nums:
            s.add(num)
        
        length = len(s)
        if length == 1:
            return "equilateral"
        elif length == 2:
            return "isosceles"
        else:
            return "scalene"




