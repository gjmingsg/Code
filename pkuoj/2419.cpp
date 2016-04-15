#include<stdio.h>
#include<string.h>
#define T 102
#define P 102
int main(){
	int p,t,i,j,count,index[P],temp;
	char hear[P][T],type[P][T];
    
	scanf("%d%d",&p,&t);
	for(i=0;i<=p;i++){
	    for(j=0;j<=t;j++){
             hear[i][j]= 'e';
             type[i][j] = '\0';
	    }
	    type[i][j] = hear[i][j]= '\0';    
	}
	while(scanf("%d%d",&i,&j)!=EOF){
		hear[i][j] = j;
	}
	//for(i=1;i<=p;i++)
	//    printf("%s\n",hear[i]);
	count = 0;
	temp = 0;
	for(i = 1;i<= p;i++){
		for(j=0;j<=count; j++)
		{
		 	//printf("%s==%s %d\n",hear[i],type[j],strcmp(hear[i],type[j]));			  
		 	if(strcmp(hear[i],type[j])==0)
			 {
		         temp = 1;
			  	 break;  						   							  
		     } 			 
        } 
        if(temp==0)
		    strcpy(type[count++],hear[i]);
		else
		    temp = 0;		  
    }
	printf("%d\n",count);
	//for(i=0;i<count;i++)
	//    printf("%s\n",type[i]);
	
	return 0;	
} 
