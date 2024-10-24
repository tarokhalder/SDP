from tkinter import *
from tkinter import messagebox
root =Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

try:
   img = PhotoImage(file='login.png')
except:
    print("Error Image not found")
    img=False
if img:    
    Label(root,image=img,bg='White').place(x=50,y=50)
frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)
heading = Label(frame,text='Sign In',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

#start username
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name =='':
        user.insert(0,'Username')

user=Entry(frame,width=25,fg='black', border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30, y=80);
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter);
user.bind('<FocusOut>',on_leave);
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
#end username

#start password
def on_enter(e):
    word.delete(0,'end')

def on_leave(e):
    name=word.get()
    if name =='':
        word.insert(0,'Password')

word=Entry(frame,width=25,fg='black', border=0,bg='white',font=('Microsoft YaHei UI Light',11))
word.place(x=30, y=150);
word.insert(0,'Password')
word.bind('<FocusIn>',on_enter);
word.bind('<FocusOut>',on_leave);
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
#end password

#start  sign in button
def signin():
    username=user.get()
    password=word.get();
    if username=='tarok' and password=='nai':
       screen.Toplevel(root)
       screen.title("App")
       screen.geometry()
       
Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Don't have an account?", fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)
#end sign in button


#start sign up button

sign_up=Button(frame,width=6,text='Sign up', border=0,bg='white',cursor='hand2',fg='#57a1f8')
sign_up.place(x=215,y=270)

#end sign up button

root.mainloop()
