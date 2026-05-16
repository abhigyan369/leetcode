#include <iostream>
#include <vector>
using namespace std;

vector<int> arr = {2,45,2,3,44,54,23};

int maxi(vector<int>&arr, int n){
    // base case
    if (n==1) return arr[0];
    int last = arr[n-1];
    return max(last, maxi(arr,n-1));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int ans = maxi(arr, arr.size());
    cout << ans << endl;

    return 0;
}