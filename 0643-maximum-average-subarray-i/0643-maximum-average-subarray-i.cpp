class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int n = nums.size();
        double maxi = INT_MIN;
        int window_sum = 0;

        // first window
        for(int i=0; i<k; i++){
            window_sum += nums[i];
        }
        maxi = (double)window_sum/k;

        // slide
        for (int i=k; i<n; i++){
            window_sum -= nums[i-k];
            window_sum += nums[i];
            maxi = max(maxi, (double)window_sum/k);
        }
        return maxi;
    }
};