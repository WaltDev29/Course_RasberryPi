// 2026.03.24
// Step Motor 제어 코드를 C언어로 구현

#include <stdio.h>
#include <errno.h>
#include <string.h>

#include <wiringPi.h>
#define STEP_IN1 27
#define STEP_IN2 28
#define STEP_IN3 29
#define STEP_IN4 25

char pinsArray[4] = {STEP_IN1,STEP_IN2,STEP_IN3,STEP_IN4}; 
char signal_full[4][4] = {
    {1, 0, 0, 0},
    {0, 1, 0, 0},
    {0, 0, 1, 0},
    {0, 0, 0, 1}
 };

char FULL_STEP = 4;
int ROTATE_360_STEP = 512; 

void setup_io(void){
    pinMode(STEP_IN1 , OUTPUT);
    pinMode(STEP_IN2 , OUTPUT);
    pinMode(STEP_IN3 , OUTPUT);
    pinMode(STEP_IN4 , OUTPUT);
    digitalWrite(STEP_IN1, LOW);
    digitalWrite(STEP_IN2, LOW);
    digitalWrite(STEP_IN3, LOW);
    digitalWrite(STEP_IN4, LOW);
}


int main ()
{
    if (wiringPiSetup() == -1)
        {
            fprintf (stdout, "oops: %s\n", strerror (errno)) ;
            return 1 ;
        }

    setup_io();
 
    for(int i = 0; i < ROTATE_360_STEP; i++){
        for(int step_idx = 0; step_idx < FULL_STEP; step_idx++){
            for(int idx = 0; idx < 4; idx++){
                digitalWrite(pinsArray[idx], signal_full[step_idx][idx]);
            }
            delay(5);
        }
    }

    for(int i = 0; i < ROTATE_360_STEP; i++){
        for(int step_idx = FULL_STEP-1; step_idx >= 0; step_idx--){
            for(int idx = 0; idx < 4; idx++){
                digitalWrite(pinsArray[idx], signal_full[step_idx][idx]);
            }
            delay(5);
        }
    }

    for (int i=0; i<FULL_STEP; i++) {
        digitalWrite(pinsArray[i], LOW);
    }
    return 0;
}