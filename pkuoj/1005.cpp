//05/07/13 23:30 Î´Í¨¹ýWA 

#include<stdio.h>
int main(){
	int n = 0,i=1;
	double x,y,temp;
	int z = 1;
	scanf("%d",&n);
	while(n>0){
 	    scanf("%lf%lf",&x,&y);
 	    temp =((x * x + y * y) *3.1415926)/2;
 	    z = 1;
		while(temp>50){
		  temp -= 50;
		  z++;			   
        } 
 		printf("Property %d: This property will begin eroding in year %d.\n",i,z);
 		n --;
 		
 		i++;
 	}
 	printf("END OF OUTPUT.\n");

    return 0;
} 
