#include<stdio.h>
int main(){
    double length,temp;
    int n=0; 
    while(scanf("%lf",&length) && length>0.0){
        n = 2;
        temp = 0;
        while(temp < length){
            temp += 1.0/n;
            n ++;       
        }
        printf("%d card(s)\n",n - 2);               
    }
    return 0;    
} 
