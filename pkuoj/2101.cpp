#include<stdio.h>
#include<math.h>
int main(){
	int n,e,el,nl,temp,ans,i;
	while(scanf("%d%d",&n,&e)!=EOF){
	    el=0;
		nl=0;
		for(i=1;i<n;i++){
	        scanf("%d",&temp);
	        nl += temp;
		}
		for(i=1;i<e;i++){
	        scanf("%d",&temp);
	        el += temp;
		}
		ans =(int) ceil(sqrt(nl*nl + el*el));
		printf("%d\n",ans);								
	}
    return 0;	
} 
