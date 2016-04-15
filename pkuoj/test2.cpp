
/*
 * 求字符串的逆序数然后按照逆序数的大小输出
 * */

#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int order;
	int count;
}input_info;

int cmp(const void *a, const void *b)
{
	input_info *aa = (input_info *)a;
	input_info *bb = (input_info *)b;
	return aa->count - bb->count;	
}
//计算一行的逆序数
int calculate(char * aline, int n)
{
	int i, j;
	int sum = 0;
	for(i = 0; i < n; i++){
		for(j = i+1; j < n; j++){
			if(aline[i] > aline[j]){
				sum++;
			}
		}
	}
	return sum;
}

int main()
{
	int n, m;
	int i;
	
	scanf("%d %d", &n, &m);
	char **input;
	input = (char **)malloc(sizeof(char *) * n * m);
	input_info *input_info_array;
	input_info_array = (input_info *)malloc(sizeof(input_info)*m);
	for(i = 0; i < m; i++){
		input[i] = (char *)malloc(sizeof(char) * n);
		scanf("%s", input[i]);
		input_info_array[i].order = i;
		input_info_array[i].count = calculate(input[i], n);
	}
	qsort(input_info_array, m, sizeof(input_info), cmp);
	for(i = 0; i < m; i++){
		printf("%s\n", input[input_info_array[i].order]);
	}
	return 0;
}
