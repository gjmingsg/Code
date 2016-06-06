#include<stdio.h>
int main(){
   int t,a;
   long b;
   int x[10]={0,1,4,4,2,1,1,4,4,2};
   int y[10][5]={{0},{1},{2, 4, 8, 6},{3, 9, 7, 1},{4, 6},{5},{6},{7, 9, 3, 1},{8, 4, 2, 6},{9,1}};
   scanf("%d",&t);
   while(--t >= 0){
       scanf("%d %ld",&a, &b);
       a %= 10;
       
       if(a==0)
       {printf("%d\n",0); continue;}
       if(b==0)
       {printf("%d\n",1); continue;}
       b %= x[a];
       //printf("%d,%d",a,(b-1)%x[a]);
       printf("%d\n",y[a][(x[a]+b-1)%x[a]]);          
   }  
   return 1;  
} 
