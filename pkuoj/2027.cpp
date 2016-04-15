#include<stdio.h>
int main(){
	int n,x,y,i;
	while(scanf("%d",&n)!=EOF){
	    for(i=0;i<n;i++){
            scanf("%d%d",&x,&y);
            if(x>=y)
                printf("MMM BRAINS\n");
            else
                printf("NO BRAINS\n");
        }
		     						   
    }
    return 0;	
}
