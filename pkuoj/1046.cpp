#include<stdio.h>
#define L 16
#define MAX 255 * 255 * 3
int main(){
	int target[L][3];
	int sR,sB,sG,i,max,temp,index;
	for(i=0;i<L;i++)
	    scanf("%d%d%d",&target[i][0],&target[i][1],&target[i][2]);
	while(1){
        max = MAX;
        index = 0;
	   	scanf("%d%d%d",&sR,&sB,&sG);
	   	if(sR==-1 && sB == -1 && sG ==-1)
	   	   break;
 	    for(i=0;i<L;i++){
			temp = (target[i][0] - sR)*(target[i][0] - sR) + (target[i][1] - sB)*(target[i][1] - sB) + (target[i][2] - sG)*(target[i][2] - sG);
			if(max>temp){
			    max = temp;
			    index  = i;
			}			 
        }
        printf("(%d,%d,%d) maps to (%d,%d,%d)\n",sR,sB,sG,target[index][0],target[index][1],target[index][2]);
    }
    return 0;
}
