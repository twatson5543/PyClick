# Libraries
import keyboard
import time
from pynput.mouse import Button, Controller

# Defining
mouse = Controller()

click_speed = 5     # in milliseconds
quit_key = 'q'        # Key to quit program
click = 'c'           # Hold to click
click_toggle = 'x'    # Press to toggle click on/off

# Math

real_clickspd = click_speed / 1000

# Print to confirm

print("Click Speed:      ",click_speed, "(ms)")
print("Quit Key:         ",quit_key)
print("Click Key:        ",click)
print("Click Toggle Key: ",click_toggle)
print("Real Click Speed: ",real_clickspd,"(s)")

# Infinite Loop for activation
while True:

    # Hold and thou shall click fast
    if keyboard.is_pressed(click):
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(real_clickspd)

    # Press and the gods shall click for you
    if keyboard.is_pressed(click_toggle):
        print("Click Loop Activated")
        time.sleep(1)
        while True:
            mouse.press(Button.left)
            mouse.release(Button.left)
            time.sleep(real_clickspd)

            # If you want to stop clicking, press toggle again
            if keyboard.is_pressed(click_toggle):
                print("Done Clicking")
                time.sleep(1)
                break

    # Click and thou shall exit
    if keyboard.is_pressed(quit_key):
        break
