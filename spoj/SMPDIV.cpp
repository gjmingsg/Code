#include<stdio.h>
int main(){
    int n,x,y,s,i;
    scanf("%d",&s);
    while(s-->0){
       scanf("%d%d%d",&n,&x,&y);
       for(i=2;i<n;i++){
          if(i%x==0 && i%y!=0)
             printf("%d ",i);
       }
       printf("\n");
    }    
    return 1;
} 
