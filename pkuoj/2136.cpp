#include<stdio.h>

int main(){
    char str[72];
    int h[27]={0},max,i,j;
    while(scanf("%s",str)!=EOF){
		i=0;						
		while(str[i]!='\0'){
			if(str[i]-'A' >=0 && 'Z' - str[i]>=0)																		
	            h[str[i]-'A'] ++;
			i++;				
		}			
    }
    max=0;
    for(i='A';i<='Z';i++){
        if(max<h[i-'A']) max = h[i-'A'];
	}

	for(i=max;i>0;i--){
        for(j='A';j<='Z';j++){
            if(h[j-'A']<i)
                printf(" ");
            else
                printf("*");
            if(j!='Z')
			    printf(" ");    
	     }
         printf("\n");    
	}
	printf("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z\n");
	scanf("%s",str);
    return 0;	
}
