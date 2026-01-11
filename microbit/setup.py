# using python.microbit.org (modified micropython / micro:bit custom features)
# run simulator
# download .hex file (bundles micropython+your program) & copy to micro:bit

# other option:
# makecode.microbit.org (block/python/JS, deploys .hex file with JS engine+your JS (not python) program)

# related:
# arcade.makecode.com (similar to above but deploys to devices with small screen rather than micro:bit)


from microbit import *
import random
import speech 
import music

music.play(music.POWER_UP)       
while True:
    if button_b.was_pressed():  
        dice_number = random.randint(0, 9) 
        display.show(str(dice_number))    
        speech.say(str(dice_number))
    
