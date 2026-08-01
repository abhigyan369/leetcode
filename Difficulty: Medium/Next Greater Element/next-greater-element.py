class Solution:
    def nextLargerElement(self, arr):
        # code here
        n = len(arr)
        out = [-1] * n
        st = []
        
        for i in range(n-1,-1,-1):
            while len(st) != 0 and st[-1] <= arr[i]:
                st.pop()
            if len(st) != 0:
                out[i] = st[-1]
            st.append(arr[i])
        return out
        
  