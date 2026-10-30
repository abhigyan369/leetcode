class Solution:
    def dfs(self,i,j,new_color,initial_color,visited,rows,cols):
        if i < 0 or i >= rows or j < 0 or j >= cols:
            return
        if visited[i][j] != initial_color:
            return
        if visited[i][j] == new_color:
            return
        visited[i][j] = new_color
        self.dfs(i+1,j,new_color,initial_color,visited,rows,cols)
        self.dfs(i-1,j,new_color,initial_color,visited,rows,cols)
        self.dfs(i,j-1,new_color,initial_color,visited,rows,cols)
        self.dfs(i,j+1,new_color,initial_color,visited,rows,cols)

    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        if color == image[sr][sc]:
            return image

        rows = len(image)
        cols = len(image[0])

        visited = deepcopy(image)
        initial_color = visited[sr][sc]

        self.dfs(sr,sc,color,initial_color,visited,rows,cols)
        return visited
