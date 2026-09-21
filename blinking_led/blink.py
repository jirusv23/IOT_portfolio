from machine import Pin
import utime

while True:
    led = Pin("LED", Pin.OUT)
    led.toggle()  # Turn on the LED
    utime.sleep(1)  # Wait for 1 second
    