#include<stdlib.h>
#include<iostream>
using  namespace std;
struct Node
{
     int data;
     struct Node *next;
};
Node* MergeLists(Node *headA, Node* headB)
{
   Node *ta = headA;
   Node *tb= headB;
   Node *t = NULL;
   Node *head = new Node();
   t = head;
   while(ta!=NULL && tb!=NULL){
      if(ta->data < tb->data){
          t->next = ta;
          ta = ta->next;
          t = t->next;
      }else{
          t->next = tb;
          tb = tb->next;
          t = t->next;      
      }
   }
   if(ta==NULL)
       t->next = tb;
   if(tb==NULL)
       t->next = ta;
   return head->next;
}

int main(){
    
	return 0;	
}

