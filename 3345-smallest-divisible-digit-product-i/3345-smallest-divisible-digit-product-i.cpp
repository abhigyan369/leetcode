class Solution {
public:
    int prodOfNum(int n){
        int prod = 1;
        while (n > 0){
            int lastDig = n % 10;
            prod = prod * lastDig;
            n = n / 10;
        }
        return prod;
    }

    int smallestNumber(int n, int t) {
        
        while (prodOfNum(n) % t != 0) {
            n++;
        }
        return n;
    }
};