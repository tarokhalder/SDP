
from tkinter import *
from PIL import ImageTk
import subprocess

# Create the main window
signup_window = Tk()
signup_window.geometry('990x660+50+50')
signup_window.title("Signup Page")
signup_window.resizable(False, False)

image = ImageTk.PhotoImage(file='bg.jpg')
bgLabel = Label(signup_window, image = image);
bgLabel.place(x=0, y = 0)

heading  = Label(signup_window, text ='Sign up' , font =('Microsoft Yahei UI Light',23,'bold'), bg = 'White' , fg ='magenta1')
heading.place(x = 605 , y = 130)
userLabel = Label(signup_window , text ='Username', font =('arial' , 15 ,'bold') , bg ='white' ,fg ='magenta1' )
userLabel.place(x = 605 , y = 170)

user_name = Entry(signup_window , width = 25 , fg = 'magenta2' , font = ('arial', 12 , 'bold'), bd = 0 )
user_name.place( x = 605 , y = 210)

user_email = Label(signup_window , text = 'E-mail' , font = ('arial' , 15 ,'bold') , bg ='white' ,fg ='magenta1')
user_email.place (x = 605 , y =235)

user_mail = Entry(signup_window , width = 25 , fg = 'magenta2' , font = ('arial', 12 , 'bold'), bd = 0 )
user_mail.place( x = 605 , y = 270)

user_pass = Label(signup_window , text = 'Password' , font = ('arial' , 15 ,'bold') , bg ='white' ,fg ='magenta1')
user_pass.place (x = 605 , y =300)

user_pas = Entry(signup_window , width = 25 , fg = 'magenta2' , font = ('arial', 12 , 'bold'), bd = 0 )
user_pas.place( x = 605 , y = 335)

user_pass = Label(signup_window , text = 'Confirm Password' , font = ('arial' , 15 ,'bold') , bg ='white' ,fg ='magenta1')
user_pass.place (x = 605 , y =365)

user_pas = Entry(signup_window , width = 25 , fg = 'magenta2' , font = ('arial', 12 , 'bold'), bd =0 , show = '*' )
user_pas.place( x = 605 , y = 395)

signup_button = Button(signup_window, text='Sign up',font = ('arial', 11 , 'bold'), width=25, activebackground="magenta1", activeforeground="white")
signup_button.place(x=605, y=425)

reset_pass = Button(signup_window , text = 'Reset Password' , font = ('arial', 11 , 'bold'), width=25, activebackground="magenta1", activeforeground="white")
reset_pass.place (x = 605 , y = 460);

def back():
    signup_window.destroy()
    subprocess.Popen(['python', 'main.py'])
    
back_button = Button(signup_window , text = 'Back' , font = ('arial', 11 , 'bold'), width=25, activebackground="magenta1", activeforeground="white" , command = back)
back_button.place (x= 605 , y = 490)


signup_window.mainloop()

