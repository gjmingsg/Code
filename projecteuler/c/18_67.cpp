#include<stdio.h>
#define N 100
int main(){
    int triangle[N][N],i,j,temp1,temp2,n;
    for(i=0;i<N;i++){
	    for(j=0;j<=i;j++)
		    scanf("%d",&triangle[i][j]);				 
    }
    for(i=N-1;i>0;i--){
		for(j=0;j<i;j++){
		    temp1 = triangle[i][j]+ triangle[i-1][j];
			temp2 = triangle[i][j+1]+ triangle[i-1][j];
			if(temp1>temp2)
			    triangle[i-1][j] = temp1;
			else
			    triangle[i-1][j] = temp2; 	  				  
        }				
    }
    
    printf("%d\n",triangle[0][0]);
    scanf("%d",&n);
    return 0;	
} 
