#include<stdio.h>
#include<string.h>
#define LEN 32
int main(){
	int N,temp,i,index;
	char ip[34];
	while(scanf("%d",&N)!=EOF){
		for(i=0;i<N;i++){			 
		   scanf("%s",ip);
		   temp =0;
		   for(index=0;index<LEN;index++){
			  temp = temp << 1;
   	          temp+=ip[index]-'0';
 			  if((index+1)%8==0){
			     if(index!=LEN-1)
		             printf("%d.",temp);
				 else			 
	 				 printf("%d\n",temp);
				 temp=0;			  
   	          }

		   } 
	    }					   
    }
	return 0;	
}
