#include<stdio.h>
#define M 102
#define N 102
int is_w[N][M]={0};
char field[N][M];
int n,m;

int isW(int i,int j){
	if(is_w[i][j]==0 &&  field[i][j]=='W'){
	    is_w[i][j] = 1;
		if(i-1>=0 && is_w[i-1][j]==0 && field[i-1][j]=='W'){
		   isW(i-1,j);
		  
	    }
		if(i+1<n && is_w[i+1][j]==0 && field[i+1][j]=='W'){
		   isW(i+1,j);
		  
	    }
		if(j-1>=0 && is_w[i][j-1]==0 && field[i][j-1]=='W'){
		   isW(i,j-1);
		 
	    }
		if(j+1<m && is_w[i][j+1]==0 && field[i][j+1]=='W'){
		   isW(i,j+1);
		  
	    }
		if(i-1>=0 && j-1>=0 && is_w[i-1][j-1]==0 && field[i-1][j-1]=='W'){
		   isW(i-1,j-1);
		  
	    }
		if(i+1<n && j+1<m && is_w[i+1][j+1]==0 && field[i+1][j+1]=='W'){
		   isW(i+1,j+1);
		   
	    }
		if(j-1>=0 && i+1<n && is_w[i+1][j-1]==0 && field[i+1][j-1]=='W'){
		   isW(i+1,j-1);
		  
	    }
		if(j+1<m && i-1>=0 && is_w[i-1][j+1]==0 && field[i-1][j+1]=='W'){
		   isW(i-1,j+1);   
		  
	    }    
	    return 1;
	}
	return 0;       
}
int printW(){
	int i,j;
	for(i=0;i<n;i++){
	for(j=0;j<m;j++)printf("%d",is_w[i][j]);	
	printf("\n");
	}
	printf("\n");
}
int find_ponds(){
    int i,j,count=0;
	for(i=0;i<n;i++){
		for(j=0;j<m;j++){
          if(isW(i,j)==1){ 
              count++; 
          //    printW();
          }
		}			 
    }
	return count;	
} 


int main(){
	int i,j;
	
	while(scanf("%d%d",&n,&m)!=EOF){
		for(i=0;i<n;i++) 
		    scanf("%s",field[i]);
        for(i=0;i<N;i++)
	       for(j=0;j<M;j++)
	          is_w[i][j]=0;
		printf("%d\n",find_ponds());															
	}
	return 0;	
}
