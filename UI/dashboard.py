from tkinter import *
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


num = 480
window = Tk()
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
 
canvas.create_text(
    45.0,
    122.0,
    anchor="nw",
    text="Login Error",
    fill="#FF6338",
    font=("Spartan Bold", 24 * -1)
    )

canvas.create_text(
    35.0,
    162.0,
    anchor="nw",
    text="Time period: ",
    fill="#000000",
    font=("Spartan Bold", 18 * -1)
)

entry_1 = Entry(
bd=0,
bg="#808080",
textvariable=num,
highlightthickness=0
)
entry_1.place(
x=145.0,
y=167.0,
width=72.0,
height=20.0
)

button_1 = Button(
text = 'Submit',
borderwidth=0,
highlightthickness=0,
command= lambda: print("button_1 clicked"),
relief="flat"
)
button_1.place(
x=48.0,
y=200.0,
width=147.0,
height=38.0
)

window.mainloop()


