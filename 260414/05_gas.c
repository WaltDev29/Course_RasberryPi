#include <stdio.h>
#include <wiringPi.h>
#include <wiringPiI2C.h>

int main(void) {
    int fd;
    int prev, a2dVal[4];

    printf("[ADC/DAC Module testing........]\n");

    // I2C 초기화 (주소: 0x48)
    if ((fd = wiringPiI2CSetup(0x48)) < 0) {
        printf("wiringPiI2CSetup failed\n");
        return -1;
    }

    while (1) {
        // 명령어 전송
        wiringPiI2CWrite(fd, 0x44);

        // 더미 데이터 (버림)
        prev = wiringPiI2CRead(fd);

        // 4채널 데이터 읽기
        for (int i = 0; i < 4; i++) {
            a2dVal[i] = wiringPiI2CRead(fd);
        }

        // ADC2 값 (가스 센서)
        printf("GAS = %d\n", a2dVal[2]);

        delay(500);
    }

    return 0;
}