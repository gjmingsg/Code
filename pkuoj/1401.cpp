#include<stdio.h>
int main(){
    long N,count,T,i,temp;
    scanf("%ld",&T);
    	while(T>0){
	       scanf("%ld",&N);
	       T--;
	       count = 0;
	       while((N/=5)>0) count+= N;

		   printf("%ld\n",count);
	    }					   
	
	return 0;
}
