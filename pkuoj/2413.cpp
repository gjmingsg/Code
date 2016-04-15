#include<stdio.h>
#include<string.h>
#define T 160
#define N 500
#define R 10
char ans[N][T]={'\0'};

int findFib(int i){
	int carry = 0,index=0,j=0,k=0,temp=0;
	while(ans[i-1][j]!='\0'){
					 
		if(ans[i-2][k]!='\0'){					 
		    temp = ans[i-1][j]-'0' + ans[i-2][k]-'0' + carry;
		    k++;
		}else{
			temp = ans[i-1][j]-'0' + carry;  
        }
		if(temp>=R){
		    ans[i][j] = '0' + (temp-R);
		    carry = 1;
		}else{
		 	ans[i][j] = '0' + temp;
	        carry = 0; 
        }
		j++;						 
    }

    if(carry>0)
        ans[i][j++]='0' + carry;
 
    return 0;
}
int findAllFib(){
	int i;
	for(i=2;i<N;i++)
		findFib(i);				
	return 0;	
}

int main(){
	char a[T],b[T],zero[T]={'0'},temp[T],temp2[T];
    int begin = 0,end=0,i,lenstr,flag;
	ans[0][0] = '1';
	ans[1][0] = '2';
	findAllFib();
	
	while((scanf("%s%s",a,b)!=EOF) && strcmp(b,"0")!=0){
		strrev(a);
		strrev(b);
        begin = 0;
        end = 0;
        flag = 0;
		for(i=0;i<N;i++){
		    if(flag==0)
			    strcpy(temp,a);
		    else
			    strcpy(temp,b);
			strcpy(temp2,ans[i]);
			lenstr = strlen(ans[i]) - strlen(temp);
			if(lenstr>0)
			    strncat(temp,zero,lenstr);
            else
			    strncat(temp2,zero,0-lenstr);
			strrev(temp);			    
			strrev(temp2);	   
		//	  printf("====%s : %s\n",temp,temp2);
	        if(flag==0){
				if(strcmp(temp,temp2)<=0){				
			 	    begin = i;
			 	    flag = 1;
			 	    i --;
			 //	    printf("%d %s <= %s\n",i,temp,temp2);
				}   
			}else{
	       		if(strcmp(temp,temp2)>=0){
				    end = i;
 			// 	    printf("%d %s >= %s\n",i,temp,temp2);
			    }	
				else{
				    break;     
				}    
		    } 
	    }
	    end = end - begin + 1;
	    if(end<0) end = 0;
		printf("%d\n",end);						    							    							   
	}
	return 0;	
} 
