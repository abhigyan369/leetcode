class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int n = grid.size(), m=grid[0].size();

        queue<pair<int, pair<int, int>>> q;
        int fresh = 0;
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(grid[i][j] == 1 || grid[i][j] == 2) fresh++;

                if(grid[i][j] == 2) q.push({0, {i, j}});
            }
        }

        int rotten = 0;
        int time = INT_MIN;
        while(!q.empty()){
            auto it = q.front();
            q.pop();
            int t = it.first;
            int r = it.second.first, c = it.second.second;
            rotten++;
            time = max(time, t);

            int delrow[4] = {-1, 0, 1, 0};
            int delcol[4] = {0, 1, 0, -1};
            for(int k=0; k<4; k++){
                int row = delrow[k] + r;
                int col = delcol[k] + c;

                if(row >= 0 && row < n && col >= 0 && col < m && grid[row][col] == 1){
                    q.push({t+1, {row, col}});
                    grid[row][col] = 2;

                }
            }
        }

        if(rotten < fresh) return -1;
        return time == INT_MIN ? 0 : time;
    }
};