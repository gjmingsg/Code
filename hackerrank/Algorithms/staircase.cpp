#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int n;
    cin >> n;
    string line(n,' ');
    string sharp(n,'#');

    for(int i=n; i>0; i--){

        cout << line.replace(i-1,n-1,sharp.substr(i-1)).substr(0,n)<< endl;        
    }
    return 0;
}
