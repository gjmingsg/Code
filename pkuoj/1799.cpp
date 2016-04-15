#include<stdio.h>
#include<math.h>
#define PI 3.1415926535
int main(){
	int t,n,i;
	float R,r;
	while(scanf("%d",&t)!=EOF){
		i=1;					   
	    while(t-->0){
		    scanf("%f%d",&R,&n);
			printf("Scenario #%d:\n",i++);
			printf("%.3f\n\n",R*sin(PI/n)/(1+sin(PI/n)));			 
        }						   
    }
    return 0;	
}
