#include<stdlib.h>
#include<iostream>
using  namespace std;
struct Node
{
     int data;
     struct Node *next;
};
int CompareLists(Node *headA, Node* headB)
{
 	while(headA!=NULL && headB!=NULL){
       if(headA->data==headB->data){
           headA=headA->next;
           headB=headB->next;
	   }
	   else
	       return 0;
    }
    if(headA==NULL && headB==NULL) 
	    return 1;
    else 
	    return 0;
}
int main(){
	return 0;	
}
