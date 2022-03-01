#include <stdio.h>
#include <stdlib.h>

int icount = 1; // default value

int sum(int a, int b){
          return a+b;
}

main(int argc, char *argv[])
{
          int i=1;

                while (1) {
                            printf("%d\n", i);
                                i=sum(i,1);
                            sleep(2);
                                          }

                  printf("Finished\n");
                    return 0;
}
