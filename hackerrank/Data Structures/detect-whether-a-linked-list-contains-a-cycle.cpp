#include<stdlib.h>
#include<iostream>
using  namespace std;
struct Node
{
     int data;
     struct Node *next;
};
int HasCycle(Node* head)
{
   Node* t1 = head;
   Node* t2 = head;
   while(t1!=NULL && t2!=NULL){
       t1 = t1->next;
	   t2 = t2->next;
	   if(t2!=NULL) 
	       t2 = t2->next;
	   else 
	       return 0;
	   if(t1==t2)
	       return 1; 	  
   }
   return 0;
}
int main(){
	return 0;	
}
