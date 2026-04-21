from i2c_class import read_i2c
from i2c_class import write_i2c
import RPi_I2C_driver
import time

RED_LED = 0b00000001
GREEN_LED = 0b00000010
BLUE_LED = 0b00000100
RELAY_1 = 0b00010000
RELAY_2 = 0b00100000

textLcd = RPi_I2C_driver.lcd()

# LCD 표시
textLcd.lcd_display_string("2501110203", 1)

try:
    adc = read_i2c()
    write = write_i2c()
    while True:
        psd_value = adc.psd_read()
        print(f"Distance: {psd_value} cm")
        
        # LCD 표시
        textLcd.lcd_display_string(str(psd_value) + "cm", 2)

        # LED 표시
        if psd_value < 20 or psd_value > 100:
            write.on(RED_LED | GREEN_LED | BLUE_LED)
            time.sleep(0.1)
            write.off(RED_LED | GREEN_LED | BLUE_LED)

        elif psd_value >= 20 and psd_value <= 30:
            write.on(RED_LED)
            write.off(GREEN_LED | BLUE_LED)

        elif psd_value >= 31 and psd_value <= 50:
            write.on(GREEN_LED)
            write.off(RED_LED | BLUE_LED)

        elif psd_value >= 51 and psd_value <= 100:
            write.on(BLUE_LED)            
            write.off(RED_LED | GREEN_LED)

        time.sleep(0.05)

except KeyboardInterrupt:
    textLcd.lcd_clear()
    print("Program Stopped")