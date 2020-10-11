#include <stdio.h>

int main() {
    int a = recursive1(5);
    printf("%d\n",a);
}

int recursive1(int n) {
    printf("%d\n",n);
    if (n<1) 
        return 2;
    else
        return (2* recursive1(n-1) +1);
    
}

// result :
// 5
// 4
// 3
// 2
// 1
// 0
// 95
