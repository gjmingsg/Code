#include<stdlib.h>
#include<iostream>
using  namespace std;

struct Node
{
     int data;
     Node *next;
     Node *prev;
};
Node* SortedInsert(Node *head,int data)
{
    Node *t = head;
    Node *pre = head;
    Node *temp = NULL;
    if(head==NULL){
       head = new Node();    
       head->data = data;
       head->next = NULL;
       head->prev = NULL;
       return head;
    }
    while((t != NULL) && (t->data <= data)) {
        pre = t;
        t = t->next;
    }
    temp = new Node();
    temp->data = data;
    if(head==t){
        head = temp;
        head->next = t;
        head->prev=t->prev;
        t->prev = head;
    }else{
        pre->next = temp;
        temp->prev = pre;
        temp->next = t;
    }
    if(t!=NULL)
        t->prev = temp;
    return head;
}
int print(Node *head){
   while(head!=NULL){
      cout << head -> data << "->"; 
      head=head->next;
   }
   cout << endl;
}
int main(){
    int i;
    Node *head = NULL;
    head = SortedInsert(head,1);
    print(head);
    head = SortedInsert(head,4);
    print(head);
    head = SortedInsert(head,2);        
    print(head);
    head = SortedInsert(head,3);
    print(head);
    head = SortedInsert(head,7);
    print(head);
    head = SortedInsert(head,6);
    print(head);
    head = SortedInsert(head,9);
    print(head);
    head = SortedInsert(head,10);
    print(head);
    cin>>i;
    return 0;
}
