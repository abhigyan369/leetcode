class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alice = 0
        bob = 0
        while len(piles) != 0:
            temp1 = max(piles)
            alice += temp1
            piles.remove(temp1)
            temp2 = max(piles)
            bob += temp2
            piles.remove(temp2)

        return alice > bob
