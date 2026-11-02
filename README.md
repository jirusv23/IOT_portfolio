# IoT Portfolio – 4.EP

**Autor:** Vojtěch Jiruš  
**Třída:** 4.EP  
**Škola:** SPŠ Trutnov  
**Předmět:** Internet věcí (IoT)  

Portfolio praktických úloh a projektů zaměřených na mikrokontroléry **Raspberry Pi Pico / Pico W** (MicroPython) a jednodeskový počítač **Raspberry Pi 4** (Linux, Python, Flask, GPIO).

---

## Přehled všech úloh

### Část 1: Malé Pico (Raspberry Pi Pico / Pico W – MicroPython)

| Úloha | Název | Popis | Odkaz |
| :--- | :--- | :--- | :--- |
| **0** | **Blinking LED** | Základní blikání vestavěné LED diody na Raspberry Pi Pico. | [Přejít na úlohu 0](./Maly_pico/0.%20blinking_led/) |
| **1** | **Digital I/O** | Ovládání externí LED diody pomocí tlačítka s ošetřením záznějů. | [Přejít na úlohu 1](./Maly_pico/1.%20digital_io/) |
| **2** | **Analog I/O** | Čtení analogové hodnoty potenciometru (ADC na GP26) a PWM řízení frekvence bzučáku (GP27). | [Přejít na úlohu 2](./Maly_pico/2.%20analog_io/) |
| **3** | **Sběrnice (I2C & LCD)** | Komunikace přes I2C s LCD 1602 (PCF8574), čtení interního teplotního senzoru RP2040 a tlačítka. | [Přejít na úlohu 3](./Maly_pico/3.%20sbernice/) |
| **4** | **UART komunikace (Pico <-> Pico)** | Drátový sériový přenos signálu tlačítka mezi dvěma Pico přes UART (TX/RX) se sepnutím LED. | [Přejít na úlohu 4](./Maly_pico/4.%20PRi%20+%20RPi%20KOMUNIKACE/) |
| **5** | **Bezdrátová komunikace (Wi-Fi / UDP)** | Bezdrátový přenos stavu tlačítka mezi dvěma Pico W přes Wi-Fi AP a UDP socket komunikaci. | [Přejít na úlohu 5](./Maly_pico/5.%20RPi%20+%20RPi%20BEZDRAT/) |

---

### Část 2: Velké Pico / Raspberry Pi 4 (Python, Flask, Linux)

| Úloha | Název | Popis | Odkaz |
| :--- | :--- | :--- | :--- |
| **6** | **Digitální I/O & Web server** | Ovládání LED diody fyzickým tlačítkem i přes Flask web s obousměrnou synchronizací stavu. | [Přejít na úlohu 6](./velky_pico/6.%20DIGIT%20LED%20+%20TLAC/) |
| **7** | **Analogové řízení & PWM** | Plynulé řízení jasu LED pomocí rotačního enkodéru a webového slideru (obousměrná live synchronizace). | [Přejít na úlohu 7](./velky_pico/7.%20velky_pico_analog/) |
| **8** | **I2C sběrnice & LCD nástěnka** | Zápis textu z webu na I2C LCD 1602 a fyzické tlačítko na GPIO 17 pro přepínání systémových informací. | [Přejít na úlohu 8](./velky_pico/8.%20velky_pico_sbernice/) |
| **9** | **I2C komunikace (RPi 4 <-> Pico)** | RPi 4 jako I2C Master, Pico jako I2C Slave. Tlačítko na RPi/webu spíná LED na Picu s live zobrazením stavu. | [Přejít na úlohu 9](./velky_pico/9.%20pi4_x_pico_i2c/) |
| **10** | **Wi-Fi REST komunikace (RPi 4 <-> Pico W)** | Pico W jako Wi-Fi AP a HTTP server, RPi 4 odesílá REST příkazy z webu i fyzického tlačítka s live synchronizací. | [Přejít na úlohu 10](./velky_pico/10.%20pi4_x_pico_wifi/) |

---

## Struktura repozitáře

```text
IOT_portfolio/
├── README.md                          # Hlavní přehled portfolia
├── pinout.svg                         # Schéma pinoutu Raspberry Pi Pico
├── Maly_pico/                         # Úlohy na Raspberry Pi Pico / Pico W
│   ├── 0. blinking_led/               # Úloha 0: Blikání LED
│   ├── 1. digital_io/                 # Úloha 1: Tlačítko a LED
│   ├── 2. analog_io/                  # Úloha 2: Potenciometr a piezo bzučák
│   ├── 3. sbernice/                   # Úloha 3: I2C LCD displej a senzor
│   ├── 4. PRi + RPi KOMUNIKACE/       # Úloha 4: Drátová UART komunikace 2x Pico
│   └── 5. RPi + RPi BEZDRAT/          # Úloha 5: Bezdrátová UDP komunikace 2x Pico W
└── velky_pico/                        # Úlohy na Raspberry Pi 4
    ├── 6. DIGIT LED + TLAC/           # Úloha 6: Tlačítko, LED a Flask server
    ├── 7. velky_pico_analog/          # Úloha 7: Rotační enkodér, PWM a slider
    ├── 8. velky_pico_sbernice/        # Úloha 8: I2C LCD a tlačítko na RPi 4
    ├── 9. pi4_x_pico_i2c/             # Úloha 9: I2C Master (RPi) <-> Slave (Pico)
    └── 10. pi4_x_pico_wifi/           # Úloha 10: Wi-Fi REST API RPi 4 <-> Pico W
```
