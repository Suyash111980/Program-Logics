#include<stdio.h>
#include<stdlib.h>

struct Node{
    int data;
    struct Node *next;
    struct Node *prev;
};

struct Node *head=NULL;

void inserttobegin(int val)
{
    struct Node  *newnode = malloc(sizeof(struct Node));

    newnode->data=val;
    newnode->next=head;
    newnode->prev=NULL;

    if (head!=NULL)
    {
        head->prev=newnode;
    }

    head=newnode;

}

void inserttoend (int val)//20
{
     struct Node  *newnode = malloc(sizeof(struct Node));

     newnode->data=val;
     newnode->next=NULL;
     newnode->prev=head;

     if (head!=NULL)
    {
        head->next=newnode;
    }

    head=newnode;

}

void deletefrombegin()
{
    struct Node *temp=head;

    if (head==NULL)
    {
        printf("\n LIST IS EMPTY");

    }

    head=temp->next;
    head->prev=NULL;
    free(temp);

    printf("\n Value removed ");
}


void display()
{
    

    if(head==NULL)
    {
        printf("LIST IS EMPTY");
        return;
    }

   struct Node *temp=head;

   while (temp!=NULL)
   {
    printf("%d ->",temp->data);
    temp=temp->next;
   }
}

void display1()
{
    

    if(head==NULL)
    {
        printf("LIST IS EMPTY");
        return;
    }

   struct Node *temp=head;

   while (temp!=NULL)
   {
    temp=temp->prev;
    printf("\n Insert to end");
    printf("\n %d ->",temp->data);
    
   }
}

int main()
{
    // inserttobegin(10);
    // inserttobegin(20);
    // inserttobegin(30);
    // inserttobegin(40);
    // display();
    // deletefrombegin();
    // deletefrombegin();
    // display();

    inserttoend(10);
    inserttoend(20);
    inserttoend(30);
    inserttoend(40);

    display1();

    return 0;
    



}

