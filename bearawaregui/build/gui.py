from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/grantpedersen/Desktop/bearawarecode/bearawaregui/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("730x444")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 444,
    width = 730,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    365.0,
    222.0,
    image=image_image_1
)

canvas.create_text(
    189.0,
    96.0,
    anchor="nw",
    text="Bear Aware is running.",
    fill="#000000",
    font=("AddingtonCF Bold", 32 * -1)
)

canvas.create_rectangle(
    248.0,
    143.0,
    481.0,
    340.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    189.0,
    349.0,
    anchor="nw",
    text="Emotion",
    fill="#000000",
    font=("AddingtonCF Bold", 32 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    191.0,
    349.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
