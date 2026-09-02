class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        set<int> st;
        int n = nums.size();
        int left = 0;
        int maxi = 0;
        int sum = 0;
        for(int right=0; right<n; right++){

            while(st.count(nums[right])){
                st.erase(nums[left]);
                sum -= nums[left];
                left++;
            }

            st.insert(nums[right]);
            sum += nums[right];
            maxi = max(maxi, sum);
        }
        return maxi;
    }
};