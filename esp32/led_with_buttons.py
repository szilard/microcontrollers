from machine import Pin
import time

led = Pin(16, Pin.OUT)
btn1 = Pin(18, Pin.IN, Pin.PULL_UP)
btn2 = Pin(19, Pin.IN, Pin.PULL_UP)

DEBOUNCE_MS = 200
MIN_DELAY = 8
MAX_DELAY = 2048

delay = 512
last_event = 0

btn1_pressed = False
btn2_pressed = False

def btn1_handler(pin):
    global btn1_pressed, last_event
    now = time.ticks_ms()
    if time.ticks_diff(now, last_event) > DEBOUNCE_MS:
        btn1_pressed = True
        last_event = now

def btn2_handler(pin):
    global btn2_pressed, last_event
    now = time.ticks_ms()
    if time.ticks_diff(now, last_event) > DEBOUNCE_MS:
        btn2_pressed = True
        last_event = now

btn1.irq(trigger=Pin.IRQ_FALLING, handler=btn1_handler)
btn2.irq(trigger=Pin.IRQ_FALLING, handler=btn2_handler)

last_printed_delay = None

while True:
    if btn1_pressed:
        btn1_pressed = False
        delay = max(delay // 2, MIN_DELAY)

    if btn2_pressed:
        btn2_pressed = False
        delay = min(delay * 2, MAX_DELAY)

    if delay != last_printed_delay:
        print("delay =", delay)
        last_printed_delay = delay

    led.on()
    time.sleep_ms(delay)
    led.off()
    time.sleep_ms(delay)
