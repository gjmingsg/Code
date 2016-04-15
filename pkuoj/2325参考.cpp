#include <iostream>
#include <cstring>
using namespace std;
void copy(int b[1001],char str[1001]);
int main()
{
	char str[1001];
	int x=0,b[1001],a[10000],c[10000],stack[10],b_count =0,a_count = 0,c_count = 0;
	int i,j,m,len;
	while(cin>>str &&strcmp("-1",str)!=0)
	{
		memset(stack,0,sizeof(stack));
		b_count =0,a_count = 0,x=0,c_count = 0;
		len = strlen(str);
		c_count = len;
		if(len == 1)
		{
			cout<<"1"<<str<<endl;
			continue;
		}
		copy(b,str);
		copy(c,str);
		for(i = 9;i>1;i--)
		{	
			while(b_count<len)
			{
				x = x*10 + b[b_count++];
				if(x<i && b_count<len)
				{
					if(a_count)
						a[a_count++] = 0;//此处为一位不够除时加零
					x = x*10 +b[b_count++];
				}
			
				a[a_count++] = x/i;
				x = x%i;
				if(b_count>=len &&x==0)//当可以被当前的数除尽时
				{
					memset(b,0,sizeof(b));
					for(j= 0;j<a_count;j++)//由c数组保存中间数
					{
						c[j] = a[j];
						b[j] = a[j];
					}
					c_count = a_count;
					len = a_count;
					stack[i]++;
					i++;
				
					if(a_count==1)
					{
						stack[a[0]]++;
						i=0;
						break;
					}
					b_count = 0;
					a_count = 0;
					memset(a,0,sizeof(a));
					x = 0;
					break;
				}
				else
					if(b_count >=len &&x!=0)//当不可以被当前的数除尽时
					{
						if(i == 2)//当已经除到最后还无法除尽时就判定无这种数
						{
							memset(stack,0,sizeof(stack));
							cout<<"There is no such number.";
							continue;
						}	
						memset(b,0,sizeof(b));
						for(m = 0;m<c_count ;m++)
							b[m] = c[m];
						len = c_count;
						b_count = 0;
						a_count = 0;
						x = 0;
						memset(a,0,sizeof(a));
						break;
					}
			}
		}

		for(i = 2;i<=9;i++)//输出
			for(j =0;j<stack[i];j++)
				cout<<i;
		cout<<endl;
		}
	return 0;
}
void copy(int b[1001],char str[1001])
{
	for(int i = 0;i<strlen(str); i++)
		b[i] = str[i]-'0';
}


