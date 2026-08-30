class Solution {
public:
    int minimumDeletions(vector<int>& nums) {
        int maxi = INT_MIN;
        int maxIndex = 0;
        int mini = INT_MAX;
        int minIndex = 0;

        int n = nums.size();
        for(int i=0; i<n; i++){
            if(nums[i] > maxi){
                maxi = nums[i];
                maxIndex = i;
            }
            if (nums[i] < mini){
                mini = nums[i];
                minIndex = i;
            }
        }
        int leftIdx = min(maxIndex,minIndex);
        int rightIdx = max(maxIndex, minIndex);
        return min({(leftIdx+1)+(n-rightIdx),rightIdx+1, n-leftIdx});
    }
};