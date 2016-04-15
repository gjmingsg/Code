#include<stdio.h>
int cycle_length(int n){
	int reminder[1001]={0},order[10001]={0},temp,length=0,i,div,index=0;
	div=1;
	reminder[0]=1;
	temp = 0;
//	printf("0.");
	while(true){
	  //  if(n<div)
	  //      printf("%d",div/n);
	    div %= n;
	    if(reminder[div] == 1)
     	    break;
     	else    
	        reminder[div] = 1;
	    order[index++] = div; 
		if(div<n){		  
		    div *= 10;
		} 												
	}	
//	printf("\n");
	if(div==0)return 0;
	temp = 0;
	for(i=0;i<index;i++){
	    if(order[i]==div && temp==0){ 
		   temp = 1;
		   length=1; 
        } 
		if(temp==1 && order[i]!=div)
		   length ++;   					 
    }
	return length;	
}
int main(){
	int max=0,i,temp,index;
	for(i = 2;i<1000;i++){
	    temp = 	cycle_length(i);
	    //printf("%d=%d\n",i,temp);
		if(temp>max){
		    max=temp;
		    index = i;
		}	  
    }	
    printf("%d",index);
    getchar();
    return 0;
} 
