#include<stdio.h>
#include<math.h>
int d(int n){
	
	int i,sum, temp=n/2 + 1;
	sum=0;
	 
	for(i=1;i<temp;i++){
				
	    if(n%i==0){
	        sum+= i;
	  
	    }

	}
    
	return sum;	
} 
int main(){
    int i,sum,temp;
    sum=0;
	for(i=1;i<=10000;i++){
		temp = d(i);				  
	    if(d(temp)==i && temp!=i)
		    sum += i;					  
    }
	printf("%d\n",sum); 
	return 0;	
}
