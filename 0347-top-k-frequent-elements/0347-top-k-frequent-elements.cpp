class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        typedef pair<int,int> P;
        unordered_map<int,int> mp;

        for(int i=0; i<nums.size(); i++){
            mp[nums[i]]++;
        }
        // min-heap
        priority_queue<P, vector<P>, greater<P>> pq;

        for (auto &it : mp){
            int val = it.first;
            int freq = it.second;

            pq.push({freq,val});

            if (pq.size() >k){
                pq.pop();
            }
        }
        vector<int> ans;
        while (!pq.empty()){
            ans.push_back(pq.top().second);
            pq.pop();
        }
        return ans;

    }
};