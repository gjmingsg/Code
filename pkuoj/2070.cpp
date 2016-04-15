#include<stdio.h>
int main(){
	float speed,weight,strength;
	int flag = 0;
	do{
	   	flag = 0;
	   	scanf("%f%f%f",&speed,&weight,&strength);
	   	
	   	if(speed<=0.0 && weight<=0.0 && strength<=0)
		   break; 
		 
		if(speed<=4.5 && weight>=150 && strength>=200){  
		   printf("Wide Receiver "); 
		   flag = 1;
        }
		if(speed<=6.0 && weight>=300 && strength>=500){  
		   printf("Lineman ");
		   flag = 1;
        }
        if(speed<=5.0 && weight>=200 && strength>=300){
           printf("Quarterback");
  		   flag = 1;
        }
        if(flag==0)
          printf("No positions");
        printf("\n");
    }while(1);
    return 0;
}
