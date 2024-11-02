from tkinter import *
from PIL import ImageTk
import subprocess

root = Tk()
root.geometry('990x660+50+50')
root.title('Log in')
root.resizable(False,False);

image = ImageTk.PhotoImage(file ='bg.jpg')
bgLabel = Label(root , image = image)
bgLabel.place( x = 0 , y = 0)

heading  = Label (root , text = 'Log in', font =('Microsoft Yahei UI Light',27,'bold'), bg = 'White' , fg ='magenta1')
heading.place(x = 635 , y = 130)

user  = Label (root , text = 'Username', font =('Microsoft Yahei UI Light',15,'bold'), bg = 'White' , fg ='magenta1')
user.place(x = 635 , y = 180)

user_name = Entry(root , width = 25 , fg = 'magenta2' , font = ('arial', 12 , 'bold'), bd = 0 )
user_name.place( x = 605 , y = 210)

user_email = Label(root , text = 'E-mail' , font = ('arial' , 15 ,'bold') , bg ='white' ,fg ='magenta1')
user_email.place (x = 635 , y =240)

user_mail = Entry(root , width = 25 , fg = 'magenta2' , font = ('arial', 12 , 'bold'), bd = 0 )
user_mail.place( x = 605 , y = 290)

user_pass = Label(root , text = 'Password' , font = ('arial' , 15 ,'bold') , bg ='white' ,fg ='magenta1')
user_pass.place (x = 635 , y =320)

user_pas = Entry(root , width = 25 , fg = 'magenta2' , font = ('arial', 12 , 'bold'), bd = 0 )
user_pas.place( x = 605 , y = 350)

signup_button = Button(root, text='Log in',font = ('arial', 12 , 'bold'), width=22, activebackground="magenta1", activeforeground="white")
signup_button.place(x=605, y=380)

acc = Label(root , text = 'Dont have account' , font = ('arial', 13 , 'bold'), width=22, activebackground="magenta1", activeforeground="magenta1")
acc.place(x=605 , y = 420)

def signup() :
    root.destroy();
    subprocess.Popen(['python', 'signup.py'])
registar = Button(root, text='Register',font = ('arial', 12 , 'bold'), width=22, activebackground="magenta1", activeforeground="white" , command = signup)
registar.place(x=605, y=450)





root.mainloop()
