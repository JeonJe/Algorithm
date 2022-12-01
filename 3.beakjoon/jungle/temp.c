#include <stdio.h>
#include <stdlib.h>
int main()
{

  int arr[2][3] = {{1, 2, 3}, {4, 5, 6}};
  int (*parr)[3];

  parr = arr;

  printf("parr[1][1] : %d \n", parr[0][1]);  // 버그!
    printf("%p\n",parr);
    printf("%p\n",(parr+1));
    printf("%d\n",**   (parr+1));
    // printf("%p\n",(parr+1));
    // printf("%p\n",(parr+1));
    // printf("%p\n",(parr+1));
  return 0;

}