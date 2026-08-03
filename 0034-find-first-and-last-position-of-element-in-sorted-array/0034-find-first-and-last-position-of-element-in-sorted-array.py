class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst():
            lo, hi = 0, len(nums) - 1
            res = -1

            while lo <= hi:
                mid = lo + (hi - lo) // 2

                if nums[mid] == target:
                    res = mid
                    hi = mid - 1      # continue searching left
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1

            return res

        def findLast():
            lo, hi = 0, len(nums) - 1
            res = -1

            while lo <= hi:
                mid = lo + (hi - lo) // 2

                if nums[mid] == target:
                    res = mid
                    lo = mid + 1      # continue searching right
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1

            return res

        return [findFirst(), findLast()]