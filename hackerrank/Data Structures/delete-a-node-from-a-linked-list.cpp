/*
  Insert Node at the end of a linked list 
  head pointer input could be NULL as well for empty list
  Node is defined as 

*/
#include<stdlib.h>

struct Node
{
     int data;
     struct Node *next;
};
Node* Delete(Node *head, int position)
{
    int i = 0;
    Node *t = head;
    Node *pre = NULL;
    while(i<position && t!=NULL){
       i++;
       pre = t;
       t = t->next;
	}
	if(head == NULL) return NULL;
	if(t==NULL) return head;
	if(pre==NULL)
 	    head = t->next;
	else
	    pre->next = t->next;
	delete t;
	return head;
}

int main(){
    
}

