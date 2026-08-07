class Solution:
    def reverse(self,lst,left,right):
        while left <= right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1

    def reverseWords(self, s: str) -> str:
        arr = s.split()
        n = len(arr)
        self.reverse(arr,0,n-1)
        return " ".join(arr)
        
