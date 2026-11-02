from machine import Pin
import utime

LED_PIN_NUMBER = 15
BTN_PIN_NUMBER = 16

LED_PIN = Pin(LED_PIN_NUMBER, Pin.OUT)
BTN_PIN = Pin(BTN_PIN_NUMBER, Pin.IN, Pin.PULL_UP)

led_state = False
last_btn_state = BTN_PIN.value()

while True:
    current_btn_state = BTN_PIN.value()

    if current_btn_state == 0 and last_btn_state == 1:
        led_state = not led_state     
        LED_PIN.value(led_state)      
        utime.sleep(0.2)              
        
    last_btn_state = current_btn_state