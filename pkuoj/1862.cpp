#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int comp(const void *p1,const void *p2)
{        
    return  *((double*)p2)>*((double*)p1)?1:-1;
}

int main(){
	double m[102];
	int N,i,j;
	while(scanf("%d",&N)!=EOF){
		for(i=0;i<N;i++)scanf("%f",&m[i]);
      
        for(i=0;i<N-1;i++)
		{
		 //排序函数有问题				  
		   qsort(m+i,N-i,sizeof(m[0]),comp);
		//   for(j=0;j<N;j++) printf("%d ",m[j]);printf("\n");				  
		   m[i+1] =  2 * sqrt(m[i]*m[i+1]);
		}
		printf("%.3f\n",m[N-1]);					   
    }
	return 0;	
}
