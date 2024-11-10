from tkinter import *
from PIL import ImageTk
import subprocess

# Create the main window
root = Tk()
root.geometry('990x660+50+50')
root.title("Stu teacher")
root.resizable(False, False)

image = ImageTk.PhotoImage(file='st.jpg')
bgLabel = Label(root, image = image);
bgLabel.place(x=0, y = 0)

def go() :
    root.destroy();
    subprocess.Popen(['python', 'main.py'])

st_button = Button(root, text='Student',font = ('arial', 16 , 'bold'), width=16, height = 2, bg="#87CEEB",fg = 'White' , activebackground="#87CEEB", activeforeground="White" , bd=0, highlightthickness=0 , command = go )
st_button.place(x=665, y=230)


t_button = Button(root, text='Teacher',font = ('arial', 16 , 'bold'), width=16, height = 2, bg="#87CEEB",fg = 'White' , activebackground="#87CEEB", activeforeground="White" , bd=0, highlightthickness=0 , command = go)
t_button.place(x=665, y=365)

root.mainloop()


