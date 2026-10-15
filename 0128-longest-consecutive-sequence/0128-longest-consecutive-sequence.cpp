class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        set<int> st;
        int maxi = 0;
        for(int i=0; i<nums.size(); i++){
            st.insert(nums[i]);
        }
        for (int num : st){
            // check if starts of a sequence
            if(st.find(num-1) == st.end()){
                int length = 0;
                while (st.find(num+length) != st.end()){
                    length++;
                }
                maxi = max(maxi, length);
            }
        }
        return maxi;
    }
};