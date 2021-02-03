# Libraries
import keyboard
import time
import mouse
from pynput.mouse import Button, Controller

# Defining
mouse = Controller()

click_speed = 0.6     # in milliseconds
quit_key = 'q'        # Key to quit program
click = 'c'           # Hold to click
click_toggle = 'x'    # Press to toggle click on/off

# Math

real_clickspd = click_speed / 100

# Print to confirm

print("Click Speed:      ",click_speed, "(ms)")
print("Quit Key:         ",quit_key)
print("Click Key:        ",click)
print("Click Toggle Key: ",click_toggle)
print("Real Click Speed: ",real_clickspd,"(s)")

# Infinite Loop for activation
while True:
    if keyboard.is_pressed('w'):
        print("You pressed W")
        time.sleep(0.05)
    if keyboard.is_pressed(click):
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(real_clickspd)
    if keyboard.is_pressed(quit_key):
        break
# Parameters Adjustment
