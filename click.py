# Libraries
import keyboard
import time
import mouse
from pynput.mouse import Button, Controller

mouse = Controller()
# Infinite Loop for activation
while True:
    if keyboard.is_pressed('w'):
        print("You pressed W")
        time.sleep(0.05)
    if keyboard.is_pressed('c'):
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(0.02)
    if keyboard.is_pressed('q'):
        break
# Parameters Adjustment
