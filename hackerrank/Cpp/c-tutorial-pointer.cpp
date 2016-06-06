#include <stdio.h>

void update(int *a,int *b) {
    int t = (*a) + (*b);    
    (*b) =  (*a) - (*b);
    if((*b) < 0)
       (*b) = 0 - (*b);
    (*a) = t;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
