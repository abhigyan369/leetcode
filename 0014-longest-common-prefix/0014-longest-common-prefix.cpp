class Solution {
public:
    string common(string s1, string s2){
        int n = min(s1.size(), s2.size());
        string s = "";
        for(int i=0; i<n; i++){
            if(s1[i] == s2[i]){
                s.push_back(s1[i]);
            }
            else{
                break;
            }
        }
        return s;
    }
    string longestCommonPrefix(vector<string>& strs) {
        string s = strs[0];
        for(int i=1; i<strs.size(); i++){
            s = common(s,strs[i]);
        }
        return s;
    }
};