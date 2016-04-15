#include<stdio.h>
int hash[1000001]={0};
int length[1000001]={0};
int main(){
    int num,temp,i,count,loop;
    while(scanf("%d",&num)!=EOF){
      
        for(i=0;i<1000001;i++)
            hash[i]=length[i]=0;  
        temp = num; 
        count = i=0;                             
        while(1){
            temp = (temp / 10) % 10000;
            //printf("%d ",temp);
            temp = temp * temp;
            //printf("%d ",temp);
            if(temp>999999)
            temp = temp % 1000000;
            //printf("%d\n",temp);
            if(hash[temp]==0)
            {
                length[i++]= temp;
                hash[temp]=1;
                count ++;
            }else
                break;  
               
        }
        loop=0;
        while(length[i--]!=temp){loop++;}
        printf("%d %d %d\n",temp,loop,count+1); 
                           
    }
    return 0;
}
 
