from tkinter import*
import os

def restart():
     os.system('Shutdown /r /t 1')
def restart_time():
    os.system('Shutdown /r /t 20')     
def logout():
    os.system('Shutdown -1') 
def shutdown():
    os.system('Shutdown /s /t 1')     

St = Tk()
St.title('ShutDown App')
St.geometry('500x500')
St.config(bg='blue')

r_button = Button(St,text='Restart',font=('Time New Roman',20,'bold'),
           relief=RAISED,cursor='plus',command=restart)
r_button.place(x=150,y=60,height=50,width=200)


r_button = Button(St,text='Restart Time',font=('Time New Roman',20,'bold'), 
           relief=RAISED,cursor='plus',command=restart_time)
r_button.place(x=150,y=170,height=50,width=200)


lg_button = Button(St,text='Log-Out',font=('Time New Roman',20,'bold'), 
            relief=RAISED,cursor='plus',command=logout)
lg_button.place(x=150,y=270,height=50,width=200)


st_button = Button(St,text='ShutDown',font=('Time New Roman',20,'bold'),
            relief=RAISED,cursor='plus',command=shutdown)
st_button.place(x=150,y=370,height=50,width=200)

St.mainloop()
