class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        ans = float('inf')
        curr_window = 0
        # first window
        for i in range(k):
            if blocks[i] == 'W':
                curr_window += 1
        ans = curr_window

        # slide the window
        for j in range(k,n):
            if blocks[j] == 'W':
                curr_window += 1
            if blocks[j-k] == 'W':
                curr_window -= 1
            ans = min(ans,curr_window)
        return ans
            