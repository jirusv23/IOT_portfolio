from machine import Pin, ADC, PWM
import utime

def translate(value: float, leftMin: float, leftMax: float, rightMin: float, rightMax: float) -> float:
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)

POT_PIN_NUMBER = 26
POT_ADC = ADC(Pin(POT_PIN_NUMBER))

POT_MIN_VALUE = 0
POT_MAX_VALUE = 65535

BUZZER_PIN_NUMBER = 27
BUZZER_PIN = PWM(Pin(BUZZER_PIN_NUMBER, Pin.OUT))

BUZZER_PIN.duty_u16(32768)

while True:
    pot_value = POT_ADC.read_u16()
    
    buzzer_freq = translate(pot_value, POT_MIN_VALUE, POT_MAX_VALUE, 200.0, 2000.0)
    buzzer_freq = int(max(200.0, min(buzzer_freq, 2000.0)))  # Clamp and convert to integer
    
    BUZZER_PIN.freq(buzzer_freq)
    
    print("Potentiometer:", pot_value, " | Frequency:", buzzer_freq, "Hz")
    
    utime.sleep(0.1)