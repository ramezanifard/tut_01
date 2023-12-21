# # !/usr/bin/python3  
# from tkinter import *  
# parent = Tk()  
# redbutton = Button(parent, text = "Red", fg = "red")  
# redbutton.pack( side = LEFT)  
# greenbutton = Button(parent, text = "Black", fg = "black")  
# greenbutton.pack( side = RIGHT )  
# bluebutton = Button(parent, text = "Blue", fg = "blue")  
# bluebutton.pack( side = TOP )  
# blackbutton = Button(parent, text = "Green", fg = "red")  
# blackbutton.pack( side = BOTTOM)  
# parent.mainloop()  


# # !/usr/bin/python3  
# from tkinter import *  
# parent = Tk()  
# name = Label(parent,text = "Name").grid(row = 0, column = 0)  
# e1 = Entry(parent).grid(row = 0, column = 1)  
# password = Label(parent,text = "Password").grid(row = 1, column = 0)  
# e2 = Entry(parent).grid(row = 1, column = 1)  
# submit = Button(parent, text = "Submit").grid(row = 4, column = 0)  
# parent.mainloop()  



# !/usr/bin/python3  
from tkinter import *  
from tkinter import ttk
from tkinter import messagebox

top = Tk()  
top.geometry("400x450")  
name = Label(top, text = "Name").place(x = 30,y = 50)  
email = Label(top, text = "Email").place(x = 30, y = 90)  
password = Label(top, text = "Password").place(x = 30, y = 130)  
e1 = Entry(top).place(x = 80, y = 50)  
e2 = Entry(top).place(x = 80, y = 90)  
e3 = Entry(top).place(x = 95, y = 130)  
# b1 = Button(top,text="button1").place(x=50,y=320)

inputtxt = Text(top, height = 5, width = 20) .place(x=170,y=20)


#-------------------------- get/show Entery text----------------------------------
def clicked():
    print("helllllo")
    s =   entry.get()
    print(s)

entry = Entry(top, width=20) 
entry.pack()
entry.place(x=170,y=200)

b2 = Button(top,text="button2", bg="orange", fg="red", command=clicked).place(x=100,y=200)
# #-------------Combo box -----------------------------------------------------
combo = ttk.Combobox(top)
combo['values'] = (1,2,3,4,5,"Text")
combo.current(3)
# combo.grid(column=0, row=0)
# combo.pack()
combo.place(x=120, y=300)
# t = combo.get()
# print('combo --> ',t)

def checkCombo():
    print('-->'+combo.get())

b3 = Button(top, text="get val", command=checkCombo).place(x=270,y=300)

# #-------------ckeck box -----------------------------------------------------
chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(top, text="Select", var=chk_state)
chk.place(x=30,y=300)

# #-------------radio button -----------------------------------------------------
rad1 = Radiobutton(top, text="Python", value=1)
rad2 = Radiobutton(top, text="Java", value=2)
rad3 = Radiobutton(top, text="Scala", value=3)
rad1.place(x=30, y=330)
rad2.place(x=30, y=350)
rad3.place(x=30, y=370)

#------------ message box --------------------------------

def mdgclicked():
    messagebox.showinfo("Message title", "message content")

btn = Button(top, text="Press to see message box", command=mdgclicked)
btn.place(x=30,y=400)

#------------ spin box --------------------------------
spin = Spinbox(top, from_=1, to=30, width=6)
spin.place(x=200,y=400)

#-----------------show image -------------------------
img = PhotoImage(file='./Mavarel_Demo/Images/led-green-off.png')

img= img.zoom(25)
icon = img.subsample(128)
label = Label(top, image=icon).place(x=350,y=300)


top.mainloop()  

