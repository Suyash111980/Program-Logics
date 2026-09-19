#include<stdio.h>
#include<stdlib.h>

struct Node{
    int data;
    struct Node *add;
};

struct Node *head=NULL;// NULL a100 a200 a300 a400

void inserttobegin(int val)
{
    struct Node *newNode=malloc(sizeof(struct Node));//a100
    // new node =a400 head =a300
    newNode -> data=val;//10
    newNode -> add=head;// null

    head=newNode;//head=a100
}

void deletefrombegin()
{
    struct Node *temp=head;

    if(temp==NULL)
    {
        printf("\n List is empty");
    }

    head=temp->add;
    free(temp);

}

void display()
{
    struct Node *temp=head;

    if(head==NULL)
    {
        printf("Linked list is empty");
        return;
    }

    while(temp!=NULL)
    {
        printf("%d -> ",temp->data);
        temp=temp->add;
    }
}


int main()
{

    inserttobegin(10);
    inserttobegin(20);
    inserttobegin(30);
    inserttobegin(40);

    display();

    printf("\n");

    deletefrombegin();
    display();
    

    return 0;
}