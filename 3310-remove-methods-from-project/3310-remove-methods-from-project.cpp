class Solution {
public:
    vector<int> remainingMethods(int n, int k, vector<vector<int>>& invocations) {
        // graph ka adjacency list
        vector<vector<int>> adj(n); // {u -> (n1,n2)}
        vector<bool> suspicious(n,false);
        vector<int> indegree(n,0);

        for (auto &edge : invocations ){
            int u = edge[0];
            int v = edge[1];
            adj[u].push_back(v);
            indegree[v]++;
        }
        // BFS
        queue<int> que;
        que.push(k);
        suspicious[k] = true;

        while (!que.empty()){
            int cur = que.front();
            que.pop();

            for (int &ngbr: adj[cur]){
                indegree[ngbr]--;
                if(!suspicious[ngbr]){
                    que.push(ngbr);
                    suspicious[ngbr] = true;
                }
            }
        }
        vector<int> res;
        bool cannotRemove = false;
        for (int i=0; i<n; i++){
            if(suspicious[i] && indegree[i] >0){
                cannotRemove = true;
                break;

            }
            if (!suspicious[i]){
                res.push_back(i);
            }
        }
        if (cannotRemove){
            vector<int> vec(n);
            for(int i=0; i<n; i++){
                vec[i] = i;
            }
            return vec;
        }
        return res;

    }
};