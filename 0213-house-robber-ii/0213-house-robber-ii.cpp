class Solution {
public:
    int t[101];
    int solve(vector<int>& nums, int index, int n){
        if (index > n){
            return 0;
        }
        if (t[index] != -1){
            return t[index];
        }
        int steal = nums[index] + solve(nums,index + 2,n);
        int skip = solve(nums, index+1, n);
        t[index] = max(steal,skip);
        return t[index];
    }
    
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 1){
            return nums[0];
        }
        memset(t,-1,sizeof(t));
        int ans1 = solve(nums, 0, n - 2);
        memset(t,-1,sizeof(t));
        int ans2 = solve(nums, 1, n - 1);
        return max(ans1,ans2);
    }
};