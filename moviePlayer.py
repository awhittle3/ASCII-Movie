import tkinter as tk
from time import sleep
from movie01 import reel

window = tk.Tk()

def main():
    
    window.title("Tkinter Movie Player")
    button = tk.Button(window, text = "Play", command = processPlay)
    button.pack()
    
    window.mainloop()
    
def processPlay():
    TIME_STEP = 0.3
    
    label = tk.Label(window, text = "", font = ("Courier"))
    label.pack()
    count = 0
    
    while count < len(reel):
        s = ""
        frame = reel[count]
        for line in frame:
            s += line + "\n"
        count += 1
        label["text"] = s
        label.pack()
        window.update()
        sleep(TIME_STEP)

main()