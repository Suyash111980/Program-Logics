#include <stdio.h>

void num(int n)
{
    if (n == 0)
    {
        return;
    }

    num(n - 1);
    printf("%d ", n);
}

int main()
{
    int num1 = 5;

    num(num1);

    return 0;
}