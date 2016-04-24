#include<stdlib.h>
#include<iostream>
using  namespace std;

struct Node
{
     int data;
     Node *next;
     Node *prev;
};
Node* Reverse(Node* head)
{
    
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

    cin>>i;
    return 0;
}
