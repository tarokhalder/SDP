from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess


#fun for database
def open_new():
    window.destroy();
    subprocess.Popen(["python" , "login.py"])

def save_data():
    full_name = entry_1.get()
    email = entry_2.get()
    password = entry_3.get()
    conn = sqlite3.connect('log.db')
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS userinformation (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    # Insert data into the table
    try:
        cursor.execute('''
            INSERT INTO userinformation (full_name, email, password)
            VALUES (?, ?, ?)
        ''', (full_name, email, password))
        conn.commit()
        print("Data inserted successfully")
    except sqlite3.IntegrityError:
        print("Error: Email already exists")
    finally:
        conn.close()



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("776x512")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 512,
    width = 776,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage (file="bgca.png")
image_1 = canvas.create_image(
    388.0,
    256.0,
    image=image_image_1
)

canvas.create_text(
    103.0,
    94.0,
    anchor="nw",
    text="Create account",
    fill="#000000",
    font=("Inter", 23 * -1)
)

canvas.create_text(
    24.0,
    283.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("Inter", 23 * -1)
)

canvas.create_rectangle(
    113.0,
    123.99999999999997,
    253.0,
    125.0,
    fill="#2326C7",
    outline="")

canvas.create_text(
    30.0,
    140.0,
    anchor="nw",
    text="Full Name",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_rectangle(
    23.0,
    212.0,
    251.0,
    213.0,
    fill="#000000",
    outline="")

canvas.create_text(
    30.0,
    213.0,
    anchor="nw",
    text="Email",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_rectangle(
    26.0,
    364.00000733435843,
    258.9995356998361,
    367.0531005859375,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    20.0,
    276.0000000841017,
    258.9999939818226,
    279.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    34.0,
    169.9999999469572,
    114.0000033074175,
    172.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    34.0,
    317.0,
    114.0,
    318.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    34.0,
    242.0,
    73.0,
    243.0,
    fill="#000000",
    outline="")

entry_image_1 = PhotoImage(
    file= "ca1e.png")
entry_bg_1 = canvas.create_image(
    138.0,
    192.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=30.0,
    y=177.0,
    width=216.0,
    height=28.0
)

entry_image_2 = PhotoImage(
    file="ca2e.png")
entry_bg_2 = canvas.create_image(
    139.5,
    262.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=24.0,
    y=250.0,
    width=231.0,
    height=22.0
)

entry_image_3 = PhotoImage(
    file="ca3e.png")
entry_bg_3 = canvas.create_image(
    139.0,
    345.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=31.0,
    y=332.0,
    width=216.0,
    height=25.0
)

button_image_1 = PhotoImage(
    file="sgbutton_1.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    relief="flat" ,
    text = "Create account" ,
    compound = "center" ,
    command = save_data
)
button_1.place(
    x=41.0,
    y=388.0,
    width=210.0,
    height=41.0
)

    
#back button
button_image_2 = PhotoImage(
    file="back.png")
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open_new,
    relief="flat" 
)
button_2.place(
    x=19.0,
    y=18.0,
    width=24.0,
    height=24.0
)
window.resizable(False, False)
window.mainloop()
