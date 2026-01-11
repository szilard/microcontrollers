# mpremote mip install github:mcauser/micropython-tm1637
# mpremote connect auto fs cp tm1637_test.py :/main.py
# mpremote reset
# mpremote repl


import tm1637
from machine import Pin
from time import sleep

tm = tm1637.TM1637(clk=Pin(5), dio=Pin(4))

# all LEDS on "88:88"
tm.write([127, 255, 127, 127])
sleep(1)

# all LEDS off
tm.write([0, 0, 0, 0])
sleep(1)

# show "0123"
tm.write([63, 6, 91, 79])

# show "COOL"
tm.write([0b00111001, 0b00111111, 0b00111111, 0b00111000])
sleep(1)

# show "12:59"
tm.numbers(12, 59)
sleep(1)

# show "-123"
tm.number(-123)
sleep(1)

# show temperature '24*C'
tm.temperature(24)
sleep(1)
