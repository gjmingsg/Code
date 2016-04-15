#include <cstdlib>
#include <iostream>

using namespace std;

const int maxn=16;

int map[maxn][maxn];
int mark[maxn][maxn];
bool visit[maxn*4+5];

int main(void)
{
    int n,t=1;
    while(scanf("%d",&n)==1)
    {
        if(n==0) break;
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++)
                mark[i][j]=2;        
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++)
                scanf("%d",&map[i][j]);
        printf("Case %d:\n\n",t);
        for(int i=1;i<=4*n+3;i++)
        {
            printf("*");
        }
        printf("\n");
        for(int i=1;i<=4*n-3;i++)
        {
            for(int j=0;j<=4*n+1;j++)
                visit[j]=false;    
            printf("*");
            if(i%4==1)
            {
                for(int j=1;j<=4*n+1;j++)
                {
                    if(j%4==1)
                    {
                        printf("H");
                        if(visit[j-1])
                            visit[j]=true;
                    }           
                    if(j%4==3)
                    {
                        printf("O");
                        if(visit[j-1])
                            visit[j]=true;
                    }
                    if(j==2)
                    {
                        printf("-");
                        visit[1]=true;
                        visit[2]=true;
                    }
                    else if(j%4==2)
                    {
                        if(map[(i-1)/4+1][(j-1)/4+1]==-1)
                            printf(" "); 
                        else if(map[(i-1)/4+1][(j-1)/4+1]==1)
                        {
                            printf("-");
                            visit[j-1]=true;
                            visit[j]=true;
                            visit[j+1]=true;
                        }                          
                        else if(visit[j-1])
                            printf(" ");
                        else
                        {
                             printf("-");
                             visit[j-1]=true;
                             visit[j]=true;
                             visit[j+1]=true;
                        }
                    }
                    else if(j%4==0)
                    {
                        if(map[(i-1)/4+1][j/4]==-1)
                            printf(" "); 
                        else if(map[(i-1)/4+1][j/4]==1)
                        {
                            printf("-");
                            visit[j]=true;
                        }
                        else if(!visit[j-1])
                        {
                            printf("-");
                            visit[j-1]=true;
                            visit[j]=true;
                        }
                        else printf(" ");  
                    }                                          
                }
                for(int j=1;j<=n;j++)
                {
                    if(map[(i-1)/4+1][j]==1) mark[(i-1)/4+1][j]=0;
                    else if(map[(i-1)/4+1][j]!=-1) mark[(i-1)/4+1][j]--;
                }                                      
            }
            else if(i%4==2)
            {
                for(int j=1;j<=4*n+1;j++)
                {
                    if(j%4==3)
                    {
                        if(mark[(i-1)/4+1][(j-1)/4+1]!=0)      
                            printf("|");
                        else printf(" ");
                    }
                    else printf(" ");
                }                       
            }
            else if(i%4==3)
            {
                for(int j=1;j<=4*n+1;j++)
                {      
                    if(j%4==3) printf("H");
                    else printf(" ");
                }
            }
            else if(i%4==0)
            {
                for(int j=1;j<=4*n+1;j++)
                {
                    if(j%4==3&&mark[(i-1)/4+1][(j-1)/4+1]==0)
                    {        
                        printf("|");
                        mark[i/4+1][(j-1)/4+1]--;
                    }
                    else printf(" ");
                }
            }                         
            printf("*\n");
        }                   
        for(int i=1;i<=4*n+3;i++)
        {
            printf("*");
        }
        printf("\n\n");
        t++;
    }                                                             
    return 0;
}
