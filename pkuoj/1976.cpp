#include<stdio.h>
#include<stdlib.h>
#define N 50000
typedef struct {
	int num;
	int i;			
} pcBatch;
int cmp(const void *a, const void *b)
{
	pcBatch *aa = (pcBatch *)a;
	pcBatch *bb = (pcBatch *)b;
	return aa->num < bb->num;	
}
int main(){
	
	int t,n,pc[N],batch_size,i,j,count,select[3]={-1},index;
	pcBatch pb[N];
	while(scanf("%d",&t)!=EOF){
	    scanf("%d",&n);
		for(i=0;i<n;i++) scanf("%d",&pc[i]);
		scanf("%d",&batch_size);

		for(i=0;i<=n-batch_size;i++){
			pb[i].num = 0;
			pb[i].i = i;						
			for(j=i;j<=i+batch_size;j++) pb[i].num += pc[j];
			//TEST		    
			//printf("i = %d , num = %d\n",pb[i].i,pb[i].num);							
	    }
        qsort(pb, n-batch_size+1, sizeof(pcBatch), cmp);
		//printf("\n");
		//for(i=0;i<=n-batch_size;i++){
        //	printf("i = %d , num = %d\n",pb[i].i,pb[i].num);							
		//}	
		index = count = 0;
		select[index]=pb[0].i;
		count = pb[0].num;
		for(i=1;i<=n-batch_size;i++){						 
	        for(j=0;j<=index;j++){
			    if(select[j]+batch_size<pb[i].i && pb[i].i < select[j])
				{
					count += pb[i].num;
					select[++index]=pb[i].i; 								
			    }    					  
            }
		}				   
    }

	return 0;
}
