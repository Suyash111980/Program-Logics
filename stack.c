#include <stdio.h>
#define max 10

int stack[max];
int top=-1;

void push(int val)
{
    if(top==max-1)
    {
        printf("Stack overflow");
        return;
    }

    stack[++top]=val;
    printf("value added");
}

void pop(int val)
{
    if(top==-1)
    {
        printf("stack empty");
        return;
    }

    printf("removed %d",stack[top]);
    top--;
}

void peek()
{
    printf("\n Top Element %d",stack[top]);
}

void display()
{
    int i;

    if(top==-1)
    {
        printf("stack empty");
        return;
    }

    for(i=top;i>=0;i--)
    {
        printf("%d ->",stack[i]);
    }
}



int main()
{
    push(10);
    push(20);
    push(30);
    push(40);
    display();
    peek();
    


    return 0;
}