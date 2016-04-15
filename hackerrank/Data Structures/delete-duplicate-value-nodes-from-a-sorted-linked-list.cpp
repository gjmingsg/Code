#include<stdlib.h>
#include<iostream>
using  namespace std;

struct Node
{
    int data;
    struct Node *next;
};

Node* RemoveDuplicates(Node *head)
{
    Node *t = head;
    if(t==NULL)
        return NULL;
    Node *nextp  =  t->next;
    while(nextp!=NULL){

        if(t->data == nextp->data){
            t->next = nextp->next;
            nextp = t->next;
        }else{
            nextp = nextp->next;
            t = t->next;
        }                   
    }
    return head;
};
int main(){

	return 0;	
}
