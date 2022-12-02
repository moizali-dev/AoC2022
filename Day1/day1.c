#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void part1() {
    // declar variables
    char value[6];
    int intvalue;
    int total_cals = 0;
    int maxcals = 0;

    // declare pointer
    FILE *in;

    // initialize pointer
    in = fopen("input.txt", "r");

    // loop
    while (!feof(in)) {
        fgets(value, sizeof(value), in);
        if (strcmp(value,"") == 10) {
            
            if (total_cals >= maxcals){
                maxcals = total_cals;
            }
            total_cals = 0;
        } else {
            intvalue = atoi(value);
            total_cals += intvalue;
        }

    }

    printf("How many total Calories is that Elf carrying? %d\n", maxcals);
}

void part2() {

    // declar and init vars
    int total_cals = 0;
    char value[6];
    int intvalue = 0;
    int elf1 = 0;
    int elf2 = 0;
    int elf3 = 0;
    // int top_3_elves = 0;
    
    // declare pointer
    FILE *in;

    // initialize pointer
    in = fopen("input.txt", "r");

    // Loop through File
    while(!feof(in)) {
        fgets(value, sizeof(value), in);

        if (strcmp(value,"") == 10) {
            total_cals = 0;
        } else {
            intvalue = atoi(value);
            total_cals += intvalue;
        }

        if (total_cals > elf1) {
            elf3 = elf2;
            elf2 = elf1;
            elf1 = total_cals;
        } else if ( total_cals > elf2) {
            elf3 = elf2;
            elf2 = total_cals;
        } else if ( total_cals > elf3) {
            elf3 = total_cals;
        }

    }

    printf("How many Calories are those Elves carrying in total? %d\n", elf1 + elf2 + elf3);

}

int main(void) {

    part1();
    part2();

}