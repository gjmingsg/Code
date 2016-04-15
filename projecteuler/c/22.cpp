#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int Comp(const void *p1,const void *p2) {
return strcmp((char *)p1,(char *)p2);	
}
int main()
{
 	char ans[5164][20];
 	long count = 0;
 	long score = 0;
 	long index = 0;
 	int len ,i,j;
	while(scanf("%s",ans[index])!=EOF){
		index ++;						
	} 
	qsort(ans,index,sizeof(ans[0]),Comp); 
    for(i=0;i<index;i++){
		len = strlen(ans[i]);
		score = 0;
		for(int j=0;j<len;j++ ){
			score += (ans[i][j]-'A' + 1);	
		}
		count += ((i+1) * score);
		
	 
		}
	printf("%ld\n",count);
		
} 
