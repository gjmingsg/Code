#include<stdio.h>
#define R 10
int main(){
	char isbn[11];
	int i,temp,m,flag;
	while(scanf("%s",isbn)!=EOF){
		temp = 0;
		m=0;
		flag = 0;
		for(i=0;i<R;i++)
		{
		 	if(isbn[i]!='?'){
				if(isbn[i]=='X')	
				    temp += 10;
				else		 
     		        temp += (isbn[i] - '0') *(R - i);			  				
		    }			
			else{
				m = R - i; 
		    }    	  				
	    }

		for(i=0	;i<=R;i++){
            if((m!=1)&&(i==R))   	
				break;
		    if((temp + i*m)%11==0){
				if(i==R)
		     	    printf("X\n");
				else		   
		     	    printf("%d\n",i);
			    flag = 1;
			    break;			
			 }    			 
	    }
	    if(flag == 0)
	    	printf("-1\n");								 							 
    }	
    return 0;
}
