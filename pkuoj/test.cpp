#include<stdio.h>
#include<string.h>
#define N 102
#define L 100
int main(){
		char temp[L],rtemp[L];
		int i= 0;
while(true){
		scanf("%s%s",temp,rtemp);
	
		printf("%s",strstr(temp,rtemp));
				printf("%d\n",strstr(temp,rtemp)==NULL);
		for(i = 0;i<12;i++);
		printf("%d",i);		
}
    return 0;	
}
