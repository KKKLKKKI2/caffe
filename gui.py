import tkinter as tk
from tkinter import filedialog as fi
from tkinter import Frame,Tk,BOTH,Text,Menu,END
def click1():
    #global count
    #count += 1
    #label.configure(text="click"+str(count)+'times')
    name1=OpenFile()
    nn=name1.split('/')
    label.configure(text=str(nn[-1]))




def OpenFile():
    name = fi.askopenfilename(initialdir="C:/Users\D300_ADAS\Desktop\caffe-windows\examples\moth\SingleTest_ID/",
                           filetypes =(("All Files","*.*"),("All Files","*.*")),
                           title = "Choose a file."
                           )

    #Using try in case user types in unknown file or closes without choosing a file.
    return name
    try:
        with open(name,'r') as UseFile:
            print(UseFile.read())
    except:
        print("No file exists")
win=tk.Tk()
win.title('FCC')
count=0
label=tk.Label(win,text='hello')
label.grid(column=1,row=15)
button=tk.Button(win,text='ok',command=click)
button.grid(column=15,row=18)

win.geometry("900x600+300+300")

win.mainloop()


