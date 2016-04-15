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

node * lca(node * root, int v1,int v2)
{
     if(root!=NULL){
         
         if(root->data < v1 && root->data < v2) 
         {
             if(v1==v2 && root->left->data==v1){
                 return root;  
             }else{
                 return lca(root->left,v1,v2);      
             }
         }             
         else if(root->data > v1 && root->data > v2) {
             if(v1==v2&& root->right->data==v1){
                 return root;  
             }else{
                 return lca(root->left,v1,v2);      
             }
         }
         else
             return root;
     }
     return root;
}


int main(){
	return 0;	
}

