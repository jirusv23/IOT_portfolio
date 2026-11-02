# Zapojení úlohy 8 (I2C sběrnice a LCD na Raspberry Pi 4)

### I2C LCD Displej (16x2 s PCF8574 převodníkem):
- **GND:** Pin 6 (GND)
- **VCC:** Pin 2 (5V)
- **SDA:** Pin 3 (GPIO 2, I2C1 SDA)
- **SCL:** Pin 5 (GPIO 3, I2C1 SCL)

### Fyzický vstup (Tlačítko):
- **Tlačítko:** Pin 11 (GPIO 17) a Pin 9 (GND) – s interním pull-up rezistorem
*(Stisk tlačítka přepíná režim zobrazení: uživatelský text / systémové informace a čas).*
