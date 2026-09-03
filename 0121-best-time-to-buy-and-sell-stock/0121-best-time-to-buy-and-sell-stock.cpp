class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int maxi = 0;
        int n = prices.size();
        int min_price = INT_MAX;
        for(int i=0; i<n; i++){
            min_price = min(min_price, prices[i]);
            profit = prices[i] - min_price;
            maxi = max(maxi, profit);
        }
        return maxi;
    }
};