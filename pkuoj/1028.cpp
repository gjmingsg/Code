#include<stdio.h>
#include<string.h>
#define W 100
#define L 103
int main(){
	char f[L][W],b[L][W],c[8],url[W],cururl[W] = "http://www.acm.org/";
	int ftop,btop;
	ftop = btop = -1;
	while(scanf("%s",c)!=EOF){
        if(strcmp("VISIT",c)==0){
			strcpy(b[++btop],cururl);
			ftop = -1;
			scanf("%s",cururl);
			printf("%s\n",cururl);
	    }else if(strcmp("BACK",c)==0){
			
			if(btop<0)
			    printf("Ignored\n");
			else{
				strcpy(f[++ftop],cururl); 
			    strcpy(cururl,b[btop--]);
		    	printf("%s\n",cururl);
			}    
	    }else if(strcmp("FORWARD",c)==0){
			
			 if(ftop<0)
			     printf("Ignored\n");
			 else{
	 	        strcpy(b[++btop],cururl);  
			 	strcpy(cururl,f[ftop--]);  
			 	printf("%s\n",cururl);	  
	         }    
	    }else if(strcmp("FORWARD",c)==0){
			  
	    }else if(strcmp("QUIT",c)==0){
	        break;	  
	    }					 
    }
	return 0;	
} 
