from tkinter import *

root = Tk()
root.title('Sign up')
root.geometry('1000x600')

frame = Frame(root)
frame.pack(side=LEFT, anchor='center')


w = Label(frame, text='hello', width=35, height=22, bg='black')
w.pack()

signup_button = Button(frame, text='Create account', width=12, fg='#17a2b8')
signup_button.pack(pady=10)

right_frame = Frame(root,width=500,height=600)
right_frame.pack(side=RIGHT, anchor='center')


img = PhotoImage(file='signup.png')  
img_label = Label(right_frame, image=img)
img_label.place(x=50,y=120) 

root.mainloop()


