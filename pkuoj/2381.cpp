#include<stdio.h>
#define L 16000010
int reminder[L]; ///对于数据很大的时候，需要用全局变量申明，初始化的值好像默认为0 
 
int main(){
	int a,c,r,m,i,max=0,rn,temp;

	while(scanf("%d %d %d %d",&a,&c,&m,&r)!=EOF){
	    for(i=0;i<L;i++)
		    reminder[i]=0;
	    rn = r;
	    while(reminder[rn]==0){
	       temp = rn;
		   reminder[rn]=1;				   
		   rn = (a * rn + c)%m;				   
        }
        for(i=0;i<m;i++)
           if(reminder[i]==1){
               r = i;
               break;
        }
        max=0;
        rn = r;
        for(i=r+1;i<m;i++){
			temp = rn;			 
			if(reminder[i]==1){	
			    if(i-temp>max)
			        max=i-temp;  
			    rn = i;    
			}		   
        }    
		printf("%d\n",max);									   
    }	
    return 0;
}
