#include<stdio.h>
#include<stdlib.h>
int ca3(char *src,char *des){
	if(src[1] == des[1] && src[0] == des[0])
	return 0;
	if(src[1] == des[1] || src[0] == des[0]) return 1;
	else return 2;
}
int ca1(char *src,char *des){
	int t1,t2;
	if(src[1] == des[1] && src[0] == des[0])
	return 0;
	t1 = des[1] - '0' - (src[1] - '0');
	t2 = des[0] - 'a' - (src[0] - 'a');
	return t1>t2?t1:t2;
}
int ca2(char *src,char *des){
    if(src[1] == des[1] && src[0] == des[0])
	return 0;
    else if(src[1] == des[1] || src[0] == des[0] || abs(src[0]-des[0])==abs(src[1]-des[1])) 
	return 	1;
	else 
	return 2;
}
int ca4(char *src,char *des){
    if(src[1] == des[1] && src[0] == des[0])
	    return 0;	
	else if(((src[0]-'a'+ 1 + src[1]-'0') % 2) != ((des[0]-'a' + 1 + des[1]-'0')%2))
        return -1;
    else if(abs(src[0]-des[0])==abs(src[1]-des[1]))
        return 1;
	else
	    return 2;
}
int main()
{
 	int t,temp;
 	char a[2][3];
 	while(scanf("%d",&t)!=EOF)
    {
	     while(t-->0){
		     scanf("%s%s",a[0],a[1]);
		     temp = ca4(a[0],a[1]);
		     if(temp==-1)
			     printf("%d %d %d Inf\n",ca1(a[0],a[1]),ca2(a[0],a[1]),ca3(a[0],a[1]));
			 else			  
	 			 printf("%d %d %d %d\n",ca1(a[0],a[1]),ca2(a[0],a[1]),ca3(a[0],a[1]),temp);
	     } 						  
    }
 	return 0; 	
}
