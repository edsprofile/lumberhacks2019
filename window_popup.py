from tkinter import *
from tkinter import font
from countdown_timer import *

import time

def window_popup():
    #make a basic gui to display
    global timer
    window = Tk()
    window_text_font = font.Font(family = 'Times', size = 20, weight="bold");
    
    window.title("Humboldt ITS help desk")
    window.geometry('1900x1080')
    is_something_wrong = Label(window, text="Do you need more help please press button again? within time limit, thank you"
                                ,font=window_text_font, height=8,width=80)
    is_something_wrong.pack()
    
    timer_button = Label(window, text="Timer",font=window_text_font, height=8, width=80)
    timer_button.pack(side="bottom")
    

    
        
    