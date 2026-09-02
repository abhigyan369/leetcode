class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        summ = 0
        left = 0
        st = set()
        n = len(nums)
        maxi = 0
        for right in range(n):
            while nums[right] in st:
                st.remove(nums[left])
                summ -= nums[left]
                left += 1
            st.add(nums[right])
            summ += nums[right]
            maxi = max(maxi, summ)
        return maxi