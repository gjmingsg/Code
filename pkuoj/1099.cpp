#include<stdio.h>
#define  M 20

int print(int asmt[M][M],int m){
	char molecules[4*M+4][4*M+4];
	int i,j,len = 4*m+3 ,mi,mj;
    for(i=0;i<4*M+4;i++)
	    for(j=0;j<4*M+4;j++)
		    molecules[i][j]=' ';					 

	for(i=0;i<len;i++)	printf("*");
	printf("\n");		
	for(i=0,mi=0;i<m;i++,mi+=4){
	    for(j=0,mj=2;j<m;j++,mj+=4)
	    {
		 	molecules[mi][mj]='O';					   
		 	molecules[mi][mj-2]=molecules[mi][mj+2]='H';
		 	if(mi-2>0)
	           molecules[mi-2][mj]= 'H';
			molecules[mi+2][mj]='H';   
		    if(asmt[i][j]==1){
				molecules[mi][mj-1]=molecules[mi][mj+1]='-';				 
            }else if(asmt[i][j]==-1){
		        molecules[mi-1][mj]=molecules[mi+1][mj]='|';				 
            }						   
	    }
    }
   	for(i=0,mi=0;i<m;i++,mi+=4){
	    for(j=0,mj=2;j<m;j++,mj+=4)
	    {
	         if(asmt[i][j]==0)
    	     {
				 if(molecules[mi][mj-2]=='H' && (mj==2 || molecules[mi][mj-3]!= '-') )
                	 molecules[mi][mj-1]='-';
				 else  if(molecules[mi][mj+2]=='H' && molecules[mi][mj+3]!= '-' )
                	 molecules[mi][mj+1]='-';
               	    
 				 if(mi-2>0&&molecules[mi-2][mj]=='H' && molecules[mi-3][mj]!='|')
					 molecules[mi-1][mj]= '|';
	 		     else if(molecules[mi+2][mj]=='H' &&  molecules[mi+3][mj]!='|' )  
                	 molecules[mi+1][mj]= '|';  
		    }
       }
    }
    for(i=0;i<4*m-3;i++)
    {
	    printf("*");
		for(j=0;j<4*m+1;j++){
		    printf("%c",molecules[i][j]);					 
	    } 
	    printf("*\n");					
    }
	for(i=0;i<len;i++)	printf("*");
	printf("\n");		
	return 0;	
}
int main(){
	int asmt[M][M],j,i,m,order=1;
	while(scanf("%d",&m)!=EOF && m!=0){
	    for(i=0;i<m;i++)
		   for(j=0;j<m;j++)
		       scanf("%d",&asmt[i][j]);
		printf("Case %d:\n\n",order++);
	    print(asmt,m);
		printf("\n");						  
    }
    return 0;	
} 
