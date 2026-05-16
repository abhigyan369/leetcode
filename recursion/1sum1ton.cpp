#include <iostream>
using namespace std;

int sum1ton(int n){
    if (n==1) return 1;
    return n + sum1ton(n-1);

}

int main(){

    int ans = sum1ton(5);
    cout << ans << endl;
}