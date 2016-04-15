#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    string time;
    int t = 0;
    cin >> time;
    string hour = time.substr(0,2);
    string type = time.substr(8);
    //cout << hour;
    //cout << type;
    t = atoi(hour.c_str());
    //cout << type=="AM" << endl;
    if(type=="AM"){
        if(t==12)
            cout << time.replace(0,2,"00").substr(0,8) << endl;
        else
            cout << time.substr(0,8) << endl;
    }else{
        if(t==12)  
            t=12;
        else
            t += 12;
        string hourstr;
        char t1 = '0'+t/10;
        char t2 = '0'+ t%10;
        hourstr.append(1,t1).append(1,t2);
        cout << time.replace(0,2,hourstr).substr(0,8) << endl;
        
    }
    return 0;
}
