from machine import I2C, Pin, ADC
from pico_i2c_lcd import I2cLcd
import utime

# Nastavení I2C sběrnice: GP0 (SDA, Pin 1) a GP1 (SCL, Pin 2)
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

# Běžná I2C adresa pro PCF8574 modul je 0x27 (případně 0x3F)
I2C_ADDR = 0x27
ROWS = 2
COLS = 16

lcd = I2cLcd(i2c, I2C_ADDR, ROWS, COLS)

# Vstup 1: Interní teplotní senzor RP2040 (ADC kanál 4)
sensor_temp = ADC(4)
conversion_factor = 3.3 / 65535

# Vstup 2: Fyzické tlačítko na GP14 s interním pull-up rezistorem
button = Pin(14, Pin.IN, Pin.PULL_UP)

# Úvodní uvítací text
lcd.clear()
lcd.putstr("Hello World!\nI2C LCD Start")
utime.sleep(2)
lcd.clear()

counter = 0

# Hlavní smyčka čtení vstupů a výpisu na LCD
while True:
    # Přepočet napětí na teplotu ve °C pro interní senzor RP2040
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27.0 - (reading - 0.706) / 0.001721
    btn_pressed = (button.value() == 0)

    # 1. řádek: výpis naměřené teploty ze senzoru
    lcd.move_to(0, 0)
    lcd.putstr("Teplota:{:5.1f} C".format(temperature))
    
    # 2. řádek: stav tlačítka a počítadlo času
    lcd.move_to(0, 1)
    if btn_pressed:
        lcd.putstr("Tlacitko: STISK ")
    else:
        lcd.putstr("Cas: {:4d}s | OK ".format(counter))

    counter += 1
    utime.sleep(1)
