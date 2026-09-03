class Solution {
  public:
    bool backtrack(int index, int target, const vector<int>& arr){
        // success kab hoga
        if (target == 0) return true;
        // failure conditon
        if (index == arr.size() || target < 0) return false;
        // pick 
        if (arr[index] <= target){
            if (backtrack(index+1, target-arr[index], arr)){
                return true;
            }
        }
        // don't pick
        return backtrack(index+1, target, arr);
    }
    bool checkSubsequenceSum(vector<int>& arr, int k) {
        // Code here
        // pattern - pick karna ya not pick karna hai
        // agar tumne pick kiya toh subtract from target k - arr[i]
        // don't pick - remaining target unchanged k
        // target reaches 0- valid subsequence exist krta hai
        // 0 se below gya toh branch fail
        
        return backtrack(0,k,arr);
    }
};