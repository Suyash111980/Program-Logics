#include<stdio.h>
int getMax(int arr[], int len)
{
    int max=arr[0];
    for(int i=0;i<len;i++)
    {
        if(arr[i]>max)
        {
            max=arr[i];
        }
    }

    return max;
}

void countingsort(int arr[],int len)
{
    //find max element 
    int max=getMax(arr,len);

    //create count array 
    int count[max+1];
    
    //intialize zero
    for(int i=0;i<max+1;i++)
    {
        count[i]=0;
    }

    //store count of original digit
    for(int i=0;i<len;i++)
    {
        count[arr[i]]++;
        //count[9]++ // suppose the value is 9 then it will go to 9th index of count array and it will increment the value from 0 to 1 this indicate that the number is present in the original array 

        //update OG array
        
       
    } 
    
    
    int index=0;// iterate og array
    int i=0;//  count array

        
    for( int i=0 ;i<max+1;i++)
    {
           while(count[i]>0)
           {
                arr[index]=i;
                count[i]--;
                index++;
           } 
            
    }
    

}

void display(int arr[],int len)
{
    for(int i=0;i<len;i++)
    {
        printf("%5d",arr[i]);
    }
}









int main()
{
    int arr[]={2,9,4,5,1,7,2};
    int len=7;
    printf("\nBefore Sorting");
    display(arr,len);
    countingsort(arr,len);
    printf("\nAfter Sorting");
    display(arr,len);

}