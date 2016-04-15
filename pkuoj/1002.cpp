#include <iostream>
#include <cstdio>
#include <string>
#include <cctype>
#include <cmath>
using namespace std;
const int mapping[26] = {2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6,
	7, 0, 7, 7, 8, 8, 8, 9, 9, 9, 0};
const long int fact[9] = {1, 10, 100, 1000, 10000, 100000, 1000000, 
	10000000, 100000000};
int duplicate[10000000];
int main()
{
	long int i, j, n, k, S;
	string str;
	cin >> n;
	for(j = 0; j < n; j++){
		cin >> str;
		k = 0;
		//cout << str << " -> ";
		for(i = 0, S = 0; i < str.length(); i++){
			if(isdigit(str[i])){
				k += fact[6 - S++] * (str[i] - '0');
			}else if(isalpha(str[i])){
				k += fact[6 - S++] * (mapping[str[i] - 'A']);
			}
		}
		//cout  << k << endl;
		duplicate[k]++;
	}
	k = 0;
	for(i = 0; i < 10000000; i++){
		if(duplicate[i] > 1){
			printf("%03d-%04d %d\n", i / 10000, i % 10000, duplicate[i]);
			k = 1;
		}
	}
	if(!k) cout << "No duplicates." << endl;
	return 0;
}