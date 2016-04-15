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



void Inorder(node *root) {
	 if(root==NULL) return;

	 Postorder(root->left);
	 cout << root->data << " ";
	 Postorder(root->right);

}

int main(){
	return 0;	
}

