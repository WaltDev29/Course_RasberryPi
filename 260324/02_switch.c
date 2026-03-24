#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <wiringPi.h>

#define SW1_PIN 7
#define SW2_PIN 0
#define SW3_PIN 1
#define SW4_PIN 3



void setup_io(void){
    pinMode(SW1_PIN, INPUT);
    pinMode(SW2_PIN, INPUT);
    pinMode(SW3_PIN, INPUT);
    pinMode(SW4_PIN, INPUT);
}



int main ()
{
    if (wiringPiSetup () == -1)
    {
        fprintf (stdout, "oops: %s\n", strerror
        (errno)) ;
        return 1 ;
    }
    setup_io();
    for (;;) {
        printf("Button State: %d %d %d %d \n", 
        digitalRead(SW1_PIN), digitalRead(SW2_PIN), 
        digitalRead(SW3_PIN), digitalRead(SW4_PIN));
    }
    return 0;
}