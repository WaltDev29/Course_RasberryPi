#include <stdio.h>
#include <wiringPi.h>
#include <wiringPiI2C.h>

int main(void) {
    int fd;
    int prev, a2dVal[4];
    float a2dVol;
    float Vref = 5.0;

    printf("[ADC/DAC Module testing........]\n");

    // I2C 장치 초기화 (주소: 0x48)
    if ((fd = wiringPiI2CSetup(0x48)) < 0) {
        printf("wiringPiI2CSetup failed\n");
        return -1;
    }

    while (1) {
        // PCF8591에 명령어 전송 (auto increment)
        wiringPiI2CWrite(fd, 0x44);

        // 더미 데이터 (버림)
        prev = wiringPiI2CRead(fd);

        // 4개 채널 데이터 읽기
        for (int i = 0; i < 4; i++) {
            a2dVal[i] = wiringPiI2CRead(fd);
        }

        // ADC0 값을 퍼센트로 변환
        a2dVol = a2dVal[0] * 100.0 / 255;

        printf("VAR = %3.0f %%\n", a2dVol);

        delay(500);
    }

    return 0;
}