class Solution {
public:
    int minimumRecolors(string blocks, int k) {
        int n = blocks.size();
        int ans = INT_MAX;
        // no of operations -> no of swap to convert white into black
        // first window
        int curr_window = 0;
    
        for(int i=0; i<k; i++){
            if (blocks[i] == 'W'){
                curr_window++;
            }
        }
        ans = min(ans,curr_window);
        for(int j=k; j<n; j++){
            if(blocks[j] == 'W'){
                curr_window++;

            }
            if(blocks[j-k] == 'W'){
                curr_window--;
            }

            ans = min(ans,curr_window);
            
        }

        return ans;
    }
};