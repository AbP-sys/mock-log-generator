
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


num = 480
window = tk.Tk()
#window = Tk()
window.title('Log Generator')
window.geometry("400x600")
window.configure(bg = "#FFFFFF")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 891,
    width = 411,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

canvas.place(x = 0, y = 0)
""" image_image_1 = PhotoImage(
file=relative_to_assets("bg"))
image_1 = canvas.create_image(
205.0,
373.0,
image=image_image_1 
) """
 


#configure the grid
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=1)
window.rowconfigure(2,weight=1)
window.rowconfigure(3,weight=1)
window.rowconfigure(4,weight=1)
window.rowconfigure(5,weight=1)
window.rowconfigure(6,weight=1)
window.rowconfigure(7,weight=1)
window.rowconfigure(8,weight=1)

#loginerror
loginerror_label=ttk.Label(window, text="Login Error")
loginerror_label.grid(column=0,row=0,sticky=tk.W,padx=10,pady=10)
timeperiod_label=ttk.Label(window, text="Time Period")
timeperiod_label.grid(column=0,row=1,sticky=tk.W,padx=5,pady=5)
timeperiod_entry=ttk.Entry(window)
timeperiod_entry.grid(column=0,row=1,sticky=tk.E,padx=5,pady=5)
login_button = ttk.Button(window, text="Submit")
login_button.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)

#Cpu overload
Cpuoverload_label=ttk.Label(window, text="CPU overload")
Cpuoverload_label.grid(column=1,row=0,sticky=tk.W,padx=10,pady=10)
timeperiod_label=ttk.Label(window, text="Time Period")
timeperiod_label.grid(column=1,row=1,sticky=tk.W,padx=5,pady=5)
timeperiod_entry=ttk.Entry(window)
timeperiod_entry.grid(column=1,row=1,sticky=tk.E,padx=5,pady=5)
login_button = ttk.Button(window, text="Submit")
login_button.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

#3rd prob
third_label=ttk.Label(window, text="ABC")
third_label.grid(column=0,row=3,sticky=tk.W,padx=10,pady=10)
timeperiod_label=ttk.Label(window, text="Time Period")
timeperiod_label.grid(column=0,row=4,sticky=tk.W,padx=5,pady=5)
timeperiod_entry=ttk.Entry(window)
timeperiod_entry.grid(column=0,row=4,sticky=tk.E,padx=5,pady=5)
login_button = ttk.Button(window, text="Submit")
login_button.grid(column=0, row=5, sticky=tk.E, padx=5, pady=5)

#4th prob
fourth_label=ttk.Label(window, text="XYZ")
fourth_label.grid(column=1,row=3,sticky=tk.W,padx=10,pady=10)
timeperiod_label=ttk.Label(window, text="Time Period")
timeperiod_label.grid(column=1,row=4,sticky=tk.W,padx=5,pady=5)
timeperiod_entry=ttk.Entry(window)
timeperiod_entry.grid(column=1,row=4,sticky=tk.E,padx=5,pady=5)
login_button = ttk.Button(window, text="Submit")
login_button.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)




window.mainloop()


