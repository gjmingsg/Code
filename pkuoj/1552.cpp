#include<stdio.h>
int main(){
	int order[200]={0},num,p[15],i,count,k,temp;
	i=0;
	while(scanf("%d",&num)!=EOF & num!=-1){
	    if(num==0)
		{
		 	count =0;	  
		 	for(k=0;k<i;k++){
				temp = p[k] * 2;			 
	            if(temp< 200 && order[temp]==1)
	                count ++;
			}	  
		    i=0;
			for(k=0;k<200;k++) order[k]=0;
			printf("%d\n",count);   		  
        }else{
		    order[num]=1;
			p[i] = num;
			i++;	  
        }							
	}
    return 0;	
}
