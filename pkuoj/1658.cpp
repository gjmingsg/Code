#include<stdio.h>
int main(){
	int t,p[4],ans,inc;
	while(scanf("%d",&t)!=EOF){
		while(t-->0){					   
		scanf("%d%d%d%d",&p[0],&p[1],&p[2],&p[3]);
		inc = p[1] - p[0];
		if(p[1]+inc == p[2] && p[2] + inc == p[3])
		    ans = p[3] + inc;
		inc = p[1]/p[0];	
		if(p[1]*inc==p[2] && p[2] * inc == p[3])
			ans = p[3] * inc;	
		printf("%d %d %d %d %d\n",p[0],p[1],p[2],p[3],ans);					   						   
		}
    }
    return 0;	
}
