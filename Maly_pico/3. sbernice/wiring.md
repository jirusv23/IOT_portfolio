# Zapojení úlohy 3 (I2C sběrnice a LCD)

### Potřebné knihovny:
Nahrát do kořene souborového systému na Pico:
- `lcd_api.py`
- `pico_i2c_lcd.py`

### I2C LCD Displej (16x2 s PCF8574 převodníkem):
- **SDA:** GP0 (Pin 1)
- **SCL:** GP1 (Pin 2)
- **GND:** GND (Pin 38)
- **VCC:** VBUS (Pin 40, napájení 5V z USB pro podsvícení a logiku displeje)

### Vstupy úlohy:
1. **Interní teplotní senzor MCU:** vestavěný v čipu RP2040 na interním kanálu ADC 4.
2. **Fyzické tlačítko (volitelné):** GP14 (Pin 19) a GND (s interním PULL_UP).
