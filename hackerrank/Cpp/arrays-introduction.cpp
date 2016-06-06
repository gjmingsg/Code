#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int N,item;
    vector<int> arr;
    cin >> N;
    for(int i=0;i<N;i++){
       cin>>item;
       arr.push_back(item);
    }
    cout<< arr[N-1];
    for(int i=N-1;i>=0;i--)
       cout<<" " << arr[i];
    cout << endl;
    return 0;
}
