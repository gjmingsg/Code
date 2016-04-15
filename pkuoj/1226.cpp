#include<stdio.h>
#include<string.h>
#define N 102
#define L 100
char *copystr(char *dest,char *src,int index,int len){
	int i,j;
	for(i=index,j=0;i<(index+len);i++,j++)
	    dest[j] = src[i];
	dest[j]='\0';    
	return dest;	
} 
int main(){
	int t,n,i,j,k,len,index,largest;
	char str[N][L];
	char temp[L],rtemp[L];
	while(scanf("%d",&t)!=EOF){
		while(t>0){
			scanf("%d",&n);
			i=0;
			while(n>i)
				scanf("%s",str[i++]);
			len = strlen(str[0]);
			largest = 0;
			for(index=0;index<len;index++){
				for(j=1;j<=len-index;j++){	
					
				    copystr(temp,str[0],index,j);
				    strcpy(rtemp,temp);
					strrev(rtemp);
	   	            //printf("取出长度%d %s %s\n",j,temp,rtemp);							
					for(k=1;k<n;k++){
					   if(strstr(str[k],temp)==NULL && strstr(str[k],rtemp)==NULL)
					   	   break;	                   
				    }
					if(n==k){
				        //printf("%d  %s %s\n",j,temp,rtemp);							
     					if(largest<j){
						   largest = j;
   			            }
					}	
				}		   
	        }
			printf("%d\n",largest);	
			t --;	   		   
	    }	
	}
    return 0;
} 
