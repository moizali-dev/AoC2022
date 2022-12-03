#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void part1() {

    // create struct similar to dict
    typedef struct RockPaperScissor {
        char input[4];
        int result;
    } RockPaperScissor;

    // adding dict to list
    RockPaperScissor RPS_List[9] = {
        {"A Z", 3}, {"B X", 1}, {"C Y", 2}, // Losses  
        {"A X", 4}, {"B Y", 5}, {"C Z", 6}, // Ties  
        {"A Y", 8}, {"B Z", 9}, {"C X", 7} // Wins  
    };

    //declare input
    char input[4];
    int score = 0;

    // declare pointer
    FILE *in;

    // init pointer
    in = fopen("day2input.txt", "r");

    // Read through input
    while(!feof(in)) {
        fgets(input, sizeof(input), in);

        for (int i = 0; i < 9; i++){
            if (strcmp(input, RPS_List[i].input) == 0){
                score += RPS_List[i].result;
            }
        }
        
    }

    printf("%d\n", score);

}

void part2() {

    typedef struct RockPaperScissor {
        char input[4];
        int result;
    } RockPaperScissor;

    RockPaperScissor RPS_List[9] = {
        {"A X", 3},
        {"B X", 1},
        {"C X", 2},
        {"A Y", 4},
        {"B Y", 5},
        {"C Y", 6},
        {"A Z", 8},
        {"B Z", 9},
        {"C Z", 7}  
    };

    char input[4];
    FILE *in;
    int score = 0;

    in = fopen("day2input.txt", "r");

    while(!(feof(in))) {
        fgets(input, sizeof(input), in);
        // printf("%s", input);
        for (int i = 0; i < 9; i++){
            if (strcmp(input, RPS_List[i].input) == 0){
                score += RPS_List[i].result;
            }
        }
    }

    printf("%d\n", score);

}

int main(void) {
    part1();
    part2();
}