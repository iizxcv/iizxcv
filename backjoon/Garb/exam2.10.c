#include <stdio.h>

void inplace_swap(int *x, int *y) {
    *y = *x ^ *y;
    *x = *x ^ *y;
    *y = *x ^ *y;
}

int main() {
    int a = 1;
    int b = 2;
    printf("%d\n", *pa); // 교환전 값 출력
    printf("%d\n", *pb); // 교환전 값 출력

    int *pa = &a;
    int *pb = &b;
    inplace_swap(pa, pb);
    printf("%d\n", *pa); // 값 출력
    printf("%d\n", *pb); // 값 출력
    printf("%p\n", (void*)pa); // 주소 출력
    printf("%p\n", (void*)pb); // 주소 출력
    return 0;
}