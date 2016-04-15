#include<stdlib.h>
#include<iostream>
using  namespace std;
/* you only have to complete the function given below.  
Node is defined as  
*/

struct node
{
    int data;
    node* left;
    node* right;
};


void height_of_bt(node * root,int level,int& max)
{
   if(root!=NULL){
       height_of_bt(root->left,level+1,max);
       height_of_bt(root->right,level+1,max);
   }else{
       max=(max>level?max:level);      
   }
}

int height(node * root)
{
    
    int i = 0;
    height_of_bt(root,0,i);
    return i;
}
int main(){
	return 0;	
}

