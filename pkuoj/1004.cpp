#include<stdio.h>
int main()
{
    int month = 1;
    double money = 0,temp = 0;
    while(scanf("%lf",&temp)){
        money += temp;     
        if(month==12){
            month = 1;
            printf("$%.2f\n",money/12);
            return 0;
            money = 0;
        }else{
            month++;
        }
                                  
    }
}
