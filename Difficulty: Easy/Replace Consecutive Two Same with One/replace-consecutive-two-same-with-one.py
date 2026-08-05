class Solution:
    def removeDuplicates(self, s):
        # code here
        
        st = []
        for ch in s:
            if len(st) == 0:
                st.append(ch)
            elif len(st) != 0 and st[-1] == ch:
                st.pop()
                st.append(ch)
            else:
                st.append(ch)
        return "".join(st)
            