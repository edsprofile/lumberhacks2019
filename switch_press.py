from send_text import *
from window_popup import *

import RPi.GPIO as GPIO
import time
import os, subprocess


os.environ['DISPLAY'] = ":0"

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#variables for display
#idle is for how long until screen is returned to screen saver

display_is_on = False
idle = 10
latest_signal = 0
subprocess.call('xset dpms 5 5 5', shell=True)
while True:
    current_time = time.time()
    if GPIO.input(7) == GPIO.HIGH:
        click_num = 1;
        if not display_is_on: #we need to turn the display on
            subprocess.call('xset dpms force on', shell=True)
            subprocess.call('xset dpms 20 20 20', shell=True)
            #the display is now on so set it on
            display_is_on = True
            if display_is_on and click_num == 1:
                send_text()
                window_popup()
        latest_signal = current_time;
    else:
        if current_time - latest_signal > idle:
            if display_is_on:
                display_is_on = False
        time.sleep(.2);
        
    
    
