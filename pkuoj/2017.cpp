#include<stdio.h>
int main(){
	int n,s,t,ans,i,prev;
	while(scanf("%d",&n)!=EOF && (n!=-1))
	{
	 	prev=0;	
		ans = 0;				  
	    for(i=0;i<n;i++){
        	scanf("%d%d",&s,&t);
			ans += s * (t-prev);
			prev = t;			 
        }
		printf("%d miles\n",ans);     						  
    }
	return 0;	
}
