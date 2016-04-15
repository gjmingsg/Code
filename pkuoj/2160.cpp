#include<stdio.h>
#include<stdlib.h>
int  comp(const void *p1,const void *p2){
	 if(((int**)p2)[0]>((int**)p1)[0])
	    return -1;
	 else if (((int**)p2)[0]==((int**)p1)[0] && ((int**)p2)[1]>=((int**)p1)[1])
	    return -1;
	 else 
	    return 1;   
}
 
int main(){
	int tan[6][2],i,j,index,index2,flag,temp,ti;
	i=0;
	while(scanf("%d%d",&tan[i][0],&tan[i][1])!=EOF){
	
		if(tan[i][0]>tan[i][1])
        {
            temp = tan[i][1];
            tan[i][1] = tan[i][0];
            tan[i][0] = temp; 
	    }
	    i+=1;
	    if(i==6){
            flag=0;
			qsort(tan,6,sizeof(tan[0]),comp);
			
		    for(j=0;j<3;j++){
				temp = j * 2;			 
			    if(!(tan[temp][0]==tan[temp+1][0] && tan[temp][1] == tan[temp+1][1]))
				{flag = 1; break;}				 
		    }
		    if(flag == 0){
			    if(tan[0][0]==tan[2][0] || tan[0][0]==tan[2][1]){
			       if(tan[0][0]==tan[2][0])
			           index = 1;
			       else 
			           index = 0;
                   ti=4;
				}
				else if(tan[0][0]==tan[4][0] || tan[0][0]==tan[4][1]){
	   			   if(tan[0][0]==tan[4][0])
			           index = 1;
			       else 
			           index = 0;
                   ti=2;
			    }
				else
			       flag = 1;
			    if(flag==0){   
	                if(tan[0][1]==tan[ti][0])
					    index2= 1;
					else if(tan[0][1]==tan[ti][1])
					    index2=0;
					else
				       flag = 1;   
				    if(flag==0){   
			            if(tan[ti][index2]==tan[(ti==4?2:4)][index]){}
						else
						   flag =1;
		            }
	           }
            }
			if(flag==0)				  
   			    printf("POSSIBLE\n");	
			else 
	     	    printf("IMPOSSIBLE\n");	
  			i=0;
        }	 
		 								
	}	
	return 0;
} 
