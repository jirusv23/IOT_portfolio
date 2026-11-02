from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd
import utime

# Set up I2C on Pin 0 (SDA) and Pin 1 (SCL)
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

# The most common I2C address for these displays is 0x27 or 0x3F
I2C_ADDR = 0x27
ROWS = 2
COLS = 16

lcd = I2cLcd(i2c, I2C_ADDR, ROWS, COLS)

lcd.clear()
lcd.putstr("Hello World!")
utime.sleep(2)
lcd.clear()
lcd.putstr("I2C is working!")