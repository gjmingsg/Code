/*
  Insert Node at the end of a linked list 
  head pointer input could be NULL as well for empty list
  Node is defined as 

*/
#include<stdlib.h>
#include<iostream>
using  namespace std;
struct Node
{
     int data;
     struct Node *next;
};
Node* Reverse(Node *head)
{
   if(head==NULL) return NULL;
   Node * t = head;
   Node * pre = NULL;
   Node * next = t->next;
   while(next!=NULL){
       pre = t;
	   t =  next;
	   next = t -> next;
	   t->next = pre;		  
   }
   head->next=NULL;
   head = t;
   return head;
}

int main(){
    
}

