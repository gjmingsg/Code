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
void ReversePrint(Node *head)
{
   if(head==NULL)
      return;
   else{
       ReversePrint(head->next);
	   cout << head->data << "\n"; 		
   }
}

int main(){
    
}

