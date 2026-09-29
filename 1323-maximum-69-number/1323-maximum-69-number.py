class Solution:
    def maximum69Number(self, num: int) -> int:
        s = str(num)
        s1 = ""
        changed = False
        for char in s:
            if char == '6' and not changed:
                s1 += '9'
                changed = True
            else:
                s1 += char
        return int(s1)