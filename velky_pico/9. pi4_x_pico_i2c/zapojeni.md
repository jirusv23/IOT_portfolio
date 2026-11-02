I2C propojení (Velké RPi 4 <-> Malé Pico)
- GND (Zem): RPi 4 Pin 6 -> Pico Pin 38 (GND)
- SDA (Data): RPi 4 Pin 3 (GPIO 2) -> Pico Pin 1 (GP0)
- SCL (Hodiny): RPi 4 Pin 5 (GPIO 3) -> Pico Pin 2 (GP1)

Fyzické tlačítko na RPi 4: Jeden pin tlačítka do GPIO 17 (Pin 11), druhý pin tlačítka do GND (Pin 9).

LEDka na Picu: Kladná nožička (delší) na GP15 (Pin 20) -> rezistor (cca 220 Ohmů) -> záporná nožička do GND (Pin 23).