from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
def open_new():
    window.destroy()
    subprocess.Popen(["python" , "login.py"])

window = Tk()

window.geometry("776x512")
window.configure(bg="#FFFFFF")
window.title("Main")  # Corrected typo


# Canvas setup
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=512,
    width=776,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

# Load and place images, buttons
button_image_1 = PhotoImage(file="button_1main.png")
button_1 = Button(
    window,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_new,
    relief="flat",
    text="Student",
    compound="center"
)
button_1.place(
    x=531.0,
    y=163.0,
    width=135.0,
    height=56.0
)

button_image_2 = PhotoImage(file="button_2main.png")
button_2 = Button(
    window,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command= open_new ,
    relief="flat",
    text="Teacher",
    compound="center"
)
button_2.place(
    x=531.0,
    y=254.0,
    width=135.0,
    height=57.0
)

# Background image
image_image_1 = PhotoImage(file="mainbg.png")
canvas.create_image(
    260.0,
    254.0,
    image=image_image_1
)

# Prevent garbage collection of images
window.image_image_1 = image_image_1
window.button_image_1 = button_image_1
window.button_image_2 = button_image_2

window.resizable(False, False)
window.mainloop()
