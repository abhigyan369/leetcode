class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int count = 1;
        int maxi = 1;
        int n = nums.size();
        sort(nums.begin(), nums.end());
        if (n == 0){
            return 0;
        }
        for (int i=1; i<n; i++){
            if(nums[i] == nums[i-1]){
                continue;
            }
            if(nums[i] == nums[i-1] + 1){
                count += 1;
                maxi = max(maxi, count);
            }else{
                count = 1;
            }
        }
        return maxi;
    }
};