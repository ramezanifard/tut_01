# !/usr/bin/python3  
from tkinter import *  
from tkinter import ttk
from tkinter import messagebox


root = Tk() 
root.geometry("1200x800") 
root.title("DEBUG / MANUAL MODE GUI") 
root.resizable(False, False)
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
  
tabControl.add(tab1, text ='Pumps/Valves') 
tabControl.add(tab2, text ='Motors') 
tabControl.add(tab3, text ='Degas Temperature') 
tabControl.add(tab4, text ='Bubble Sensors') 
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
# # Create a canvas widget
canvas=Canvas(tab1, width=1200, height=800,bg='#D9D9D9')
canvas.pack()
# Add a line in canvas widget
canvas.create_line(0,30,1200,30, fill='gray', width=1)
canvas.create_line(300,170,600,170, fill='gray', width=1)
canvas.create_line(300,320,600,320, fill='gray', width=1)
canvas.create_line(300,465,600,465, fill='gray', width=1)
canvas.create_line(300,610,600,610, fill='gray', width=1)
canvas.create_line(300,30,300,800, fill='gray', width=1)
canvas.create_line(600,30,600,800, fill='gray', width=1)
canvas.create_line(900,30,900,800, fill='gray', width=1)

canvas.create_line(900,170,1200,170, fill='gray', width=1)
canvas.create_line(900,320,1200,320, fill='gray', width=1)
canvas.create_line(900,465,1200,465, fill='gray', width=1)
canvas.create_line(900,610,1200,610, fill='gray', width=1)

#--------------------- DEFINE PUMP 1 ---------------------------------------
Label(tab1, text = "PUMP 1 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t1+60,y = 40)  
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

  

#--------------------- DEFINE PUMP 2 ---------------------------------------
dy_t1 = 50
dx_t2 = 650
col10 = 140
row2 = 100
Label(tab1, text = "PUMP 2 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t2 +60,y = 40)  
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
dx_t1 = 350
col1 = 60
row2 = 100
#--------------------- COLUMN 1: VALVES 1, 3 ---------------------------------------
Label(tab1, text = "VALVE 1 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t1+60,y = 40)  
Label(tab1, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t1,y = col1 + dy_t1)  
v1_cur_pos = Label(tab1, text = "----",font=("Arial", 10) ).place(x =row2 + dx_t1,y = col1 + dy_t1)  
Label(tab1, text = "New Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t1,y = col1 + 2*dy_t1)  
combo1 = ttk.Combobox(tab1,  width=2, font="Verdana 12 ")
combo1['values'] = (1,2,3,4,5,"Text")
combo1.current(3)
combo1.place(x = row2 + dx_t1,y = col1 + 2*dy_t1)
Button(tab1, bg="#c5ccd1", fg="red",text="set", command=checkCombo1).place(x = row2 + dx_t1+50,y = col1 + 2*dy_t1 - 2)

yy = 140
Label(tab1, text = "VALVE 3 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t1+60,y = yy+col1-15)  
Label(tab1, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t1,y = yy+col1 + dy_t1)  
v3_cur_pos = Label(tab1, text = "----",font=("Arial", 10) ).place(x =row2 + dx_t1,y = yy+col1 + dy_t1)  
Label(tab1, text = "New Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t1,y = yy+col1 + 2*dy_t1)  
combo3 = ttk.Combobox(tab1,  width=2, font="Verdana 12 ")
combo3['values'] = (1,2,3,4,5,"Text")
combo3.current(3)
combo3.place(x = row2 + dx_t1,y =yy+ col1 + 2*dy_t1)
Button(tab1, bg="#c5ccd1", fg="red",text="set", command=checkCombo3).place(x = row2 + dx_t1+50,y =yy+ col1 + 2*dy_t1 - 2)

yy = 283
Label(tab1, text = "VALVE 5 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t1+60,y = yy+col1-15)  
Label(tab1, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t1,y = yy+col1 + dy_t1)  
v5_cur_pos = Label(tab1, text = "----",font=("Arial", 10) ).place(x =row2 + dx_t1,y = yy+col1 + dy_t1)  
Label(tab1, text = "New Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t1,y = yy+col1 + 2*dy_t1)  
combo5 = ttk.Combobox(tab1,  width=2, font="Verdana 12 ")
combo5['values'] = (1,2,3,4,5,"Text")
combo5.current(3)
combo5.place(x = row2 + dx_t1,y =yy+ col1 + 2*dy_t1)
Button(tab1, bg="#c5ccd1", fg="red",text="set", command=checkCombo5).place(x = row2 + dx_t1+50,y =yy+ col1 + 2*dy_t1 - 2)

yy = 423
Label(tab1, text = "VALVE 9 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t1+60,y = yy+col1-15)  
Label(tab1, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t1,y = yy+col1 + dy_t1)  
v5_cur_pos = Label(tab1, text = "----",font=("Arial", 10) ).place(x =row2 + dx_t1,y = yy+col1 + dy_t1)  
Label(tab1, text = "New Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t1,y = yy+col1 + 2*dy_t1)  
combo9 = ttk.Combobox(tab1,  width=2, font="Verdana 12 ")
combo9['values'] = (1,2,3,4,5,"Text")
combo9.current(3)
combo9.place(x = row2 + dx_t1,y =yy+ col1 + 2*dy_t1)
Button(tab1, bg="#c5ccd1", fg="red",text="set", command=checkCombo9).place(x = row2 + dx_t1+50,y =yy+ col1 + 2*dy_t1 - 2)

  

# dy_t1 = 50
dx_t2 = 950
# col10 = 140
# row2 = 100
#--------------------- DEFINE PUMP 2  VALVES ---------------------------------------
Label(tab1, text = "VALVE 2 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t2 +60,y = 40)  
Label(tab1, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t2,y = col1 + dy_t1)  
v2_cur_pos = Label(tab1, text = "----",font=("Arial", 10) ).place(x =row2 + dx_t2,y = col1 + dy_t1)  


Label(tab1, text = "New Pos",font=("Arial", 10), bg='#D9D9D9',fg='black' ).place(x = dx_t2,y = col1 + 2*dy_t1)  
combo2 = ttk.Combobox(tab1,  width=2, font="Verdana 12 ")
combo2['values'] = (1,2,3,4,5,"Text")
combo2.current(3)
combo2.place(x = row2 + dx_t2,y = col1 + 2*dy_t1)
Button(tab1,text="set", bg="#c5ccd1", fg="red", command=checkCombo2).place(x =row2 + dx_t2+50,y = col1 + 2*dy_t1 - 2)


yy = 140
Label(tab1, text = "VALVE 4 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t2 +60,y=yy+col1-15)  
Label(tab1, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t2,y = yy+col1 + dy_t1)  
v4_cur_pos = Label(tab1, text = "----",font=("Arial", 10) ).place(x =row2 + dx_t2,y = yy+col1 + dy_t1)  
Label(tab1, text = "New Pos",font=("Arial", 10), bg='#D9D9D9',fg='black' ).place(x = dx_t2,y = yy+col1 + 2*dy_t1)  
combo4 = ttk.Combobox(tab1,  width=2, font="Verdana 12 ")
combo4['values'] = (1,2,3,4,5,"Text")
combo4.current(3)
combo4.place(x = row2 + dx_t2,y = yy+col1 + 2*dy_t1)
Button(tab1,text="set2", bg="#c5ccd1", fg="red", command=checkCombo4).place(x =row2 + dx_t2+50,y = yy+col1 + 2*dy_t1)

yy = 283
Label(tab1, text = "VALVE 6 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t2 +60,y=yy+col1-15)  
Label(tab1, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t2,y = yy+col1 + dy_t1)  
v6_cur_pos = Label(tab1, text = "----",font=("Arial", 10) ).place(x =row2 + dx_t2,y = yy+col1 + dy_t1)  
Label(tab1, text = "New Pos",font=("Arial", 10), bg='#D9D9D9',fg='black' ).place(x = dx_t2,y = yy+col1 + 2*dy_t1)  
combo6 = ttk.Combobox(tab1,  width=2, font="Verdana 12 ")
combo6['values'] = (1,2,3,4,5,"Text")
combo6.current(3)
combo6.place(x = row2 + dx_t2,y = yy+col1 + 2*dy_t1)
Button(tab1,text="set", bg="#c5ccd1", fg="red", command=checkCombo6).place(x =row2 + dx_t2+50,y = yy+col1 + 2*dy_t1)

yy = 423
Label(tab1, text = "VALVE 7 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t2 +60,y=yy+col1-15)  
Label(tab1, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t2,y = yy+col1 + dy_t1)  
v7_cur_pos = Label(tab1, text = "----",font=("Arial", 10) ).place(x =row2 + dx_t2,y = yy+col1 + dy_t1)  
Label(tab1, text = "New Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t2,y = yy+col1 + 2*dy_t1)  
combo7 = ttk.Combobox(tab1,  width=2, font="Verdana 12 ")
combo7['values'] = (1,2,3,4,5,"Text")
combo7.current(3)
combo7.place(x = row2 + dx_t2,y =yy+ col1 + 2*dy_t1)
Button(tab1, bg="#c5ccd1", fg="red",text="set", command=checkCombo7).place(x =row2 + dx_t2+50,y =yy+ col1 + 2*dy_t1 - 2)

yy = 566
Label(tab1, text = "VALVE 8 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t2 +60,y=yy+col1-15)  
Label(tab1, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t2,y = yy+col1 + dy_t1)  
v8_cur_pos = Label(tab1, text = "----",font=("Arial", 10) ).place(x =row2 + dx_t2,y = yy+col1 + dy_t1)  
Label(tab1, text = "New Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t2,y = yy+col1 + 2*dy_t1)  
combo8 = ttk.Combobox(tab1,  width=2, font="Verdana 12 ")
combo8['values'] = (1,2,3,4,5,"Text")
combo8.current(3)
combo8.place(x = row2 + dx_t2,y =yy+ col1 + 2*dy_t1)
Button(tab1, bg="#c5ccd1", fg="red",text="set", command=checkCombo8).place(x =row2 + dx_t2+50,y =yy+ col1 + 2*dy_t1 - 2)






#---------------------  MOTORS TAB ---------------------------------------

# # Create a canvas widget
canvas=Canvas(tab2, width=1200, height=800,bg='#D9D9D9')
canvas.pack()
# Add a line in canvas widget
canvas.create_line(0,30,1200,30, fill='gray', width=1)
# canvas.create_line(300,170,600,170, fill='gray', width=1)
# canvas.create_line(300,320,600,320, fill='gray', width=1)
# canvas.create_line(300,465,600,465, fill='gray', width=1)
# canvas.create_line(300,610,600,610, fill='gray', width=1)
canvas.create_line(300,30,300,800, fill='gray', width=1)
canvas.create_line(600,30,600,800, fill='gray', width=1)
canvas.create_line(900,30,900,800, fill='gray', width=1)

# canvas.create_line(900,170,1200,170, fill='gray', width=1)
# canvas.create_line(900,320,1200,320, fill='gray', width=1)
# canvas.create_line(900,465,1200,465, fill='gray', width=1)
# canvas.create_line(900,610,1200,610, fill='gray', width=1)

#--------------------- DEFINE CALLBACK FUNCTIONS FOR BUTTONS ---------------------------------------
def p1_b_abs_pos_click():
    print("m1_new_spd")
    s =   ent_m1_spd_.get()
    print(s)

def checkCombo_mh():
    print('-->'+combo_mh.get())

def checkCombo_mv():
    print('-->'+combo_mv.get())
#--------------------- DEFINE Motor 1 ---------------------------------------
dy_t1 = 50
dx_t1 = 50
col1 = 140
row2 = 100
Label(tab2, text = "MOTOR 1 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t1+40,y = 40)  
Label(tab2, text = "Current Spd",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t1,y = col1 + dy_t1)  
m1_cur_spd = Label(tab2, text = "----",font=("Arial", 10) ).place(x =row2 + dx_t1,y = col1 + dy_t1)  

Label(tab2, text = "New Spd",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t1,y = col1 + 2*dy_t1)  
ent_m1_spd_ = Entry(tab2, width=8)
ent_m1_spd_.pack()
ent_m1_spd_.place(x = row2 + dx_t1,y = col1 + 2*dy_t1 ) 
b_m1_spd = Button(tab2,text="set", bg="#c5ccd1", fg="red", command=p1_b_abs_pos_click).place(x = row2 + dx_t1+60,
                                                                                           y = col1 + 2*dy_t1 - 2)
#--------------------- COLUMN 2: Gantry Horizontal ---------------------------------------
dx_t1 = 350
Label(tab2, text = "GANTRY HORIZ.",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t1-10,y = 40)  
Label(tab2, text = "Current Spd",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t1,y = col1 + dy_t1)  
m2_cur_spd = Label(tab2, text = "----",font=("Arial", 10) ).place(x =row2 + dx_t1,y = col1 + dy_t1)  
Label(tab2, text = "New Spd",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t1,y = col1 + 2*dy_t1)  
combo_mh = ttk.Combobox(tab2,  width=2, font="Verdana 12 ")
combo_mh['values'] = (1,2,3,4,5,"Text")
combo_mh.current(3)
combo_mh.place(x = row2 + dx_t1,y = col1 + 2*dy_t1)
Button(tab2, bg="#c5ccd1", fg="red",text="set", command=checkCombo_mh).place(x = row2 + dx_t1+50,y = col1 + 2*dy_t1 - 2)

#--------------------- COLUMN 3: Gantry vertical ---------------------------------------
dx_t1 = 650
Label(tab2, text = "GANTRY VER.",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t1-0,y = 40)  
Label(tab2, text = "Current Spd",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t1,y = col1 + dy_t1)  
m3_cur_spd = Label(tab2, text = "----",font=("Arial", 10) ).place(x =row2 + dx_t1,y = col1 + dy_t1)  
Label(tab2, text = "New Spd",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t1,y = col1 + 2*dy_t1)  
combo_mv = ttk.Combobox(tab2,  width=2, font="Verdana 12 ")
combo_mv['values'] = (1,2,3,4,5,"Text")
combo_mv.current(3)
combo_mv.place(x = row2 + dx_t1,y = col1 + 2*dy_t1)
Button(tab2, bg="#c5ccd1", fg="red",text="set", command=checkCombo_mv).place(x = row2 + dx_t1+50,y = col1 + 2*dy_t1 - 2)

#--------------------- COLUMN 4: Gantry vertical ---------------------------------------
x_t2_c3 = 950
col1 = 100
dy_t1 = 40
img = PhotoImage(file='./Mavarel_Demo/Images/led-green-off.png')
img= img.zoom(25)
icon_off = img.subsample(128)

img = PhotoImage(file='./Mavarel_Demo/Images/led-green-on.png')
img= img.zoom(25)
icon_on = img.subsample(128)

Label(tab2, text = "BUBBLE SENSORS",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = x_t2_c3-30,y = 40)  
Label(tab2, text = "BS1",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = x_t2_c3,y = col1 + 0*dy_t1)  
Label(tab2, text = "BS2",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = x_t2_c3,y = col1 + 1*dy_t1)  
Label(tab2, text = "BS3",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = x_t2_c3,y = col1 + 2*dy_t1)  
Label(tab2, text = "BS4",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = x_t2_c3,y = col1 + 3*dy_t1)
Label(tab2, text = "BS5",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = x_t2_c3,y = col1 + 4*dy_t1)
Label(tab2, text = "BS6",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = x_t2_c3,y = col1 + 5*dy_t1)
Label(tab2, text = "BS7",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = x_t2_c3,y = col1 + 6*dy_t1)
Label(tab2, text = "BS8",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = x_t2_c3,y = col1 + 7*dy_t1)
Label(tab2, text = "BS9",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = x_t2_c3,y = col1 + 8*dy_t1)
Label(tab2, text = "BS10",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = x_t2_c3,y = col1 + 9*dy_t1)
Label(tab2, text = "BS11",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = x_t2_c3,y = col1 + 10*dy_t1)
Label(tab2, text = "BS12",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = x_t2_c3,y = col1 + 11*dy_t1)
Label(tab2, text = "BS13",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = x_t2_c3,y = col1 + 12*dy_t1)
Label(tab2, text = "BS14",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = x_t2_c3,y = col1 + 13*dy_t1)

# led_off_1 = Label(tab2, image=icon_off).place(x = x_t2_c3+50,y = col1 + 0*dy_t1)
# led_off_2 = Label(tab2, image=icon_off).place(x = x_t2_c3+50,y = col1 + 1*dy_t1)
# led_off_3 = Label(tab2, image=icon_off).place(x = x_t2_c3+50,y = col1 + 2*dy_t1)
# led_off_4 = Label(tab2, image=icon_off).place(x = x_t2_c3+50,y = col1 + 3*dy_t1)
# led_off_5 = Label(tab2, image=icon_off).place(x = x_t2_c3+50,y = col1 + 4*dy_t1)
# led_off_6 = Label(tab2, image=icon_off).place(x = x_t2_c3+50,y = col1 + 5*dy_t1)
# led_off_7 = Label(tab2, image=icon_off).place(x = x_t2_c3+50,y = col1 + 6*dy_t1)
# led_off_8 = Label(tab2, image=icon_off).place(x = x_t2_c3+50,y = col1 + 7*dy_t1)
# led_off_9 = Label(tab2, image=icon_off).place(x = x_t2_c3+50,y = col1 + 8*dy_t1)
# led_off_10= Label(tab2, image=icon_off).place(x = x_t2_c3+50,y = col1 + 9*dy_t1)
# led_off_11 = Label(tab2, image=icon_off).place(x = x_t2_c3+50,y = col1 + 10*dy_t1)
# led_off_12 = Label(tab2, image=icon_off).place(x = x_t2_c3+50,y = col1 + 11*dy_t1)
# led_off_13 = Label(tab2, image=icon_off).place(x = x_t2_c3+50,y = col1 + 12*dy_t1)
# led_off_14 = Label(tab2, image=icon_off).place(x = x_t2_c3+50,y = col1 + 13*dy_t1)

led_off_1 = Label(tab2, image=icon_off)
led_off_1.pack()
led_off_1.place(x = x_t2_c3+50,y = col1 + 0*dy_t1)

led_off_2 = Label(tab2, image=icon_off)
led_off_2.pack()
led_off_2.place(x = x_t2_c3+50,y = col1 + 1*dy_t1)

led_off_3 = Label(tab2, image=icon_off)
led_off_3.pack()
led_off_3.place(x = x_t2_c3+50,y = col1 + 2*dy_t1)

led_off_4 = Label(tab2, image=icon_off)
led_off_4.pack()
led_off_4.place(x = x_t2_c3+50,y = col1 + 3*dy_t1)

led_off_5 = Label(tab2, image=icon_off)
led_off_5.pack()
led_off_5.place(x = x_t2_c3+50,y = col1 + 4*dy_t1)

led_off_6 = Label(tab2, image=icon_off)
led_off_6.pack()
led_off_6.place(x = x_t2_c3+50,y = col1 + 5*dy_t1)

led_off_7 = Label(tab2, image=icon_off)
led_off_7.pack()
led_off_7.place(x = x_t2_c3+50,y = col1 + 6*dy_t1)

led_off_8 = Label(tab2, image=icon_off)
led_off_8.pack()
led_off_8.place(x = x_t2_c3+50,y = col1 + 7*dy_t1)

led_off_9 = Label(tab2, image=icon_off)
led_off_9.pack()
led_off_9.place(x = x_t2_c3+50,y = col1 + 8*dy_t1)

led_off_10= Label(tab2, image=icon_off)
led_off_10.pack()
led_off_10.place(x = x_t2_c3+50,y = col1 + 9*dy_t1)

led_off_11 = Label(tab2, image=icon_off)
led_off_11.pack()
led_off_11.place(x = x_t2_c3+50,y = col1 + 10*dy_t1)

led_off_12 = Label(tab2, image=icon_off)
led_off_12.pack()
led_off_12.place(x = x_t2_c3+50,y = col1 + 11*dy_t1)

led_off_13 = Label(tab2, image=icon_off)
led_off_13.pack()
led_off_13.place(x = x_t2_c3+50,y = col1 + 12*dy_t1)

led_off_14 = Label(tab2, image=icon_off)
led_off_14.pack()
led_off_14.place(x = x_t2_c3+50,y = col1 + 13*dy_t1)


dd=50
led_on_1 = Label(tab2, image=icon_on)
led_on_1.pack()
led_on_1.place(x = x_t2_c3+50+dd,y = col1 + 0*dy_t1)

led_on_2 = Label(tab2, image=icon_on)
led_on_2.pack()
led_on_2.place(x = x_t2_c3+50+dd,y = col1 + 1*dy_t1)

led_on_3 = Label(tab2, image=icon_on)
led_on_3.pack()
led_on_3.place(x = x_t2_c3+50+dd,y = col1 + 2*dy_t1)

led_on_4 = Label(tab2, image=icon_on)
led_on_4.pack()
led_on_4.place(x = x_t2_c3+50+dd,y = col1 + 3*dy_t1)

led_on_5 = Label(tab2, image=icon_on)
led_on_5.pack()
led_on_5.place(x = x_t2_c3+50+dd,y = col1 + 4*dy_t1)

led_on_6 = Label(tab2, image=icon_on)
led_on_6.pack()
led_on_6.place(x = x_t2_c3+50+dd,y = col1 + 5*dy_t1)

led_on_7 = Label(tab2, image=icon_on)
led_on_7.pack()
led_on_7.place(x = x_t2_c3+50+dd,y = col1 + 6*dy_t1)

led_on_8 = Label(tab2, image=icon_on)
led_on_8.pack()
led_on_8.place(x = x_t2_c3+50+dd,y = col1 + 7*dy_t1)

led_on_9 = Label(tab2, image=icon_on)
led_on_9.pack()
led_on_9.place(x = x_t2_c3+50+dd,y = col1 + 8*dy_t1)

led_on_10= Label(tab2, image=icon_on)
led_on_10.pack()
led_on_10.place(x = x_t2_c3+50+dd,y = col1 + 9*dy_t1)

led_on_11 = Label(tab2, image=icon_on)
led_on_11.pack()
led_on_11.place(x = x_t2_c3+50+dd,y = col1 + 10*dy_t1)

led_on_12 = Label(tab2, image=icon_on)
led_on_12.pack()
led_on_12.place(x = x_t2_c3+50+dd,y = col1 + 11*dy_t1)

led_on_13 = Label(tab2, image=icon_on)
led_on_13.pack()
led_on_13.place(x = x_t2_c3+50+dd,y = col1 + 12*dy_t1)

led_on_14 = Label(tab2, image=icon_on)
led_on_14.pack()
led_on_14.place(x = x_t2_c3+50+dd,y = col1 + 13*dy_t1)


led_on_14.place_forget()






root.mainloop()