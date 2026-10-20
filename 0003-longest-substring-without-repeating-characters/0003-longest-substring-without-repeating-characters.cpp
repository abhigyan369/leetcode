class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<char,int> mp;
        int i = 0; // static- and won't move until repeating number
        int maxi = 0; //j - i + 1

        for(int j=0; j<s.size(); j++){
            // map me hai
            if (mp.find(s[j]) != mp.end()){
                i = max(i, mp[s[j]] + 1);
            }

            mp[s[j]] = j;
            maxi = max(maxi, j-i+1);
        }
        return maxi;


        return maxi;
    }
};