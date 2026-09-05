class Solution {
public:
    long long minCost(vector<int>& startPos, vector<int>& homePos,
                      vector<int>& rowCosts, vector<int>& colCosts) {

        int r1 = startPos[0];
        int c1 = startPos[1];

        int r2 = homePos[0];
        int c2 = homePos[1];

        long long totalCost = 0;

        // Move vertically
        if (r1 < r2) {
            for (int r = r1 + 1; r <= r2; r++) {
                totalCost += rowCosts[r];
            }
        } else {
            for (int r = r1 - 1; r >= r2; r--) {
                totalCost += rowCosts[r];
            }
        }

        // Move horizontally
        if (c1 < c2) {
            for (int c = c1 + 1; c <= c2; c++) {
                totalCost += colCosts[c];
            }
        } else {
            for (int c = c1 - 1; c >= c2; c--) {
                totalCost += colCosts[c];
            }
        }

        return totalCost;
    }
};