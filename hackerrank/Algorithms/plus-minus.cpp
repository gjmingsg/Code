#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int n;
    int t;
    double ne,z,p;
    ne = 0.0;
    z = 0.0;
    p = 0.0;
    cin >> n;
     
    for(int arr_i = 0;arr_i < n;arr_i++){
       cin >> t;
       if(t>0) p+=1;
       if(t==0) z += 1;
       if(t<0) ne +=1;
    }
  
    cout << p/n << endl;
    cout << ne/n << endl;
    cout << z/n << endl;
    
    return 0;
}
