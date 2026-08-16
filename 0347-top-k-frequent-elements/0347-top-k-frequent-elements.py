class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for num in nums:
            mp[num] = mp.get(num,0) + 1
        
        res = []
        #sorted_mp = {k:v for k,v in sorted(mp.items(), key=lambda x: x[1], reverse= True)}
        sorted_mp = sorted(mp, key=mp.get, reverse=True)

        for i in range(k):
            res.append(sorted_mp[i])
        return res