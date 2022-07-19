from tkinter import *
import random
chance=5
r=random.randint(1,100)
root=Tk()
root.title("Guess the number")
def play():
    def submit():
        global r
        global chance
        n=""
        n=enter.get()
        if n=="/n" or n=="":
            result.config(text="enter a value")
            return
        else:
            n=int(n)
            if chance>0:
                chance=chance-1
                ch.config(text="you have "+str(chance)+" left")
                if n<r:
                    result.config(text="value is greater")
                elif n>r:
                    result.config(text="value is less")
                else:
                    result.config(text="You won")
            else:
                result.config(text="You lose and the value was:"+str(r))
            enter.delete(0,END)
    gui=Tk()
    gui.title("Guess the number")
    label=Label(gui,text="Guess the number between 1 to 100")
    ch=Label(gui,text="you have 5 chances")
    enter=Entry(gui)
    submitb=Button(gui,text="submit",command=submit)
    result=Label(gui)
    label.pack()
    ch.pack()
    enter.pack()
    submitb.pack()
    result.pack()
    gui.mainloop()
def setting():
    newSetting()
def exit():
    root.quit()

playb=Button(root,text="Play",command=play)
settingb=Button(root,text="How to play")#,command=setting)
exitb=Button(root,text="Exit",command=exit)
playb.pack()
settingb.pack()
exitb.pack()
root.mainloop()