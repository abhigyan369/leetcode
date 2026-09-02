class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        map<int,int> mp;
        int n = fruits.size();
        int left =0;
        int maxi = 0;
        for(int right=0; right<n; right++){
            mp[fruits[right]]++;
            while (mp.size() > 2){
                mp[fruits[left]]--;
                if (mp[fruits[left]]==0){
                    mp.erase(fruits[left]);
                    
                }
                left++;
            }
            maxi = max(maxi, right-left+1);
        }
        return maxi;
    }
};