#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int find_index(vector<string> &a, string key){
	for(int i=0;i<a.size();i++){
	    if(a[i]==key)
	        return i;
	}	
	return -1;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    vector<string> vstr;
    vector<int> str_count;
    int n,q;
    string strs;
    while(cin>>n){
        while((n--)>0){
	        cin >> strs;
	        int i = find_index(vstr,strs);
			if (i==-1)
			{
			    vstr.push_back(strs);
			    str_count.push_back(1);
			}  else {
			   str_count[i]++;
			}
		}
		cin>>q;
		while((q--)>0){
            cin >> strs;
            int i = find_index(vstr,strs);
            if(i==-1)
                cout << 0 << endl;
            else
                cout<< str_count[i] << endl;
        }
    }
    return 0;
}

