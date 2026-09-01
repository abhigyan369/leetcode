
class Solution {
public:
    vector<int> decrypt(vector<int>& code, int k) {
        int n = code.size();
        vector<int> res(n);

        if (k == 0) {
            return res;
        }

        int left, right;

        if (k > 0) {
            left = 1;
            right = k;
        } else {
            left = n + k;   // n - abs(k)
            right = n - 1;
        }

        int window_sum = 0;

        // Calculate initial window
        for (int i = left; i <= right; i++) {
            window_sum += code[i % n];
        }

        // Slide the window
        for (int i = 0; i < n; i++) {
            res[i] = window_sum;

            window_sum -= code[left % n];
            left++;

            right++;
            window_sum += code[right % n];
        }

        return res;
    }
};

