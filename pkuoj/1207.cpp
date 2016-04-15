#include<stdio.h>
int count(int num)
{
 	int count = 1;
    while(num!=1){
	    if(num%2==0)
		    num /= 2;
		else
		    num = num * 3 + 1;
		count ++;	  
    }
    return count;
}
int main(){
   int a,b,max,tempa,tempb,i,temp;
   while(scanf("%d%d",&a,&b)!=EOF){
       max = 0;
       tempa = (a>b?b:a);
	   tempb = (a>b?a:b);
	   for(i=tempa;i<=tempb;i++){
           temp = count(i);
		   if(max<temp)
		       max = temp;
	   }
	   printf("%d %d %d\n",a,b,max);
   } 	
   return 0;
}
