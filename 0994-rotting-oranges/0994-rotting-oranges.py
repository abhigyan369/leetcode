class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        gridcopy = deepcopy(grid)
        fresh_cnt = 0
        queue = deque()
        
        for r in range(rows):
            for c in range(cols):
                if gridcopy[r][c] == 2:
                    queue.append((r,c))
                elif gridcopy[r][c] == 1:
                    fresh_cnt += 1
        mins = 0
        while len(queue) != 0 and fresh_cnt > 0:
            mins += 1
            totalRotten = len(queue)
            for _ in range(totalRotten):
                i,j = queue.popleft()
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    new_i, new_j = i + dx, j + dy
                    # condition for boundary
                    if new_i < 0 or new_i == rows or new_j < 0 or new_j == cols:
                        continue
                    if gridcopy[new_i][new_j] == 2 or gridcopy[new_i][new_j] == 0:
                        continue
                    fresh_cnt -= 1
                    gridcopy[new_i][new_j] = 2
                    queue.append((new_i, new_j))

        if fresh_cnt > 0:
            return -1
        return mins
        