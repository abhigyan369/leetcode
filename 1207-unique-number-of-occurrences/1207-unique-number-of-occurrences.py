class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mp = {}
        for num in arr:
            mp[num] = mp.get(num,0) + 1
        s = set()

        for val in mp.values():
            if val in s:
                return False
            s.add(val)
        return True
        
    

## {1:3, 2:2, 3:1} - set = (3,2,1)
## {1:1, 2:1} - set = (1)