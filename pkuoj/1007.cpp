/**
计算每个字符的得分，然后将得分存到对应下标的数组
用index存放各个字符的得分，如果同分，则在同一个index下标下存放 
**/
#include<stdio.h>
int str_count(char* str){
	int count = 0, last =0,i = 1;
	
	while(str[last]!='\0'){
        i = last + 1;
		while(str[i]!='\0'){
		    if(str[last]>str[i])
			    count ++;
			i++;		  
		}
		last ++;
    }
    return count;
}
int main(){
	int n,m,i,temp;
	int order[2000];
	int index[2000][100];
	char array[101][51];
    for(i = 0; i < 2000; i ++)
            order[i] = 0;
	scanf("%d%d",&n,&m);
		for(i = 0; i < m; i ++)
		{
            scanf("%s",array[i]);
            temp= str_count(array[i]);
            index[temp][order[temp]] = i;
            order[temp] ++;
  		}
  		//printf("\n");
		for(i=0;i<2000;i++)
		{
            temp = 0;
		 	while(temp<order[i])
	 		{	
	   		    printf("%s\n",array[index[i][temp]]);
	   		    temp ++;
			}
			order[i] = 0;
        }					    						  
    
	return 0;	
}


