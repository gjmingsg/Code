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
Node* InsertNth(Node *head, int data, int position)
{ 	
	int i = 0;
	Node * t = head;
	Node * pre = NULL;
	while(i<position && t!=NULL){
	   i++;
	   pre = t;
	   t=t->next;				 
    }
    if(head==NULL){
		head = new Node;
		head -> data=data;
		head -> next = NULL;
    }
	else
	{
	 	if(pre==NULL){
            pre = new Node;
            pre->next = head;
            head=pre;
	    }
        else{
            pre->next = new Node;
	 	    pre = pre->next;
	 	    pre->next= t;
		}
	 	pre->data=data;
	 	
	}
	return head;
}
int main(){
    
}

