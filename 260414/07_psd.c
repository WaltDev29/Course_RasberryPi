#include <stdio.h>
#include <wiringPi.h>
#include <wiringPiI2C.h>

int main(void) {
    int fd;
    int prev, a2dVal[4];
    float psd_value;
    float range;

    printf("[ADC/DAC Module testing........]\n");

    // I2C 초기화
    if ((fd = wiringPiI2CSetup(0x48)) < 0) {
        printf("wiringPiI2CSetup failed\n");
        return -1;
    }

    while (1) {
        // 명령어 전송
        wiringPiI2CWrite(fd, 0x44);

        // 더미 데이터 버림
        prev = wiringPiI2CRead(fd);

        // ADC 값 읽기
        for (int i = 0; i < 4; i++) {
            a2dVal[i] = wiringPiI2CRead(fd);
        }

        // ADC3 → PSD 센서
        psd_value = (a2dVal[3] / 255.0 * 3.3) * 3 / 2;

        // 거리 계산 (보정 공식)
        if (psd_value > 0.228) {   // 0으로 나누는 것 방지
            range = 19.8 / (psd_value - 0.228);
            printf("range = %3.0f cm\n", range);
        } else {
            printf("range = out of range\n");
        }

        delay(50);
    }

    return 0;
}