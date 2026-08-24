class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set()
        s2 = set()
    
        for num in nums1:
            s.add(num)
        for num in nums2:
            if num in s:
                s2.add(num)
        return list(s2)