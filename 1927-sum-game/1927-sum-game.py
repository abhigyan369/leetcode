class Solution:
    def sumGame(self, num: str) -> bool:
        leftknownsum = 0
        rightknownsum = 0
        leftquesmark  = 0
        rightquesmark = 0
        n = len(num)

        for i in range(n):

            if num[i] == '?':
                if i < n//2:
                    leftquesmark += 1
                else:
                    rightquesmark += 1
            else:
                if i < n//2:
                    leftknownsum  += int(num[i])
                else:
                    rightknownsum  += int(num[i])

        totalquesmark = leftquesmark + rightquesmark
        if totalquesmark % 2 == 1:
            # odd - alice always wins
            return True

        left = 2*leftknownsum + 9*leftquesmark
        right = 2*rightknownsum + 9*rightquesmark
        if left == right: return False
        else:
            return True
