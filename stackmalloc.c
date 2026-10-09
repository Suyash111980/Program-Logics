#include<stdio.h>
#include<stdlib.h>

struct Node {
    int data;
    struct Node *add;
};

struct Node *top=NULL;


void push(int val)
{
    struct Node *newnode=malloc(sizeof(struct Node));

    newnode->data=val;
    newnode->add=top;


    top=newnode;
}

void pop()
{
    if(top==NULL)
    {
        printf("\n Stack is empty ");
    }

    struct Node *temp=top;

    top=top->add;
    free(temp);
}


void peek()
{
    printf("\n Top Element %d",top->data);
}

void display()
{
    if(top==NULL)
    {
        printf("\n Stack is empty ");
    }

     struct Node *temp=top;
     while(temp!=NULL)
     {
        printf("%d ->",temp->data);
        temp=temp->add;
     }

     printf("\n");



}


int main()
{
    push(10);
    push(20);
    push(30);
    push(40);
    display();
    pop();
    display();
}