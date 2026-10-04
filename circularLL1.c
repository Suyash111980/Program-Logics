#include <stdio.h>
#include <stdlib.h>
struct  node
{
    int data;
    struct node *add;
};

struct node *head = NULL;

void inserttoend(int val)
{
    struct node *newnode=malloc(sizeof(struct node));

    newnode->data=val;
    newnode->add=head;

    if(head==NULL)
    {
        head=newnode;  
        newnode->add=head;
        return;

    }
    
    

    struct node *temp=head;

    while(temp->add!=head)
    {
        temp=temp->add;
    } 

    temp->add=newnode;

}




void deletefromend()
{
    struct node *temp=head;
    if(head == NULL)
    {
        printf("Linked list is empty");
        return;
    }

     if(head->add==head)
    {
        head=NULL;
       
        return;
    }
     
    while (temp->add->add!=head)
    {
        temp = temp->add;

    }
    free(temp->add);
    temp->add = head;
    
}

void insertbegin(int val)
{
    struct node *newnode =malloc(sizeof(struct node));
    newnode->data=val;
    newnode->add=NULL;
    if(head==NULL)
    {
        head=newnode;
        newnode->add=head;
        return;
    }

    newnode->add=head;
    struct node *temp=head;

    while(temp->add != newnode->add)
    {
        temp=temp->add;
    }

    temp->add=newnode;
    head=newnode;

}


void deletefrombegin()
{
    struct node *temp=head;
    struct node *oldtemp=head;

    if (head==NULL)
    {
        printf("\n LIST IS EMPTY");

    }

    if(head->add==head)
    {
        head=NULL;
       
        return;
    }
     
  while(temp->add!=head)// 
    {
        temp=temp->add;
    }

    oldtemp=head;

    head=head->add;
    temp->add=head;
    free(oldtemp);

    printf("\n Value removed");
   

}

void display()
{
        struct node *temp=head;

        if(head==NULL)
        {
            printf("Linked list is empty ");
            return;
        }

        while (temp->add!=head)
        {
            printf("%d->\t",temp->data);
            temp=temp->add;
        }
        printf("%d->\t\n",temp->data);
    

}


int main()
{

    insertbegin(10);
    insertbegin(20);
    insertbegin(30);
    insertbegin(40);
    display();
    deletefrombegin();
    display();
     deletefrombegin();
    display();
     deletefrombegin();
    display();
     deletefrombegin();
    display();
    // inserttoend(10);
    // inserttoend(20);
    // inserttoend(30);
    // inserttoend(99);
    // display();
    // deletefromend();
    // display();
    // deletefromend();
    // display();
    // deletefromend();
    // display();
    // deletefromend();
    // display();
    return 0;
}