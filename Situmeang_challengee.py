#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#Program that calculates the type of triangle
int main(int argc, char *argv[]) {

    int x,y,z,longest;

    printf("Type in the integer lengths of 3 sides of a triangle:\n");
    scanf("%d %d %d", &x, &y, &z); //reads the user's inputs
    if((x<=0) || (y<=0) || (z<=0)) {
      printf("This is not a triangle.\n");
    } else {
        if((x + y <= z) || (x + z <= y) || (y + z <= x)) {
        printf("This is not a triangle.\n");
        } else {

            longest = z;
            if (longest < x) {
                z = longest;
                longest = x;
                x = z;
            }
            if (longest < y) {
                z = longest;
                longest = y;
                y = z;
            }

            if( x * x + y * y == longest * longest ) {
                printf("This is a right-angled triangle.\n");
            } else if( x * x + y * y > longest * longest) {
                printf("This is an acute-angled triangle.\n");
            } else printf("This is an obtuse-angled triangle.\n");
        }
  }

  return 0;
}