class Solution:

    def countSpecialIntegers(self, nums: list[int]) -> int:

        result = {}
        count = 0

        for i, num in enumerate(nums):

            if num not in result:
                result[num] = []

            result[num].append(i)

        for num, idx in result.items():

            if len(idx) == 3:

                if idx[1] - idx[0] == idx[2] - idx[1]:
                    count += 1

        return count