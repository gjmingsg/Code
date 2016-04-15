#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n,oper,num;
    vector<int> stack,max_stack;
    while(cin>>n){
        while((n--)>0){
	        scanf("%d",&oper);
//		    cin>>oper;
		    switch(oper){
			    case 1:
					 //cin>>num;
					 scanf("%d",&num);
					 stack.push_back(num);
					 if(max_stack.empty()||max_stack.back()<=num  )
					     max_stack.push_back(num);
					 break;
	            case 2:
					 if(stack.empty()==false){
						 int top = stack.back();
						 stack.pop_back();
						 if(top==max_stack.back())
						     max_stack.pop_back();
					 }
					 break;
				case 3:
					 cout << max_stack.back()<<endl;
					 break; 
			}
		}
		stack.clear();
		max_stack.clear();
	}
    return 0;
}
