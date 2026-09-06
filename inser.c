#include<stdio.h>
int main ()
{
    int arr[]={10,9,8,7,6,5,4,3,2,1};
    int len=10;
    int i,j;
    

    for(i=0;i<len;i++)
    {
        printf("%5d",arr[i]);
    }

    printf("\n");

    

    for(i=1;i<len;i++)
    {
       int key = arr[i];
         for(j=i-1;j>=0 && key < arr[j];j--)
         {
            arr[j+1]=arr[j];

         }

         arr[j+1]=key;
    }

    for(i=0;i<len;i++)
    {
        printf("%5d",arr[i]);
    }


    return 0;
}