class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = ["0", "1"]
        if n == 1: return res
        for i in range(2,n+1):
            temp = []
            for j in range(len(res)):
                if res[j][-1] == '1':
                    temp.append(res[j] + "1")
                    temp.append(res[j] + "0")
                else:
                    temp.append(res[j] + "1")
            res = temp
        return res