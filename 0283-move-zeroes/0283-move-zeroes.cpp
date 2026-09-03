class Solution {
public:
    void moveZeroes(vector<int>& arr) {
        int n = arr.size();
        // using two pointer
        int left = 0;
        for(int right=0; right<n; right++){
            if(arr[left] == 0 && arr[right] != 0){
                swap(arr[left], arr[right]);
                left += 1;
            }
            if(arr[left] != 0){
                left += 1;
            }
        }
    }
};