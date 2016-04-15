#include<stdio.h>
int main(){
	int t,n,p[10001],i,temp,count;
	while(scanf("%d",&t)!=EOF){
		while(t-->0){
			scanf("%d",&n);
			for(i=0;i<n;i++){
		 	    scanf("%d",&p[i]);
		    }
		    count = 0;
		    i=0;
			while(1){
		    	if(p[i]!=(i+1)){
			        temp = p[i];
			        p[i] = p[temp-1];
			        p[temp-1] = temp;
			        count ++;
				}else
				    i ++;
				if(i>=n-1)
				    break;		 
			}
			
			printf("%d\n",count);		 
	    }					   
    }
	return 0;	
} 
