#define FUNCTION(opname,oper) void opname(int& a,int& b){a=(a oper b? a:b);}
#define io(v) cin>>v
#define toStr(s) "Result ="
#define INF 2^32-1
#define foreach(v,i) for(int i=0; i <n; i++)
#include <iostream>
#include <vector>
using namespace std;

#if !defined toStr || !defined io || !defined FUNCTION || !defined INF
#error Missing preprocessor definitions
#endif 

FUNCTION(minimum, <)
FUNCTION(maximum, >)

int main(){
	int n; cin >> n;
	vector<int> v(n);
	foreach(v, i) {
		io(v)[i];
	}
	int mn = INF;
	int mx = -INF;
	foreach(v, i) {
		minimum(mn, v[i]);
		maximum(mx, v[i]);
	}
	int ans = mx - mn;
	cout << toStr(Result =) <<' '<< ans;
system("pause"); 
	return 0;

}
