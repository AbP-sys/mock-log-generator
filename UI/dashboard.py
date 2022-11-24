
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter import *
import simulate_webserver
import simulate_cpu

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

# spiky= PhotoImage(file = r"C:\Users\Owner\Desktop\DellH2H\UI\assets\spiky.png")
#constant = PhotoImage(file = r"C:\Users\Owner\Desktop\DellH2H\UI\assets\constant.png")
#gradual= PhotoImage(file = r"C:\Users\Owner\Desktop\DellH2H\UI\assets\gradual.png") 

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def change_graph_type(graph_type,new_type):
    graph_type.value = new_type

def render_dashboard(graph_type):
    window = tk.Tk()
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
    window.rowconfigure(1,weight=0)
    window.rowconfigure(2,weight=0)
    window.rowconfigure(3,weight=0)
    window.rowconfigure(4,weight=1)
    window.rowconfigure(5,weight=1)
    window.rowconfigure(6,weight=1)
    window.rowconfigure(7,weight=1)
    window.rowconfigure(8,weight=1)

    #loginerror
    loginerror_label=ttk.Label(window, text="Authentication failure")
    loginerror_label.grid(column=0,row=0,sticky=tk.W,padx=10,pady=10)
    ip_label=ttk.Label(window, text="IP Address")
    ip_label.grid(column=0,row=1,sticky=tk.W,padx=3,pady=3)
    ip_entry=ttk.Entry(window)
    ip_entry.grid(column=0,row=1,sticky=tk.E,padx=3,pady=3)

    attempt_label=ttk.Label(window, text="No of Attempts")
    attempt_label.grid(column=0,row=2,sticky=tk.W,padx=3,pady=3)
    attempt_entry=ttk.Entry(window)
    attempt_entry.grid(column=0,row=2,sticky=tk.E,padx=3,pady=3)

    timeperiod_label=ttk.Label(window, text="Time Period")
    timeperiod_label.grid(column=0,row=3,sticky=tk.W,padx=5,pady=5)
    timeperiod_entry=ttk.Entry(window)
    timeperiod_entry.grid(column=0,row=3,sticky=tk.E,padx=5,pady=5)
    login_button1 = ttk.Button(window, text="Submit",command=lambda: simulate_webserver.repeated_login(int(attempt_entry.get()),int(timeperiod_entry.get()),True,ip_entry.get()))
    login_button1.grid(column=0, row=4, padx=5, pady=5)

    #Cpu overload
    Cpuoverload_label=ttk.Label(window, text="CPU overload")
    Cpuoverload_label.grid(column=1,row=0,sticky=tk.W,padx=10,pady=10)

    login_button2 = ttk.Button(window, text="S",command = lambda:change_graph_type(graph_type, 1))
    login_button2.grid(column=1, row=1,sticky=tk.W, padx=5, pady=5)

    login_button3 = ttk.Button(window, text="C",command = lambda:change_graph_type(graph_type, 0))
    login_button3.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

    login_button4 = ttk.Button(window, text="G",command = lambda:change_graph_type(graph_type, 2))
    login_button4.grid(column=1, row=2, padx=10, pady=10)

    #3rd prob
    third_label=ttk.Label(window, text="Use Case 3")
    third_label.grid(column=0,row=5,sticky=tk.W,padx=10,pady=10)
    timeperiod_label2=ttk.Label(window, text="Time Period")
    timeperiod_label2.grid(column=0,row=6,sticky=tk.W,padx=5,pady=5)
    timeperiod_entry2=ttk.Entry(window)
    timeperiod_entry2.grid(column=0,row=6,sticky=tk.E,padx=5,pady=5)
    login_button5 = ttk.Button(window, text="Submit")
    login_button5.grid(column=0, row=7, sticky=tk.E, padx=5, pady=5)

    #4th prob
    fourth_label=ttk.Label(window, text="Use Case 4")
    fourth_label.grid(column=1,row=5,sticky=tk.W,padx=10,pady=10)
    timeperiod_label3=ttk.Label(window, text="Time Period")
    timeperiod_label3.grid(column=1,row=6,sticky=tk.W,padx=5,pady=5)
    timeperiod_entry3=ttk.Entry(window)
    timeperiod_entry3.grid(column=1,row=6,sticky=tk.E,padx=5,pady=5)
    login_button6 = ttk.Button(window, text="Submit")
    login_button6.grid(column=1, row=7, sticky=tk.E, padx=5, pady=5)




    window.mainloop()


