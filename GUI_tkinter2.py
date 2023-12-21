# !/usr/bin/python3  
from tkinter import *  
from tkinter import ttk
from tkinter import messagebox


root = Tk() 
root.geometry("1200x800") 
root.title("DEBUG / MANUAL MODE GUI") 

s = ttk.Style()
s.theme_create( "MyStyle", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {"configure": {"padding": [70, 10],
                                        "font" : ('URW Gothic L', '11', 'bold')},}})
s.theme_use("MyStyle")


# s.configure('TNotebook.Tab', font=('URW Gothic L','11','bold') )

#--------------------- DEFINE TABS ---------------------------------------
tabControl = ttk.Notebook(root) 
  
tab1 = Frame(tabControl) 
tab2 = Frame(tabControl) 
tab3 = Frame(tabControl)
tab4 = Frame(tabControl)
tab5 = Frame(tabControl)
  
tabControl.add(tab1, text ='Pumps') 
tabControl.add(tab2, text ='Valves') 
tabControl.add(tab3, text ='Degas Temperature') 
tabControl.add(tab4, text ='Motors') 
tabControl.add(tab5, text ='Bubble Sensors') 
tabControl.pack(expand = 1, fill ="both") 


#--------------------- DEFINE CALLBACK FUNCTIONS FOR BUTTONS ---------------------------------------
def p1_b_abs_pos_click():
    print("p1_abs pos")
    s =   ent_abs_pos.get()
    print(s)

def p1_b_pickup_pos_click():
    print("p1_pickup ")
    s =   ent_pickup_pos.get()
    print(s)

def p1_b_dispense_pos_click():
    print("p1_dispense ")
    s =   ent_dispemse_pos.get()
    print(s)

def p1_b_top_spd_click():
    print("p1_top speed")
    s =   ent_top_spd.get()
    print(s)

def p2_b_abs_pos_click():
    print("p2_abs pos")
    s =   ent_abs_pos.get()
    print(s)

def p2_b_pickup_pos_click():
    print("p2_pickup ")
    s =   ent_pickup_pos.get()
    print(s)

def p2_b_dispense_pos_click():
    print("p2_dispense ")
    s =   ent_dispemse_pos.get()
    print(s)

def p2_b_top_spd_click():
    print("p2_top speed")
    s =   ent_top_spd.get()
    print(s)

#---------------------  PUMP TAB ---------------------------------------
dy_t1 = 50
dx_t1 = 50
col1 = 140
 
row2 = 100
#--------------------- DEFINE PUMP 1 ---------------------------------------


#-------------------- Separator object
separator1 = ttk.Separator(tab1, orient='vertical')
separator1.place(relx=0, rely=0, relwidth=1, relheight=1)

separator2 = ttk.Separator(tab1, orient='vertical')
separator2.place(relx=0.25, rely=0, relwidth=1, relheight=1)

separator3 = ttk.Separator(tab1, orient='vertical')
separator3.place(relx=0.5, rely=0, relwidth=1, relheight=1)

separator4 = ttk.Separator(tab1, orient='vertical')
separator4.place(relx=0.75, rely=0, relwidth=1, relheight=1)

# separator2 = ttk.Separator(tab1, orient='horizontal')
# separator2.place(relx=0, rely=0.5, relwidth=1, relheight=1)

Label(tab1, text = "PUMP 1 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t1+60,y = 50)  
Label(tab1, text = "Position",font=("Arial", 15), bg='#D9D9D9',fg='black' ).place(x = dx_t1+70,y = 130)  
Label(tab1, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t1,y = col1 + dy_t1)  
p1_cur_pos = Label(tab1, text = "----",font=("Arial", 10) ).place(x =row2 + dx_t1,y = col1 + dy_t1)  

Label(tab1, text = "Absolute Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t1,y = col1 + 2*dy_t1)  
ent_abs_pos = Entry(tab1, width=8)
ent_abs_pos.pack()
ent_abs_pos.place(x = row2 + dx_t1,y = col1 + 2*dy_t1 ) 
b_abs_pos = Button(tab1,text="set", bg="#c5ccd1", fg="red", command=p1_b_abs_pos_click).place(x = row2 + dx_t1+60,
                                                                                           y = col1 + 2*dy_t1 - 2)
Label(tab1, text = "Pickup Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t1,y = col1 + 3*dy_t1)  
ent_pickup_pos = Entry(tab1, width=8) 
ent_pickup_pos.pack()
ent_pickup_pos.place(x = row2 + dx_t1,y = col1 + 3*dy_t1, )
b_pickup_pos = Button(tab1,text="set", bg="#c5ccd1", fg="red", command=p1_b_pickup_pos_click).place(x = row2 + dx_t1+60,
                                                                                           y = col1 + 3*dy_t1 - 2)
Label(tab1, text = "Dispense Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t1,y = col1 + 4*dy_t1)  
ent_dispemse_pos = Entry(tab1, width=8)
ent_dispemse_pos.pack()
ent_dispemse_pos.place(x = row2 + dx_t1,y = col1 + 4*dy_t1, ) 
b_dispense_pos = Button(tab1,text="set", bg="#c5ccd1", fg="red", command=p1_b_dispense_pos_click).place(x = row2 + dx_t1+60,
                                                                                           y = col1 + 4*dy_t1 - 2)
Label(tab1, text = "Speed",font=("Arial", 15) , bg='#D9D9D9',fg='black').place(x = dx_t1+70,y =  col1 + 5*dy_t1)  
Label(tab1, text = "Cur Top Spd",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t1,y = col1 + 6*dy_t1)  
p1_cur_spd = Label(tab1, text = "----",font=("Arial", 10) ).place(x =row2 + dx_t1,y = col1 + 6*dy_t1)  
Label(tab1, text = "Top Speed",font=("Arial", 10), bg='#D9D9D9',fg='black' ).place(x = dx_t1,y = col1 + 7*dy_t1)  
ent_top_spd = Entry(tab1, width=8)
ent_top_spd.pack()
ent_top_spd.place(x = row2 + dx_t1,y = col1 + 7*dy_t1, ) 
b_top_spd = Button(tab1,text="set", bg="#c5ccd1", fg="red", command=p1_b_top_spd_click).place(x = row2 + dx_t1+60,
                                                                                           y = col1 + 7*dy_t1 - 2)
# Label(tab2, text ="Lets dive into the world of computers", bg='#D9D9D9',fg='black').grid(column = 0,row = 0, 
                                                                # padx = 30, pady = 30) 


  
dy_t1 = 50
dx_t2 = 350
col10 = 140
row2 = 100
#--------------------- DEFINE PUMP 2 ---------------------------------------
Label(tab1, text = "PUMP 2 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t2 +60,y = 50)  
Label(tab1, text = "Position",font=("Arial", 15), bg='#D9D9D9',fg='black' ).place(x = dx_t2+70,y = 130)  
Label(tab1, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t2,y = col10 + dy_t1)  
p_cur_pos2 = Label(tab1, text = "----",font=("Arial", 10) ).place(x =row2 + dx_t2,y = col10 + dy_t1)  

Label(tab1, text = "Absolute Pos",font=("Arial", 10), bg='#D9D9D9',fg='black' ).place(x = dx_t2,y = col10 + 2*dy_t1)  
ent_abs_pos2 = Entry(tab1, width=8)
ent_abs_pos2.pack()
ent_abs_pos2.place(x = row2 + dx_t2,y = col10 + 2*dy_t1 ) 
b_abs_pos2 = Button(tab1,text="set", bg="#c5ccd1", fg="red", command=p2_b_abs_pos_click).place(x = row2 + dx_t2+60,
                                                                                           y = col10 + 2*dy_t1 - 2)
Label(tab1, text = "Pickup Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t2,y = col10 + 3*dy_t1)  
ent_pickup_pos2 = Entry(tab1, width=8) 
ent_pickup_pos2.pack()
ent_pickup_pos2.place(x = row2 + dx_t2,y = col10 + 3*dy_t1, )
b_pickup_pos2 = Button(tab1,text="set", bg="#c5ccd1", fg="red", command=p2_b_pickup_pos_click).place(x = row2 + dx_t2+60,
                                                                                           y = col10 + 3*dy_t1 - 2)
Label(tab1, text = "Dispense Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t2,y = col10 + 4*dy_t1)  
ent_dispemse_pos2 = Entry(tab1, width=8)
ent_dispemse_pos2.pack()
ent_dispemse_pos2.place(x = row2 + dx_t2,y = col10 + 4*dy_t1, ) 
b_dispense_pos2 = Button(tab1,text="set", bg="#c5ccd1", fg="red", command=p2_b_dispense_pos_click).place(x = row2 + dx_t2+60,
                                                                                           y = col10 + 4*dy_t1 - 2)
Label(tab1, text = "Speed",font=("Arial", 15) , bg='#D9D9D9',fg='black').place(x = dx_t2+70,y =  col10 + 5*dy_t1)  
Label(tab1, text = "Cur Top Spd",font=("Arial", 10), bg='#D9D9D9',fg='black' ).place(x = dx_t2,y = col10 + 6*dy_t1)  
p1_cur_spd2 = Label(tab1, text = "----",font=("Arial", 10) ).place(x =row2 + dx_t2,y = col10 + 6*dy_t1)  
Label(tab1, text = "Top Speed",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t2,y = col10 + 7*dy_t1)  
ent_top_spd2 = Entry(tab1, width=8)
ent_top_spd2.pack()
ent_top_spd2.place(x = row2 + dx_t2,y = col10 + 7*dy_t1, ) 
b_top_spd2 = Button(tab1,text="set", bg="#c5ccd1", fg="red", command=p2_b_top_spd_click).place(x = row2 + dx_t2+60,
                                                                                           y = col10 + 7*dy_t1 - 2)
# Label(tab2, text ="Lets dive into the world of computers", bg='#D9D9D9',fg='black').grid(column = 0,row = 0, 
#                                                                 padx = 30, pady = 30) 







#--------------------- DEFINE CALLBACK FUNCTIONS FOR VALVES BUTTONS ---------------------------------------
def checkCombo1():
    print('-->'+combo1.get())


def checkCombo3():
    print('-->'+combo3.get())

def checkCombo5():
    print('-->'+combo5.get())

def checkCombo9():
    print('-->'+combo9.get())        

def checkCombo2():
    print('-->'+combo2.get())  

def checkCombo4():
    print('-->'+combo4.get()) 

def checkCombo6():
    print('-->'+combo6.get()) 

def checkCombo7():
    print('-->'+combo7.get()) 

def checkCombo8():
    print('-->'+combo8.get()) 
#---------------------  VALVE   TAB ---------------------------------------
dy_t1 = 35
dx_t1 = 50
col1 = 60
row2 = 100
#--------------------- COLUMN 1: VALVES 1, 3 ---------------------------------------


#-------------------- Separator object
separator1 = ttk.Separator(tab2, orient='vertical')
separator1.place(relx=0, rely=0, relwidth=1, relheight=1)

separator2 = ttk.Separator(tab2, orient='vertical')
separator2.place(relx=0.25, rely=0, relwidth=1, relheight=1)

separator3 = ttk.Separator(tab2, orient='vertical')
separator3.place(relx=0.5, rely=0, relwidth=1, relheight=1)

separator4 = ttk.Separator(tab2, orient='vertical')
separator4.place(relx=0.75, rely=0, relwidth=1, relheight=1)

# # separator2 = ttk.Separator(tab2, orient='horizontal')
# # separator2.place(relx=0, rely=0.5, relwidth=1, relheight=1)

Label(tab2, text = "VALVE 1 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t1+60,y = col1-5)  
Label(tab2, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t1,y = col1 + dy_t1)  
v1_cur_pos = Label(tab2, text = "----",font=("Arial", 10) ).place(x =row2 + dx_t1,y = col1 + dy_t1)  
Label(tab2, text = "New Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t1,y = col1 + 2*dy_t1)  
combo1 = ttk.Combobox(tab2,  width=2, font="Verdana 12 ")
combo1['values'] = (1,2,3,4,5,"Text")
combo1.current(3)
combo1.place(x = row2 + dx_t1,y = col1 + 2*dy_t1)
Button(tab2, bg="#c5ccd1", fg="red",text="set", command=checkCombo1).place(x = row2 + dx_t1+50,y = col1 + 2*dy_t1 - 2)

yy = 140
Label(tab2, text = "VALVE 3 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t1+60,y = yy+col1-5)  
Label(tab2, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t1,y = yy+col1 + dy_t1)  
v3_cur_pos = Label(tab2, text = "----",font=("Arial", 10) ).place(x =row2 + dx_t1,y = yy+col1 + dy_t1)  
Label(tab2, text = "New Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t1,y = yy+col1 + 2*dy_t1)  
combo3 = ttk.Combobox(tab2,  width=2, font="Verdana 12 ")
combo3['values'] = (1,2,3,4,5,"Text")
combo3.current(3)
combo3.place(x = row2 + dx_t1,y =yy+ col1 + 2*dy_t1)
Button(tab2, bg="#c5ccd1", fg="red",text="set", command=checkCombo3).place(x = row2 + dx_t1+50,y =yy+ col1 + 2*dy_t1 - 2)

yy = 283
Label(tab2, text = "VALVE 5 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t1+60,y = yy+col1-5)  
Label(tab2, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t1,y = yy+col1 + dy_t1)  
v5_cur_pos = Label(tab2, text = "----",font=("Arial", 10) ).place(x =row2 + dx_t1,y = yy+col1 + dy_t1)  
Label(tab2, text = "New Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t1,y = yy+col1 + 2*dy_t1)  
combo5 = ttk.Combobox(tab2,  width=2, font="Verdana 12 ")
combo5['values'] = (1,2,3,4,5,"Text")
combo5.current(3)
combo5.place(x = row2 + dx_t1,y =yy+ col1 + 2*dy_t1)
Button(tab2, bg="#c5ccd1", fg="red",text="set", command=checkCombo5).place(x = row2 + dx_t1+50,y =yy+ col1 + 2*dy_t1 - 2)

yy = 423
Label(tab2, text = "VALVE 9 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t1+60,y = yy+col1-5)  
Label(tab2, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t1,y = yy+col1 + dy_t1)  
v5_cur_pos = Label(tab2, text = "----",font=("Arial", 10) ).place(x =row2 + dx_t1,y = yy+col1 + dy_t1)  
Label(tab2, text = "New Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t1,y = yy+col1 + 2*dy_t1)  
combo9 = ttk.Combobox(tab2,  width=2, font="Verdana 12 ")
combo9['values'] = (1,2,3,4,5,"Text")
combo9.current(3)
combo9.place(x = row2 + dx_t1,y =yy+ col1 + 2*dy_t1)
Button(tab2, bg="#c5ccd1", fg="red",text="set", command=checkCombo9).place(x = row2 + dx_t1+50,y =yy+ col1 + 2*dy_t1 - 2)

  

# dy_t1 = 50
# dx_t2 = 350
# col10 = 140
# row2 = 100
#--------------------- DEFINE PUMP 2  VALVES ---------------------------------------
Label(tab2, text = "VALVE 2 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t2 +60,y = 50)  
Label(tab2, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t2,y = col1 + dy_t1)  
v2_cur_pos = Label(tab2, text = "----",font=("Arial", 10) ).place(x =row2 + dx_t2,y = col1 + dy_t1)  


Label(tab2, text = "New Pos",font=("Arial", 10), bg='#D9D9D9',fg='black' ).place(x = dx_t2,y = col1 + 2*dy_t1)  
combo2 = ttk.Combobox(tab2,  width=2, font="Verdana 12 ")
combo2['values'] = (1,2,3,4,5,"Text")
combo2.current(3)
combo2.place(x = row2 + dx_t2,y = col1 + 2*dy_t1)
Button(tab2,text="set", bg="#c5ccd1", fg="red", command=checkCombo2).place(x =row2 + dx_t2+50,y = col1 + 2*dy_t1 - 2)


yy = 140
Label(tab2, text = "VALVE 4 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t2 +60,y=yy+col1-5)  
Label(tab2, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t2,y = yy+col1 + dy_t1)  
v4_cur_pos = Label(tab2, text = "----",font=("Arial", 10) ).place(x =row2 + dx_t2,y = yy+col1 + dy_t1)  
Label(tab2, text = "New Pos",font=("Arial", 10), bg='#D9D9D9',fg='black' ).place(x = dx_t2,y = yy+col1 + 2*dy_t1)  
combo4 = ttk.Combobox(tab2,  width=2, font="Verdana 12 ")
combo4['values'] = (1,2,3,4,5,"Text")
combo4.current(3)
combo4.place(x = row2 + dx_t2,y = yy+col1 + 2*dy_t1)
Button(tab2,text="set2", bg="#c5ccd1", fg="red", command=checkCombo4).place(x =row2 + dx_t2+50,y = yy+col1 + 2*dy_t1)

yy = 283
Label(tab2, text = "VALVE 6 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t2 +60,y=yy+col1-5)  
Label(tab2, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t2,y = yy+col1 + dy_t1)  
v6_cur_pos = Label(tab2, text = "----",font=("Arial", 10) ).place(x =row2 + dx_t2,y = yy+col1 + dy_t1)  
Label(tab2, text = "New Pos",font=("Arial", 10), bg='#D9D9D9',fg='black' ).place(x = dx_t2,y = yy+col1 + 2*dy_t1)  
combo6 = ttk.Combobox(tab2,  width=2, font="Verdana 12 ")
combo6['values'] = (1,2,3,4,5,"Text")
combo6.current(3)
combo6.place(x = row2 + dx_t2,y = yy+col1 + 2*dy_t1)
Button(tab2,text="set", bg="#c5ccd1", fg="red", command=checkCombo6).place(x =row2 + dx_t2+50,y = yy+col1 + 2*dy_t1)

yy = 423
Label(tab2, text = "VALVE 7 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t2 +60,y=yy+col1-5)  
Label(tab2, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t2,y = yy+col1 + dy_t1)  
v7_cur_pos = Label(tab2, text = "----",font=("Arial", 10) ).place(x =row2 + dx_t2,y = yy+col1 + dy_t1)  
Label(tab2, text = "New Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t2,y = yy+col1 + 2*dy_t1)  
combo7 = ttk.Combobox(tab2,  width=2, font="Verdana 12 ")
combo7['values'] = (1,2,3,4,5,"Text")
combo7.current(3)
combo7.place(x = row2 + dx_t2,y =yy+ col1 + 2*dy_t1)
Button(tab2, bg="#c5ccd1", fg="red",text="set", command=checkCombo7).place(x =row2 + dx_t2+50,y =yy+ col1 + 2*dy_t1 - 2)

yy = 566
Label(tab2, text = "VALVE 8 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t2 +60,y=yy+col1-5)  
Label(tab2, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t2,y = yy+col1 + dy_t1)  
v8_cur_pos = Label(tab2, text = "----",font=("Arial", 10) ).place(x =row2 + dx_t2,y = yy+col1 + dy_t1)  
Label(tab2, text = "New Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t2,y = yy+col1 + 2*dy_t1)  
combo8 = ttk.Combobox(tab2,  width=2, font="Verdana 12 ")
combo8['values'] = (1,2,3,4,5,"Text")
combo8.current(3)
combo8.place(x = row2 + dx_t2,y =yy+ col1 + 2*dy_t1)
Button(tab2, bg="#c5ccd1", fg="red",text="set", command=checkCombo8).place(x =row2 + dx_t2+50,y =yy+ col1 + 2*dy_t1 - 2)
root.mainloop()