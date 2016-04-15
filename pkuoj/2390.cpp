#include<stdio.h>
#include<math.h>
int  main(){
     int R,M,Y,i;
     double temp,yr;
     while(scanf("%d%d%d",&R,&M,&Y)!=EOF){
         yr = 1+R/100.0;
         temp = M * 1.0;
         for(i=0;i<Y;i++)
             temp *= yr;
         printf("%d\n",(int)floor(temp));
     }
     return 0;     
}
     
