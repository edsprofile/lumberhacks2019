import tkinter

class CountdownTimer(tkinter.Tk):
    def _init_(self):
        tkinter.TK.__init__(self)
        self.label = tk.Label(self, text="", width=10)
        self.label.pack()
        self.remaining = 0
        self.countdown(20)
        
    def countdown(self, time = None):
        if time is not None:
            self.time = time
        
        if self.remaining <= 0:
            self.label.configure(text="00:00")
        else:
            self.label.configure(text="%d" % self.time)
            self.time = self.time - 1
            self.after(1000, self.countdown)
            
if __name__ == "__main__":
    timer = CountdownTimer()
    timer.mainloop()