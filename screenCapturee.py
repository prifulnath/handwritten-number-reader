# pip install pyscreenshot
# pip install Pillow - Python imaging library(PIL)
# pip install pyautogui
# pip install termcolor

import pyscreenshot as ImageGrab
import time
import pyautogui
from termcolor import colored


# Get screen size to adjust the paint position
screen_width, screen_height = pyautogui.size()
print(f"Screen width: {screen_width}")
print(f"Screen height: {screen_height}")

for number in range (0, 10):
    print(colored("Capturing the image of " + str(number), 'red'))
    store_folder = './capturedImages/' + str(number) + '/'
    for i in range(30,30):
        time.sleep(8)
        # Capture the image from the x1,y1,x2,y2 coordinate
        image = ImageGrab.grab(bbox=(41,280,938,958))
        print(colored("Saved " + str(i) + "th image", "yellow"))
        image.save(store_folder + str(i) + '.png')
        print(colored("Clear screen and redraw now!", "green"))