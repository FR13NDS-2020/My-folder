#10 000 klikov v sekundu
import mouse
import time
import keyboard as key

start_key = input("klavisha start :")
stop_key = input("klavisha stop :")
while True:
    if key.is_pressed(start_key):
        time.sleep(0.001)
        mouse.double_click(button="left")
        mouse.double_click(button="left")
        mouse.double_click(button="left")
        mouse.double_click(button="left")
        mouse.double_click(button="left")
        mouse.double_click(button="left")
        mouse.double_click(button="left")
        mouse.double_click(button="left")
    if key.is_pressed(stop_key):
        break
