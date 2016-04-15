#include<stdio.h>
#include<string.h>
int getnum(char* str,int len){
	int ans = 0,i;
	for(i=0;i<len;i++){
	    ans += (str[i]-'A' +1);				   
    }
    return ans;
}

int main(){
	char str[100];
	int array[100],i,count,temp;
	for(i=1;i<100;i++){
        array[i-1] = i*(i+1)/2;
	}
	count=0;
	while(scanf("%s",str)!=EOF){
		temp = getnum(str,strlen(str));
		for(i=1;i<100;i++){
           
 			if(array[i-1] == temp){
		  	    count++;
			    printf("%s=%d",str,temp);
		  	    break;
		    }			   
        }																
	}
	printf("\n%d",count);
	return 0;	
} 
