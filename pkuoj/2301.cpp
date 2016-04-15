#include<stdio.h>
int main(){
	int a,b,n;
	int sa,sb;
	scanf("%d",&n);
	while(n>0){
		scanf("%d%d",&a,&b);
		if((a+b)%2!=0 || b>a){
            printf("impossible\n");
            n--;
            continue;
		}
		sa = (a+b)/2;
		sb = a - sa;
		a = (sa>sb?sa:sb);
		b = (sa>sb?sb:sa);
		printf("%d %d\n",a,b);
		n--;		 
    }
	return 0;	
} 
