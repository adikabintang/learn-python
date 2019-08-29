/*
https://renenyffenegger.ch/notes/development/languages/C-C-plus-plus/GCC/create-libraries/index
gcc -c -fPIC mylib.c -o mylib.o
ar rcs libmylib.a mylib.o
 */
#include "mylib.h"
#include <stdio.h>

void help()
{
    printf("aaa help meee\n");
}