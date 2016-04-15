#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int t;
    char str[1002];
    vector<char> stack;
    while(cin>>t){
	    while((t--)>0){
	        cin >> str;
	        int i=0;
	        while(str[i]!='\0'){
			
		        if(stack.empty()==0 
				 &&((str[i]==')' && stack.back()=='(') 
				 ||(str[i]==']' && stack.back()=='[') 
				 ||(str[i]=='}' && stack.back()=='{')))
			        stack.pop_back(); 
 		        else
 		            stack.push_back(str[i]);
			    i++;
    			
		    }
		   
		    if(stack.empty())
		        cout << "YES" << endl;
            else
                cout << "NO" << endl;
            stack.clear();
		}			  
    }
    return 0;
}
