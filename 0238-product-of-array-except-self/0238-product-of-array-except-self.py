class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## we can use divsion method to solve 
        ## we will count the number of zeros and the total product of array without zero

        prod = 1
        cnt = 0
        answer = [0] * len(nums)
        for num in nums:
            if num == 0:
                cnt += 1
                continue
            prod = prod * num
        for i in range(len(nums)):
            if nums[i] != 0:
                if cnt > 0:
                    answer[i] = 0
                else:
                    answer[i] = prod // nums[i]
            elif nums[i] == 0:
                if cnt > 1:
                    answer[i] = 0
                else:
                    answer[i] = prod
        return answer