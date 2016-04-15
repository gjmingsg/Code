/*
  Insert Node at the end of a linked list 
  head pointer input could be NULL as well for empty list
  Node is defined as 

*/

struct Node
{
     int data;
     struct Node *next;
};
Node* Insert(Node *head,int data)
{
    if(head==NULL){
		head = new Node;
		head -> data=data;
		head -> next = NULL;
    }
	else
	{
 	    Node * t = head;
	    Node * pre = t;
     	while(t!=NULL){
 		    pre = t;
	        t = t->next;
        }
        t = new Node;
        t->data=data;
        t->next=NULL;
        pre->next = t;
        
	}
	return head;
}
int main(){
    
}

