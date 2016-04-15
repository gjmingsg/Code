#include <iostream>
using namespace std;

const unsigned MAX_SIZE = 50;

bool loop;
int n, m4, shrunk[MAX_SIZE];

int main(){
	int i, k;
	scanf("%d", &n);
	loop = true;
	for ( i = 0; ; ++i ) {
		n /= 10;
		m4 = n % 10000;
		n = m4 * m4;
		if(n > 999999)
			n %= 1000000;
		shrunk[i] = n;
		for ( k = 0; k < i; ++k ) {
			if(shrunk[k] == n ){
				loop = false;
				break;
			}
		}
		if(!loop)break;
	}
	printf("%d %d %d\n",shrunk[i], i - k, i + 1);
	return 0;
}
