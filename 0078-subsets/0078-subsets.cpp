class Solution {
public:
    void helper(int index, vector<int> &current, vector<int>& nums,vector<vector<int>>& result){
        if(index == nums.size()){
            result.push_back(current);
            return;
        }
        // choice 1, pick nums[index]
        current.push_back(nums[index]);
        helper(index+1, current, nums, result);

        // backtrack
        current.pop_back();

        // choice , not pick nums[index]
        helper(index+1, current, nums, result);

    }

    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;
        helper(0, current, nums,result);
        return result;
    }
};