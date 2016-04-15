#include<stdio.h> 
#include<string.h>
#define R 10
#define N(x) ((x)-'0')
#define V(x) ('0'+(x))
#define D(x)  "987654321"[x]
int main(){
    char num[1010],temp[1010];
    int digits[10],i,j,reminder,value,count,k;
    
    while(scanf("%s",num)!=EOF && strcmp(num,"-1")!=0){
        count=0;                       
        for(j=0;j<10;j++)
            digits[j]=0;
        j=0;    
        if( strcmp(num,"0")==0)
        {
            printf("10\n");
            continue;
        }
         if( strcmp(num,"1")==0)
        {
            printf("11\n");
            continue;
        }
        strcpy(temp,num);
        strrev(temp);      
        while(j<9){
            strcpy(num,temp); 
            reminder=0;
            i=strlen(temp)-1;
            while(i>=0){
                 if(reminder==0){       
                     if(temp[i]<D(j) & i>0){
                         value = N(temp[i]) * R + N(temp[i-1]);   
                         temp[i--]='\0';     
                     }  
                     else{
                         value = N(temp[i]);                 
                     } 
                }
                else{
                    value = reminder * R + N(temp[i]);
                } 
                reminder =value % N(D(j));
                temp[i--] = V(value / N(D(j))); 
            }
            //for(k=0;k<strlen(temp);k++)printf("%c",temp[k]);printf("\n");                                                                             
            //printf("%s\n",temp);
            
            if(reminder==0) 
            {
                digits[9-j]++;
                count++;
            }else{
               j++;
               strcpy(temp,num);    
            } 
            
        } 
        for(j=0;j<10;j++){
           if(strcmp(temp,"0")!=0 || count==0)
           {
              printf("There is no such number."); 
              break;  
           }
           else if(count==1 && j==0){
              printf("1");
           }else if(digits[j]>0){
              for(i=0;i<digits[j];i++)
                 printf("%d",j);   
           }
        } 
        printf("\n");                         
    } 
    return 0;    
}
