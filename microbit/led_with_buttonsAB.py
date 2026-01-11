from microbit import *
import math

sleep_time = 500  # Start with 500ms

while True:
    # Check button A to multiply by sqrt(2)
    if button_a.was_pressed():
        sleep_time = int(sleep_time * math.sqrt(2))
        sleep(100)  # Debounce delay
    
    # Check button B to divide by sqrt(2)
    if button_b.was_pressed():
        sleep_time = int(sleep_time / math.sqrt(2))
        if sleep_time < 1:  # Ensure minimum 1ms
            sleep_time = 1
        sleep(100)  # Debounce delay
    
    pin0.write_digital(1)
    display.set_pixel(0, 0, 9)
    sleep(sleep_time)
    pin0.write_digital(0)
    display.set_pixel(0, 0, 0)
    sleep(sleep_time)