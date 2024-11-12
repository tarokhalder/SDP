from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import subprocess

window = Tk()
window.geometry("776x512")
window.configure(bg="#FFFFFF")

def open_new():
    window.destroy()
    subprocess.Popen(["python" , "signup.py"])

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

# Display Image
image_image_1 = PhotoImage(file="logb.png")
image_1 = canvas.create_image(388.0, 256.0, image=image_image_1)

canvas.create_text(
    557.0,
    82.0,
    anchor="nw",
    text="Login",
    fill="#000000",
    font=("Inter Black", 32 * -1)
)

canvas.create_rectangle(
    572.0,
    131.0,
    631.0,
    132.0,
    fill="#1532C2",
    outline=""
)

# create account Button
button_image_1 = PhotoImage(file="ca.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command= open_new,
    relief="flat",
    text="Create account",
    compound="center"
)
button_1.place(x=472.0, y=368.0, width=247.0, height=48.0)

canvas.create_rectangle(
    482.0,
    220.0,
    717.0,
    221.0,
    fill="#000000",
    outline=""
)

canvas.create_rectangle(
    483.0,
    309.0,
    717.9999847412109,
    310.0,
    fill="#000000",
    outline=""
)

canvas.create_text(
    489.0,
    132.0,
    anchor="nw",
    text="Username",
    fill="#000000",
    font=("Inter Black", 23 * -1)
)

canvas.create_text(
    484.0,
    229.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("Inter Black", 23 * -1)
)

# Username Entry
entry_image_1 = PhotoImage(file="entry_1l.png")
entry_bg_1 = canvas.create_image(602.0, 198.5, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_1.place(x=489.0, y=182.0, width=226.0, height=31.0)

# Password Entry
entry_image_2 = PhotoImage(file="entry_2l.png")
entry_bg_2 = canvas.create_image(597.0, 289.5, image=entry_image_2)
entry_2 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_2.place(x=484.0, y=273.0, width=226.0, height=31.0)

# LOg in Button
button_image_2 = PhotoImage(file="btl1.png")
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat" ,
    text = "Log in",
    compound = "center"
)
button_2.place(x=513.0, y=319.0, width=165.0, height=45.0)

# Reset Password Button
button_image_3 = PhotoImage(file="backl.png")
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(x=717.0, y=11.0, width=46.0, height=39.0)

# Additional Button
rsp = PhotoImage(file="rs.png")
rs = Button(
    image=rsp,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat" ,
    text = "Reset Password" ,
    compound = "center" 
)
rs.place(x=472.0, y=420.0, width=247.0, height=52.0)

window.resizable(False, False)
window.mainloop()
