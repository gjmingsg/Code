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



void LevelOrder(node * root)
{
   node *queue[100];
   int length = 1,top=0,bottom=0;
   
   queue[0] = root;
   while(length>0){
       top = top%100;
       bottom=bottom%100;
       node * t = queue[bottom];
       if(t!=NULL){
           cout << t->data << " ";
           length--;
           bottom++;
       }
       if(t->left!=NULL){
           queue[++top] = t->left;
           length++;       
       }
       if(t->right!=NULL){
           queue[++top] = t->right;
           length++;
       }
   }
}
int main(){
	return 0;	
}

