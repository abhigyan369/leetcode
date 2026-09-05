
class Solution {
public:
    int maxVowels(string s, int k) {
        int n = s.size();
        int ans = INT_MIN;
        int curr_window = 0;
        set<char> st = {'a','e','i','o','u'};

        // first window
        for(int i=0; i<k; i++){
            if(st.count(s[i])){
                curr_window++;
            }
        }
        ans =max(ans, curr_window);
        // slide
        for(int j=k; j<n; j++){
            if(st.count(s[j])){
                curr_window++;
            }
            if(st.count(s[j-k])){
                curr_window--;
            }
            ans = max(ans, curr_window);
        }
        return ans;
    }

};

