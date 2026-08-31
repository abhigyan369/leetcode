class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards)
        s = set()
        ans = float('inf')
        left = 0 # shrink
        #right = 0 # expand

        for right in range(n):

            #SHRINK while condition is satisfied
            while cards[right] in s:
                ans = min(ans, right-left+1)
                s.remove(cards[left])
                left += 1
            # expand
            s.add(cards[right])
        
        return ans if ans != float('inf') else -1



        