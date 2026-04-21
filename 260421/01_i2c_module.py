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

textLcd.lcd_display_string("KOPO AISW", 1)
textLcd.lcd_display_string("I2C_BUS TEST", 2)

adc = read_i2c()
write = write_i2c()

print(f"VR: {adc.vr_read()} %")
print(f"CdS: {adc.cds_read()} %")
print(f"GAS: {adc.gas_read()} GAS")
print(f"Distance: {adc.psd_read()} cm")

textLcd.lcd_display_string(
    str(round(adc.vr_read(),2)) + "% " + str(round(adc.cds_read(),2)) + "%",
    2
)

write.on(RED_LED)
time.sleep(0.5)

write.on(GREEN_LED)
time.sleep(0.5)

write.on(BLUE_LED)
time.sleep(0.5)

write.off(RED_LED | GREEN_LED | BLUE_LED)
time.sleep(0.5)

write.on(RELAY_1 | RELAY_2)
time.sleep(0.5)

write.off(RELAY_1 | RELAY_2)
time.sleep(0.5)