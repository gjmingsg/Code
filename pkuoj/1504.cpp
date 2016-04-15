#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main(){
	int N,a,b,c;
	char sa[10],sb[10];
	while(scanf("%d",&N)!=EOF){
	    while(N-->0){
		    scanf("%s%s",sa,sb);
			a = atoi(strrev(sa));
			b = atoi(strrev(sb));
			c = (a+b);
			while(c%10==0) c/=10;
			sprintf(sb, "%d", c);
			printf("%s\n",strrev(sb));			 
        }						   
    }
    return 0;	
}
