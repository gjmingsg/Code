#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
   vector<string> s;
   s.push_back("one");
   s.push_back("two");
   s.push_back("three");
   s.push_back("four");
   s.push_back("five");
   s.push_back("six");
   s.push_back("seven");
   s.push_back("eight");
   s.push_back("nine");
   int a,b;
   cin >> a >> b;
   for(int i = a; i<=b; i ++){
      if(i>0 && i <10)
          cout << s[i-1] << endl;
      else if(i%2==0)
          cout << "even" << endl;  
      else 
          cout << "odd" << endl;     
   }
   
   return 0; 
}
