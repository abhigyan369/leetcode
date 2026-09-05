class Solution {
  public:
    int count(int n){
        int cnt = 0;
        while(n > 0){
            n = n/10;
            cnt++;
        }
        return cnt;
    }
    bool armstrongNumber(int n) {
        // code here
        int original = n;
        int totalDigits = count(n);
        int sum = 0;
        while (n > 0){
            int rem = n%10;
            sum += pow(rem,totalDigits);
            n = n/10;
        }
        if(sum == original) return true;
        
        return false;
        
    }
};