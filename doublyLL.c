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
     

     if (head==NULL)
    {
        head=newnode;
        newnode->prev=NULL;
        return;


    }
    struct Node *temp=head;

    while(temp->next!=NULL)
    {
        temp=temp->next;

    }

    newnode->prev=temp;
    temp->next=newnode;

}

void serach(int val)
{
    struct Node *temp=head;
    int count=0;

    while (temp!=NULL)
    {
        count++;
       

        if(temp->data==val)
        {
            printf("\n Data  Found at %d",count);
          
          
            return;
        }
         
        temp=temp->next;
         
       

        
      
    }

    printf("\n Data Not Found ");
    

}



void deletefrombegin()
{
    struct Node *temp=head;

    if (head==NULL)
    {
        printf("\n LIST IS EMPTY");

    }

    if(head->next==NULL)
    {
        head=NULL;
        free(temp);
        return;
    }

    head=temp->next;
    head->prev=NULL;
    free(temp);

    printf("\n Value removed ");
}


void deleteend()
{
    
    
    if (head==NULL)
    {
        printf("\n List is empty");
    }
    struct Node *temp=head;


    if(head->next==NULL)
    {
        head=NULL;
        free(temp);
        return;
    }

    

     while(temp->next!=NULL)
    {
        temp=temp->next;

    }

    //temp=a400

    temp->prev->next=NULL;
    free(temp);
    
    



}

void display()
{
    printf("\n");

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

    display();
    inserttobegin(99);
    display();
    serach(99);
    
    // deletefrombegin();
    // display();
    // deleteend();
    // display();
    // deletefrombegin();   
    // display();
    // deleteend();
    // display();
    // deleteend();
    // display();
    // deletefrombegin();
    // display();
    // deletefrombegin();
    // display();
    // deletefrombegin();
    // display();
    // deletefrombegin();
    // display();


    return 0;
    



}

