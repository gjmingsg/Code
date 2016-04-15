/**
#include<stdio.h>

int main()
{
    int day;
    while(scanf("%d", &day), day)
    {
        int n = 1;
        while((1+n)*n/2 < day) n++;
        printf("%d %ld\n", day, (n-1)*n*(2*n-1)/6 + n*(day-(n-1)*n/2));
    }
    return 0;
}

**/

#include<stdio.h>
int main(){
	long n,ans,i,t;
	while(scanf("%d",&n)!=EOF && n!=0){
        ans =0;
        t = n;
		for(i=1;i<=n;i++)
		{
			 t-=i;
		     if(t<0){
			    ans += (t+i) * i;
			    break;
		     }else{
			    ans += i * i;	   
	         }		 				  
        }
		printf("%d %ld\n",n,ans);					  
								  
    }
    return 0;	
} 
