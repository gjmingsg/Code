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


node * insert(node * root, int value)
{
   node * t = root, * pre=NULL;
    if(root==NULL){
        root=new node();
        root->data = value;
        root->left=NULL;
        root->right=NULL;
        return root;               
    }
    
   while(t!=NULL){
       pre = t;
       if(t->data<value)
          t=t->right;
       else if(t->data>value)
          t=t->left;
       else
          break; 
   } 
   if(t==NULL){
       t = new node();
       t->left = NULL;
       t->right = NULL;
       t->data = value;
       if(pre->data>value)
           pre->left = t;
       else
           pre->right = t;
   }
   return root;
}

int main(){
	return 0;	
}

