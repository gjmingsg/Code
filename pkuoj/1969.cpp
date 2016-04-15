#include<stdio.h>
int main(){
    long  n,x,y,k;
    while(scanf("%d",&n)!=EOF){
		k=1;					   
	    while(k*(k+1)<2*n) k++;
		if(k%2==0){
        	y = k - ((k*(k+1)/2)- n);	
			x = k + 1 - y;   
		}
		else{
		 	x =  k -((k*(k+1)/2)- n);
		 	y = k + 1 - x;
        }
        printf("TERM %d IS %d/%d\n",n,y,x);
								   
    }
    return 0;	
} 
