#include<stdio.h>
#include<string.h>

#define DEGREE 10000
/*
����R��ֵ����һ����6λ��Ҳ�п���������6λ�������6λ���� 0.12��23ʲô�ġ�
����Ҫ����R=0��n=0�������������û����֤������ԣ����Բ�֪���ǲ��Ǳ���ġ�
������Ϊ��ѭ�����룬���ԣ�ÿ���������ʱ�ǵ�Ҫ�Ѵ洢�ռ����㡣
����С����������λ�ÿ��ܣ�(1).123���ͣ�С��������ǰ�棻(2)0.123���ͣ�С�����������м䣻(3)123.����С���������ֵ����
�����������Ĵ��ڣ��� 000012��000.02��0011.2��12.000��00.000���ȶ�Ҫ���ǵ���
���������ʽ��0.123 Ӧ���� .123����123. Ӧ���� 123 ��
*/
int cal(char ans[],int n, long long *numArr)
{
    int i = 0,length,index = 0,j;
    long long temp = 0l,up;
    length = strlen(ans);
    while(length)
    {   
        length --;  
        if(ans[i] == '.')
        {
            i ++;
            continue;
        }      
        temp *= 10;
        temp += ans[i ++] - '0';
                
    }  
    numArr[index] = temp;
    
    for(i = 1; i < n; i ++)
    {
        up = 0l;
        for(j = 0; j <= index; j ++)
        {
            numArr[j] *= temp;
            numArr[j] += up;  
            up = 0l; 
            if(numArr[j] >= DEGREE)
            {
                up =  numArr[j] / DEGREE;
                numArr[j] %= DEGREE;            
            }       
        }
       
         while(up != 0l)
         {
             numArr[++index] += up;
             up = 0l;
             if(numArr[index] >= DEGREE)
             {
                 up =  numArr[index] / DEGREE;
                 numArr[index] %= DEGREE;            
             }         
         }
            
    }  
    //for(i = index;i >= 0; i --)
    //    printf("%04d",numArr[i]);
    //printf("\n");  
    return index;
}
int getLength(long long a)
{
    if(a < 10l)
        return 1;
    else if(a < 100l)
        return 2;
    else if(a < 1000l)
        return 3;
    else if(a < 10000l)
        return 4;    
}
int printPoint(long long xxx,int pindex,char hflag)
{
     int ans = (int)xxx;
     if(hflag = 'h')
     {
         if(pindex == 0)
             printf("%ld.",ans);
         else if(pindex == 1)
             printf("%ld.%ld",ans / 10,ans%10);
         else if(pindex == 2)
             printf("%ld.%02ld",ans / 100,ans%100);
         else if(pindex == 3)
             printf("%ld.%03ld",ans / 1000,ans%1000);     
     }
     else
     {
         if(pindex == 0)
             printf("%04ld.",ans);
         else if(pindex == 1)
             printf("%03ld.%ld",ans / 10,ans%10);
         else if(pindex == 2)
             printf("%02ld.%02ld",ans / 100,ans%100);
         else if(pindex == 3)
             printf("%ld.%03ld",ans / 1000,ans%1000);
     }
     return 0;
}
int printEnd(long long xxx)
{
    int a = (int)xxx;
    if(a < 1)
       printf("0000");
    if(a < 10)
       printf("000");
    else if(a < 100)
        printf("00");
    else if(a < 1000)
        printf("0");
    while(a%10 == 0)
        a/=10;
    printf("%d\n",a);
    return 0;
}
int chechEnd(long long *ans,int length)
{
    int i = 0;
    while(ans[i ++]==0l && i <= length);
    return i - 1;
}
int main()
{
    char R[7],*p;
    long long ans[50];
    int i,plength,pindex,length,n,numlength,ppindex,endindex,temp;
   
    while(scanf("%s%d",R,&n)!=-1)
    {
        if(n==0)
        {
            printf("1\n");
            continue;          
        }
        length = strlen(R);
        if(length == 0 && R[0] == '0' && n == 1)
        {
            printf("1\n");
            continue;        
        } 
        p = strchr(R,'.');
      
        if(p == NULL)
            pindex = length;
        else
            pindex = p - R;
        
        plength = (length - pindex - 1) * n;
        for(i = 0 ; i < 50; i ++)
            ans[i] = 0l;
        length = cal(R,n,ans);
        numlength = length * 4;
        ///���С����ĸ�ʽ��.xxxxxx .001
        if(plength >= numlength + getLength(ans[length]))
        {
            endindex = chechEnd(ans,length);
            printf(".");
            temp = plength - numlength - getLength(ans[length]);
            for(i = 0 ; i < temp; i ++)
                printf("0");
            if(endindex == length)
            {
                 temp = (int) ans[length];
                 while(temp%10 == 0)
                     temp/=10;
                 printf("%d\n",temp);
            }
            else
            {
                for(i = length - 1; i > endindex; i --)
                    printf("%04ld",ans[i]);
                printEnd(ans[endindex]);
            }

        }
        else
        {
            ///���С������xxxx. 
            if(plength == 0)
            {
                printf("%ld",ans[length]);        
                for(i = length - 1; i >= 0; i --)
                    printf("%04ld",ans[i]);
                printf("\n");        
            }
            else
            {
                ///���С������xxxx.xxxx 
                 pindex = plength % 4;
                 ppindex = plength /4;
               
                 endindex = chechEnd(ans,length);
                 temp = (endindex>ppindex?ppindex:endindex);
                 for(i = length; i > temp; i --)
                 {
                     if(ppindex == i)
                     {
                         if(i == length)
                             printPoint(ans[i],pindex,'h');
                         else
                             printPoint(ans[i],pindex,'m');      
                     }
                     else
                     {
                         if(i == length)
                            printf("%ld",ans[i]); 
                         else
                            printf("%04ld",ans[i]); 
                         
                     }
                 }
                 ///���С����xxxx000.,XXXX000.01
                 if(ppindex < endindex)
                 {
                      if(pindex == 0)
                          printf("0000\n");
                      if(pindex == 1)
                          printf("000\n");
                      else if(pindex == 2)
                          printf("00\n");
                      else if(pindex == 3)
                          printf("0\n");
                 }    
                 else if(ppindex == endindex)
                 {
                      if(pindex == 0)
                          printf("%04ld\n",ans[endindex]);
                      else
                      {
                          printPoint(ans[endindex],pindex,'m'); 
                          printf("\n");
                      }
                 }
                 else
                     printEnd(ans[endindex]);
                 
            }       
        }      
    } 
    return 0;    
}

