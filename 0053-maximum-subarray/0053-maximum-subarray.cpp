class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int curr = 0;
        int best = nums[0];
        int n = nums.size();
        for(int i=0; i<n; i++){
            curr = max(nums[i], curr+nums[i]);
            best = max(best,curr);
        }
        return best;
    }
};