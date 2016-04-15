#include<stdlib.h>
#include<iostream>
using  namespace std;

struct node
{
    int data;
    node* left;
    node* right;
};



void print(node * root, node * cur){
    if(cur!=NULL)
    {
        print(root,root->left);
        cout << root->data << " ";
    }
    if(root==cur){
       while(cur!=NULL){
           cout << cur->data << " ";
           cur = cur -> right;
       }
    }        
}

void top_view(node * root)
{
    print(root,root);
}
int main(){
	return 0;	
}
