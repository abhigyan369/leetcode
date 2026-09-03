class Solution {
public:
    void helper(int start, vector<int> &nums, vector<int>&curr, vector<vector<int>> &ans){
        ans.push_back(curr);
        for(int i=start; i<nums.size(); i++){
            // skip duplicates
            if(i > start && nums[i] == nums[i-1]){
                continue;
            }
            curr.push_back(nums[i]);
            helper(i+1, nums, curr, ans);
            curr.pop_back(); // backtrack
        }
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> curr;
        sort(nums.begin(), nums.end());
        helper(0,nums,curr,ans);
        return ans;
    }
};