#include<stdio.h>
#define R 10000
#define L 1000
#define AL L/4
#define NUMTABLE "0123456789ABCDEDGHIJKLMNOPQRSLUVWYZabcdefghijklmnopqrsluvywz"
int printNum(int *num,int length){
	int i;
	for(i=length;i>=0;i--)
	    printf("%d",num[i]);
    printf("\n");
    return 0;	
}
int printChar(){
    return 0;	
}
int getNum(char ap){
	return (ap-'0'>9?(ap-'A'>25?ap-'a'+36:ap-'A'+10):ap-'0');
}
int convert(char *srcNum,int srcB,char *desNum,int desB){
	int B10[AL],i=0,index=0,carry=0,j,BD[AL];
	
	for(j=0;j<AL;j++)
	    BD[j] = B10[j] =0;
    //转换成10进制 
	while(srcNum[i]!='\0'){				   
		for(j=0;j<=index;j++){

	 	    B10[j] = B10[j] * srcB + carry;
            if(carry)
                carry = 0;
	 	    if(B10[j]>R){
	 	        carry = B10[j]/R;
	 	        B10[j] %= R;
		    }
	    }
	    //printf("%d case:+ %d\t",i,getNum(srcNum[i]));
		B10[0] += getNum(srcNum[i]);
		if(carry>0){
		    B10[j] += carry;
		    carry = 0;
		    index = j;
		}
		//printf("%d case:+ %d",i,getNum(srcNum[i]));	
		//printNum(B10,index);			   
		i ++;		   
    }
    //printNum(B10,index);
    //10进制转换其他进制 
    while(index>=0){
	    for(i=index;i>=0;i--){
							  
        }				
    }
	return 0;
}

int main(){
	int n,srcB,desB,i;
	char srcNum[L],desNum[L];
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%d%d%s",&srcB,&desB,srcNum);
		convert(srcNum,srcB,desNum,desB);
		
		//printf("%d %s\n",srcB,srcNum);
		//printf("%d %s\n\n",desB,desNum);				 				 
    }
    return 0;
} 
