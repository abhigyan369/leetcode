class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ans;
        int cnt =0;
        int prod = 1;
        int prodWithoutzero = 1;

        for (int i=0; i<nums.size(); i++){
            if (nums[i] == 0){
                cnt++;
            }
            if (nums[i] != 0){
                prodWithoutzero *= nums[i];
            }else{
                prod *= nums[i];
            }
        }
        for(int i =0; i<nums.size(); i++){
            if(nums[i] != 0){
                if(cnt > 0){
                    ans.push_back(0);
                }else{
                    ans.push_back(prodWithoutzero/nums[i]);
                }
            }
            else{
                if(cnt > 1){
                    ans.push_back(0);
                }else{
                    ans.push_back(prodWithoutzero);
                }
            }
        }

        return ans;
    }
};