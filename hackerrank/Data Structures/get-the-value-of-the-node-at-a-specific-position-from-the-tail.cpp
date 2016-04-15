#include<stdlib.h>
#include<iostream>
using  namespace std;
struct Node
{
     int data;
     struct Node *next;
};
int GetNode(Node *head,int positionFromTail)
{
   //if(head==NULL) return NULL;
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
   while(positionFromTail>0){
       positionFromTail --;
       t=t->next;
   }
   return t->data;
}
int main(){
	return 0;	
}
