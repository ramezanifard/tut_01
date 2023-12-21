# !/usr/bin/python3  
from tkinter import *  
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import threading
import sys

class GUI():
    def __init__(self, root):
        # root.geometry("1200x800+50+50") 
        root.title("DEBUG / MANUAL MODE GUI") 
        root.resizable(False, False)
        # root.overrideredirect(True)

        window_height = 800
        window_width = 1200
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        position_top = int(screen_height/2 -window_height/2)
        position_right = int(screen_width / 2 - window_width/2)
        print('H:', screen_height, 'x W:', screen_width )
        root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
        def disable_event():
            pass
        root.protocol("WM_DELETE_WINDOW", disable_event)
        # root.resizable(width=FALSE, height=FALSE)   

        s = ttk.Style()
        s.theme_create( "MyStyle", parent="alt", settings={
                "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
                "TNotebook.Tab": {"configure": {"padding": [70, 10],
                                                "font" : ('URW Gothic L', '11', 'bold')},}})
        s.theme_use("MyStyle")
        #--------------------- DEFINE TABS ---------------------------------------
        self.tabControl = ttk.Notebook(root) 
        self.tab1 = Frame(self.tabControl) 
        self.tab2 = Frame(self.tabControl)
        self.tab3 = Frame(self.tabControl)
        self.tabControl.add(self.tab1, text ='Pumps/Valves') 
        self.tabControl.add(self.tab2, text ='Motors') 
        self.tabControl.add(self.tab3, text ='Degas Temperature') 
        self.tabControl.pack(expand = 1, fill ="both") 
        #---------------------  PUMP TAB ------------------------------------------------------------------------------------------------------
        
        #------------- Draw Lines -------------------------------------------------
        # # Create a self.canvas2 widget
        self.canvas1=Canvas(self.tab1, width=1200, height=800,bg='#D9D9D9')
        self.canvas1.pack()
        # Add a line in self.canvas1 widget
        self.canvas1.create_line(0,30,1200,30, fill='gray', width=1)
        self.canvas1.create_line(300,170,600,170, fill='gray', width=1)
        self.canvas1.create_line(300,320,600,320, fill='gray', width=1)
        self.canvas1.create_line(300,465,600,465, fill='gray', width=1)
        self.canvas1.create_line(300,610,600,610, fill='gray', width=1)
        self.canvas1.create_line(300,30,300,800, fill='gray', width=1)
        self.canvas1.create_line(600,30,600,800, fill='gray', width=1)
        self.canvas1.create_line(900,30,900,800, fill='gray', width=1)
        self.canvas1.create_line(900,170,1200,170, fill='gray', width=1)
        self.canvas1.create_line(900,320,1200,320, fill='gray', width=1)
        self.canvas1.create_line(900,465,1200,465, fill='gray', width=1)
        self.canvas1.create_line(900,610,1200,610, fill='gray', width=1)
        #--------------------- DEFINE PUMP 1 ---------------------------------------
        dY1 = 50
        XX1 = 50 # first col. of labels
        Y1 = 140
        XX2 = 100 # second col of labels
        XX3 = 60 #  3rd col of labels
        Label(self.tab1, text = "PUMP 1 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = XX1+60,y = 40)          
        self.b_p1_Zinit = Button(self.tab1,text="   Z Init.   ", bg="#c5ccd1", fg="red", font=("Arial", 12),
                                command=self.p1_b_Zinit_click).place(x = XX1-10 ,y = 90)
        self.b_p1_Yinit = Button(self.tab1,text="   Y Init.   ", bg="#c5ccd1", fg="red", font=("Arial", 12),
                                command=self.p1_b_Yinit_click).place(x = XX1+110 ,y = 90)
        Label(self.tab1, text = "Position",font=("Arial", 15), bg='#D9D9D9',fg='black' ).place(x = XX1+70,y = 140)  
        Label(self.tab1, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = XX1,y = Y1 + dY1)  
        self.p1_cur_pos = Label(self.tab1, text = "----",font=("Arial", 10) )
        self.p1_cur_pos.pack()
        self.p1_cur_pos.place(x =XX1 + XX2,y = Y1 + dY1)  
        Label(self.tab1, text = "Absolute Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = XX1,y = Y1 + 2*dY1)  
        self.ent_abs_pos = Entry(self.tab1, width=8)
        self.ent_abs_pos.pack()
        self.ent_abs_pos.place(x = XX1 + XX2,y = Y1 + 2*dY1 ) 
        self.b_abs_pos = Button(self.tab1,text="set", bg="#c5ccd1", fg="red", 
                                command=self.p1_b_abs_pos_click).place(x = XX1 + XX2+60, y = Y1 + 2*dY1 - 2)
        Label(self.tab1, text = "Pickup Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = XX1,y = Y1 + 3*dY1)  
        self.ent_pickup_pos = Entry(self.tab1, width=8) 
        self.ent_pickup_pos.pack()
        self.ent_pickup_pos.place(x = XX1 + XX2,y = Y1 + 3*dY1, )
        self.b_pickup_pos = Button(self.tab1,text="set", bg="#c5ccd1", fg="red", 
                                   command=self.p1_b_pickup_pos_click).place(x = XX1 + XX2+XX3, y = Y1 + 3*dY1 - 2)
        Label(self.tab1, text = "Dispense Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = XX1,y = Y1 + 4*dY1)  
        self.ent_dispemse_pos = Entry(self.tab1, width=8)
        self.ent_dispemse_pos.pack()
        self.ent_dispemse_pos.place(x = XX1 + XX2,y = Y1 + 4*dY1, ) 
        self.b_dispense_pos = Button(self.tab1,text="set", bg="#c5ccd1", fg="red",
                                      command=self.p1_b_dispense_pos_click).place(x = XX1 + XX2+XX3,y = Y1 + 4*dY1 - 2)
        Label(self.tab1, text = "Speed",font=("Arial", 15) , bg='#D9D9D9',fg='black').place(x = XX1+70,y =  Y1 + 5*dY1)  
        Label(self.tab1, text = "Cur Top Spd",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = XX1,y = Y1 + 6*dY1)  
        self.p1_cur_spd = Label(self.tab1, text = "----",font=("Arial", 10) ).place(x =XX1 + XX2,y = Y1 + 6*dY1)  
        Label(self.tab1, text = "Top Speed",font=("Arial", 10), bg='#D9D9D9',fg='black' ).place(x = XX1,y = Y1 + 7*dY1)  
        self.ent_top_spd = Entry(self.tab1, width=8)
        self.ent_top_spd.pack()
        self.ent_top_spd.place(x = XX1 + XX2,y = Y1 + 7*dY1, ) 
        self.b_top_spd = Button(self.tab1,text="set", bg="#c5ccd1", fg="red", 
                                command=self.p1_b_top_spd_click).place(x = XX1 + XX2+XX3,y = Y1 + 7*dY1 - 2)
        # #--------------------- DEFINE PUMP 2 ---------------------------------------
        dY1 = 50
        XX1 = 650
        Y10 = 140
        XX2 = 100
        XX3 = 60 #  3rd col of labels
        Label(self.tab1, text = "PUMP 2 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = XX1 +60,y = 40)  

        self.b_p2_Zinit = Button(self.tab1,text="   Z Init.   ", bg="#c5ccd1", fg="red", font=("Arial", 12),
                                command=self.p2_b_Zinit_click).place(x = XX1 ,y = 90)
        self.b_p2_Yinit = Button(self.tab1,text="   Y Init.   ", bg="#c5ccd1", fg="red", font=("Arial", 12),
                                command=self.p2_b_Yinit_click).place(x = XX1+120 ,y = 90)
        

        Label(self.tab1, text = "Position",font=("Arial", 15), bg='#D9D9D9',fg='black' ).place(x = XX1+70,y = 140)  
        Label(self.tab1, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = XX1,y = Y10 + dY1)  
        self.p_cur_pos2 = Label(self.tab1, text = "----",font=("Arial", 10) ).place(x =XX1 + XX2,y = Y10 + dY1)  
        Label(self.tab1, text = "Absolute Pos",font=("Arial", 10), bg='#D9D9D9',fg='black' ).place(x = XX1,y = Y10 + 2*dY1)  
        self.ent_abs_pos2 = Entry(self.tab1, width=8)
        self.ent_abs_pos2.pack()
        self.ent_abs_pos2.place(x = XX1 + XX2,y = Y10 + 2*dY1 ) 
        self.b_abs_pos2 = Button(self.tab1,text="set", bg="#c5ccd1", fg="red", 
                                 command=self.p2_b_abs_pos_click).place(x = XX1 + XX2+XX3,y = Y10 + 2*dY1 - 2)
        Label(self.tab1, text = "Pickup Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = XX1,y = Y10 + 3*dY1)  
        self.ent_pickup_pos2 = Entry(self.tab1, width=8) 
        self.ent_pickup_pos2.pack()
        self.ent_pickup_pos2.place(x = XX1 + XX2,y = Y10 + 3*dY1, )
        self.b_pickup_pos2 = Button(self.tab1,text="set", bg="#c5ccd1", fg="red", 
                                    command=self.p2_b_pickup_pos_click).place(x = XX1 + XX2+XX3,y = Y10 + 3*dY1 - 2)
        Label(self.tab1, text = "Dispense Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = XX1,y = Y10 + 4*dY1)  
        self.ent_dispemse_pos2 = Entry(self.tab1, width=8)
        self.ent_dispemse_pos2.pack()
        self.ent_dispemse_pos2.place(x = XX1 + XX2,y = Y10 + 4*dY1, ) 
        self.b_dispense_pos2 = Button(self.tab1,text="set", bg="#c5ccd1", fg="red", 
                                      command=self.p2_b_dispense_pos_click).place(x = XX1 + XX2+XX3,y = Y10 + 4*dY1 - 2)
        Label(self.tab1, text = "Speed",font=("Arial", 15) , bg='#D9D9D9',fg='black').place(x = XX1+70,y =  Y10 + 5*dY1)  
        Label(self.tab1, text = "Cur Top Spd",font=("Arial", 10), bg='#D9D9D9',fg='black' ).place(x = XX1,y = Y10 + 6*dY1)  
        self.p1_cur_spd2 = Label(self.tab1, text = "----",font=("Arial", 10) ).place(x =XX1 + XX2,y = Y10 + 6*dY1)  
        Label(self.tab1, text = "Top Speed",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = XX1,y = Y10 + 7*dY1)  
        self.ent_top_spd2 = Entry(self.tab1, width=8)
        self.ent_top_spd2.pack()
        self.ent_top_spd2.place(x = XX1 + XX2,y = Y10 + 7*dY1, ) 
        self.b_top_spd2 = Button(self.tab1,text="set", bg="#c5ccd1", fg="red", 
                                 command=self.p2_b_top_spd_click).place(x = XX1 + XX2 + XX3,y = Y10 + 7*dY1 - 2)
        #---------------------  VALVE   TAB ---------------------------------------
        dY1 = 35
        XX1 = 350  #1st col of labels
        Y1 = 60
        XX2 = 100  #2nd col of labels
        XX3 = 50   #3rd col of labels
        #--------------------- COLUMN 2: VALVES 1,3, 5, 9 ---------------------------------------
        Label(self.tab1, text = "VALVE 1 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = XX1+60,y = 40)  
        Label(self.tab1, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = XX1,y = Y1 + dY1)  
        self.v1_cur_pos = Label(self.tab1, text = "----",font=("Arial", 10) ).place(x =XX1 + XX2,y = Y1 + dY1)  
        Label(self.tab1, text = "New Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = XX1,y = Y1 + 2*dY1)  
        self.combo1 = ttk.Combobox(self.tab1,  width=2, font="Verdana 12 ")
        self.combo1['values'] = (1,2,3,4,5,"Text")
        self.combo1.current(3)
        self.combo1.place(x = XX1 + XX2,y = Y1 + 2*dY1)
        Button(self.tab1, bg="#c5ccd1", fg="red",text="set", command=self.checkCombo1).place(x = XX1 + XX2+XX3,y = Y1 + 2*dY1 - 2)
        yy = 140
        Label(self.tab1, text = "VALVE 3 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = XX1+60,y = yy+Y1-15)  
        Label(self.tab1, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = XX1,y = yy+Y1 + dY1)  
        self.v3_cur_pos = Label(self.tab1, text = "----",font=("Arial", 10) ).place(x =XX1 + XX2,y = yy+Y1 + dY1)  
        Label(self.tab1, text = "New Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = XX1,y = yy+Y1 + 2*dY1)  
        self.combo3 = ttk.Combobox(self.tab1,  width=2, font="Verdana 12 ")
        self.combo3['values'] = (1,2,3,4,5,"Text")
        self.combo3.current(3)
        self.combo3.place(x = XX1 + XX2,y =yy+ Y1 + 2*dY1)
        Button(self.tab1, bg="#c5ccd1", fg="red",text="set", command=self.checkCombo3).place(x = XX1 + XX2+XX3,y =yy+ Y1 + 2*dY1 - 2)
        yy = 283
        Label(self.tab1, text = "VALVE 5 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = XX1+60,y = yy+Y1-15)  
        Label(self.tab1, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = XX1,y = yy+Y1 + dY1)  
        self.v5_cur_pos = Label(self.tab1, text = "----",font=("Arial", 10) ).place(x =XX1 + XX2,y = yy+Y1 + dY1)  
        Label(self.tab1, text = "New Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = XX1,y = yy+Y1 + 2*dY1)  
        self.combo5 = ttk.Combobox(self.tab1,  width=2, font="Verdana 12 ")
        self.combo5['values'] = (1,2,3,4,5,"Text")
        self.combo5.current(3)
        self.combo5.place(x = XX1 + XX2,y =yy+ Y1 + 2*dY1)
        Button(self.tab1, bg="#c5ccd1", fg="red",text="set", command=self.checkCombo5).place(x = XX1 + XX2+XX3,y =yy+ Y1 + 2*dY1 - 2)
        yy = 423
        Label(self.tab1, text = "VALVE 9 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = XX1+60,y = yy+Y1-15)  
        Label(self.tab1, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = XX1,y = yy+Y1 + dY1)  
        self.v5_cur_pos = Label(self.tab1, text = "----",font=("Arial", 10) ).place(x =XX1 + XX2,y = yy+Y1 + dY1)  
        Label(self.tab1, text = "New Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = XX1,y = yy+Y1 + 2*dY1)  
        self.combo9 = ttk.Combobox(self.tab1,  width=2, font="Verdana 12 ")
        self.combo9['values'] = (1,2,3,4,5,"Text")
        self.combo9.current(3)
        self.combo9.place(x = XX1 + XX2,y =yy+ Y1 + 2*dY1)
        Button(self.tab1, bg="#c5ccd1", fg="red",text="set", command=self.checkCombo9).place(x = XX1 + XX2+XX3,y =yy+ Y1 + 2*dY1 - 2)
        #--------------------- COLUMN 4:   VALVES 2, 4, 6, 7, 8 ---------------------------------------
        dx_t2 = 950   
        Label(self.tab1, text = "VALVE 2 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t2 +60,y = 40)  
        Label(self.tab1, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t2,y = Y1 + dY1)  
        self.v2_cur_pos = Label(self.tab1, text = "----",font=("Arial", 10) ).place(x =XX2 + dx_t2,y = Y1 + dY1)  
        Label(self.tab1, text = "New Pos",font=("Arial", 10), bg='#D9D9D9',fg='black' ).place(x = dx_t2,y = Y1 + 2*dY1)  
        self.combo2 = ttk.Combobox(self.tab1,  width=2, font="Verdana 12 ")
        self.combo2['values'] = (1,2,3,4,5,"Text")
        self.combo2.current(3)
        self.combo2.place(x = XX2 + dx_t2,y = Y1 + 2*dY1)
        Button(self.tab1,text="set", bg="#c5ccd1", fg="red", command=self.checkCombo2).place(x =XX2 + dx_t2+XX3,y = Y1 + 2*dY1 - 2)
        yy = 140
        Label(self.tab1, text = "VALVE 4 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t2 +60,y=yy+Y1-15)  
        Label(self.tab1, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t2,y = yy+Y1 + dY1)  
        self.v4_cur_pos = Label(self.tab1, text = "----",font=("Arial", 10) ).place(x =XX2 + dx_t2,y = yy+Y1 + dY1)  
        Label(self.tab1, text = "New Pos",font=("Arial", 10), bg='#D9D9D9',fg='black' ).place(x = dx_t2,y = yy+Y1 + 2*dY1)  
        self.combo4 = ttk.Combobox(self.tab1,  width=2, font="Verdana 12 ")
        self.combo4['values'] = (1,2,3,4,5,"Text")
        self.combo4.current(3)
        self.combo4.place(x = XX2 + dx_t2,y = yy+Y1 + 2*dY1)
        Button(self.tab1,text="set2", bg="#c5ccd1", fg="red", command=self.checkCombo4).place(x =XX2 + dx_t2+XX3,y = yy+Y1 + 2*dY1)
        yy = 283
        Label(self.tab1, text = "VALVE 6 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t2 +60,y=yy+Y1-15)  
        Label(self.tab1, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t2,y = yy+Y1 + dY1)  
        self.v6_cur_pos = Label(self.tab1, text = "----",font=("Arial", 10) ).place(x =XX2 + dx_t2,y = yy+Y1 + dY1)  
        Label(self.tab1, text = "New Pos",font=("Arial", 10), bg='#D9D9D9',fg='black' ).place(x = dx_t2,y = yy+Y1 + 2*dY1)  
        self.combo6 = ttk.Combobox(self.tab1,  width=2, font="Verdana 12 ")
        self.combo6['values'] = (1,2,3,4,5,"Text")
        self.combo6.current(3)
        self.combo6.place(x = XX2 + dx_t2,y = yy+Y1 + 2*dY1)
        Button(self.tab1,text="set", bg="#c5ccd1", fg="red", command=self.checkCombo6).place(x =XX2 + dx_t2+XX3,y = yy+Y1 + 2*dY1)
        yy = 423
        Label(self.tab1, text = "VALVE 7 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t2 +60,y=yy+Y1-15)  
        Label(self.tab1, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t2,y = yy+Y1 + dY1)  
        self.v7_cur_pos = Label(self.tab1, text = "----",font=("Arial", 10) ).place(x =XX2 + dx_t2,y = yy+Y1 + dY1)  
        Label(self.tab1, text = "New Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t2,y = yy+Y1 + 2*dY1)  
        self.combo7 = ttk.Combobox(self.tab1,  width=2, font="Verdana 12 ")
        self.combo7['values'] = (1,2,3,4,5,"Text")
        self.combo7.current(3)
        self.combo7.place(x = XX2 + dx_t2,y =yy+ Y1 + 2*dY1)
        Button(self.tab1, bg="#c5ccd1", fg="red",text="set", command=self.checkCombo7).place(x =XX2 + dx_t2+XX3,y =yy+ Y1 + 2*dY1 - 2)
        yy = 566
        Label(self.tab1, text = "VALVE 8 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = dx_t2 +60,y=yy+Y1-15)  
        Label(self.tab1, text = "Current Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t2,y = yy+Y1 + dY1)  
        self.v8_cur_pos = Label(self.tab1, text = "----",font=("Arial", 10) ).place(x =XX2 + dx_t2,y = yy+Y1 + dY1)  
        Label(self.tab1, text = "New Pos",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = dx_t2,y = yy+Y1 + 2*dY1)  
        self.combo8 = ttk.Combobox(self.tab1,  width=2, font="Verdana 12 ")
        self.combo8['values'] = (1,2,3,4,5,"Text")
        self.combo8.current(3)
        self.combo8.place(x = XX2 + dx_t2,y =yy+ Y1 + 2*dY1)
        Button(self.tab1, bg="#c5ccd1", fg="red",text="set", command=self.checkCombo8).place(x =XX2 + dx_t2+XX3,y =yy+ Y1 + 2*dY1 - 2)

        # #---------------------  MOTORS TAB ---------------------------------------
        # # Create a canvas widget
        self.canvas2=Canvas(self.tab2, width=1200, height=800,bg='#D9D9D9')
        self.canvas2.pack()
        # Add a line in self.canvas2 widget
        self.canvas2.create_line(0,30,1200,30, fill='gray', width=1)
        self.canvas2.create_line(300,30,300,800, fill='gray', width=1)
        self.canvas2.create_line(600,30,600,800, fill='gray', width=1)
        self.canvas2.create_line(900,30,900,800, fill='gray', width=1)
        #--------------------- COLUMN1:  Motor 1 ---------------------------------------
        dY1 = 50
        XX1 = 50
        Y1 = 140
        XX2 = 100
        Label(self.tab2, text = "MOTOR 1 ",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = XX1+40,y = 40)  
        Label(self.tab2, text = "Current Spd",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = XX1,y = Y1 + dY1)  
        self.m1_cur_spd = Label(self.tab2, text = "----",font=("Arial", 10) ).place(x =XX1 + XX2,y = Y1 + dY1)  
        Label(self.tab2, text = "New Spd",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = XX1,y = Y1 + 2*dY1)  
        self.ent_m1_spd_ = Entry(self.tab2, width=8)
        self.ent_m1_spd_.pack()
        self.ent_m1_spd_.place(x = XX1 + XX2,y = Y1 + 2*dY1 ) 
        self.b_m1_spd = Button(self.tab2,text="set", bg="#c5ccd1", fg="red", command=self.m1_b_abs_pos_click).place(x = XX1 + XX2+XX3,
                                                                                                y = Y1 + 2*dY1 - 2)
        #--------------------- COLUMN 2: Gantry Horizontal ---------------------------------------
        XX1 = 350
        Label(self.tab2, text = "GANTRY HORIZ.",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = XX1-10,y = 40)  
        Label(self.tab2, text = "Current Spd",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = XX1,y = Y1 + dY1)  
        self.m2_cur_spd = Label(self.tab2, text = "----",font=("Arial", 10) ).place(x =XX1 + XX2,y = Y1 + dY1)  
        Label(self.tab2, text = "New Spd",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = XX1,y = Y1 + 2*dY1)  
        self.combo_mh = ttk.Combobox(self.tab2,  width=2, font="Verdana 12 ")
        self.combo_mh['values'] = (1,2,3,4,5,"Text")
        self.combo_mh.current(3)
        self.combo_mh.place(x = XX1 + XX2,y = Y1 + 2*dY1)
        Button(self.tab2, bg="#c5ccd1", fg="red",text="set", command=self.checkCombo_mh).place(x = XX1 + XX2+50,y = Y1 + 2*dY1 - 2)
        #--------------------- COLUMN 3: Gantry vertical ---------------------------------------
        XX1 = 650
        Label(self.tab2, text = "GANTRY VER.",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = XX1-0,y = 40)  
        Label(self.tab2, text = "Current Spd",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = XX1,y = Y1 + dY1)  
        self.m3_cur_spd = Label(self.tab2, text = "----",font=("Arial", 10) ).place(x =XX1 + XX2,y = Y1 + dY1)  
        Label(self.tab2, text = "New Spd",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = XX1,y = Y1 + 2*dY1)  
        self.combo_mv = ttk.Combobox(self.tab2,  width=2, font="Verdana 12 ")
        self.combo_mv['values'] = (1,2,3,4,5,"Text")
        self.combo_mv.current(3)
        self.combo_mv.place(x = XX1 + XX2,y = Y1 + 2*dY1)
        Button(self.tab2, bg="#c5ccd1", fg="red",text="set", command=self.checkCombo_mv).place(x = XX1 + XX2+50,y = Y1 + 2*dY1 - 2)
        # #--------------------- COLUMN 4: BUBBLE SENSORS ---------------------------------------
        X3 = 950
        Y1 = 100
        dY1 = 40

        image1 = Image.open('./Mavarel_Demo/Images/led-green-off.png')
        image1 = image1.resize((24, 24))
        icon_off = ImageTk.PhotoImage(image1)
        image1 = Image.open('./Mavarel_Demo/Images/led-green-on.png')
        image1 = image1.resize((24, 24))
        icon_on = ImageTk.PhotoImage(image1)

        Label(self.tab2, text = "BUBBLE SENSORS",font=("Arial", 20) , bg='#D9D9D9',fg='black').place(x = X3-30,y = 40)  
        Label(self.tab2, text = "BS1",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = X3,y = Y1 + 0*dY1)  
        Label(self.tab2, text = "BS2",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = X3,y = Y1 + 1*dY1)  
        Label(self.tab2, text = "BS3",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = X3,y = Y1 + 2*dY1)  
        Label(self.tab2, text = "BS4",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = X3,y = Y1 + 3*dY1)
        Label(self.tab2, text = "BS5",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = X3,y = Y1 + 4*dY1)
        Label(self.tab2, text = "BS6",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = X3,y = Y1 + 5*dY1)
        Label(self.tab2, text = "BS7",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = X3,y = Y1 + 6*dY1)
        Label(self.tab2, text = "BS8",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = X3,y = Y1 + 7*dY1)
        Label(self.tab2, text = "BS9",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = X3,y = Y1 + 8*dY1)
        Label(self.tab2, text = "BS10",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = X3,y = Y1 + 9*dY1)
        Label(self.tab2, text = "BS11",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = X3,y = Y1 + 10*dY1)
        Label(self.tab2, text = "BS12",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = X3,y = Y1 + 11*dY1)
        Label(self.tab2, text = "BS13",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = X3,y = Y1 + 12*dY1)
        Label(self.tab2, text = "BS14",font=("Arial", 10) , bg='#D9D9D9',fg='black').place(x = X3,y = Y1 + 13*dY1)
        self.led_off_1 = Label(self.tab2, image=icon_off)
        self.led_off_1.image = icon_off
        self.led_off_1.place(x = X3+50,y = Y1 + 0*dY1)
        self.led_off_2 = Label(self.tab2, image=icon_off)
        self.led_off_2.image = icon_off
        self.led_off_2.place(x = X3+50,y = Y1 + 1*dY1)
        self.led_off_2 = Label(self.tab2, image=icon_off)
        self.led_off_2.image = icon_off
        self.led_off_2.place(x = X3+50,y = Y1 + 2*dY1)
        self.led_off_2 = Label(self.tab2, image=icon_off)
        self.led_off_2.image = icon_off
        self.led_off_2.place(x = X3+50,y = Y1 + 3*dY1)
        self.led_off_2 = Label(self.tab2, image=icon_off)
        self.led_off_2.image = icon_off
        self.led_off_2.place(x = X3+50,y = Y1 + 4*dY1)
        self.led_off_2 = Label(self.tab2, image=icon_off)
        self.led_off_2.image = icon_off
        self.led_off_2.place(x = X3+50,y = Y1 + 5*dY1)
        self.led_off_2 = Label(self.tab2, image=icon_off)
        self.led_off_2.image = icon_off
        self.led_off_2.place(x = X3+50,y = Y1 + 6*dY1)
        self.led_off_2 = Label(self.tab2, image=icon_off)
        self.led_off_2.image = icon_off
        self.led_off_2.place(x = X3+50,y = Y1 + 7*dY1)
        self.led_off_2 = Label(self.tab2, image=icon_off)
        self.led_off_2.image = icon_off
        self.led_off_2.place(x = X3+50,y = Y1 + 8*dY1)
        self.led_off_2 = Label(self.tab2, image=icon_off)
        self.led_off_2.image = icon_off
        self.led_off_2.place(x = X3+50,y = Y1 + 9*dY1)
        self.led_off_2 = Label(self.tab2, image=icon_off)
        self.led_off_2.image = icon_off
        self.led_off_2.place(x = X3+50,y = Y1 + 10*dY1)
        self.led_off_2 = Label(self.tab2, image=icon_off)
        self.led_off_2.image = icon_off
        self.led_off_2.place(x = X3+50,y = Y1 + 11*dY1)
        self.led_off_2 = Label(self.tab2, image=icon_off)
        self.led_off_2.image = icon_off
        self.led_off_2.place(x = X3+50,y = Y1 + 12*dY1)
        self.led_off_2 = Label(self.tab2, image=icon_off)
        self.led_off_2.image = icon_off
        self.led_off_2.place(x = X3+50,y = Y1 + 13*dY1)

        dd=50
        self.led_on_1  = Label(self.tab2, image=icon_on)
        self.led_on_1 .image = icon_on
        self.led_on_1 .place(x =X3+50+dd,y = Y1 + 0*dY1)
        self.led_on_2  = Label(self.tab2, image=icon_on)
        self.led_on_2.image = icon_on
        self.led_on_2.place(x = X3+50+dd,y = Y1 + 1*dY1)
        self.led_on_3  = Label(self.tab2, image=icon_on)
        self.led_on_3.image = icon_on
        self.led_on_3.place(x = X3+50+dd,y = Y1 + 2*dY1)        
        self.led_on_4  = Label(self.tab2, image=icon_on)
        self.led_on_4.image = icon_on
        self.led_on_4.place(x = X3+50+dd,y = Y1 + 3*dY1)        
        self.led_on_5  = Label(self.tab2, image=icon_on)
        self.led_on_5.image = icon_on
        self.led_on_5.place(x = X3+50+dd,y = Y1 + 4*dY1)
        self.led_on_6  = Label(self.tab2, image=icon_on)
        self.led_on_6.image = icon_on
        self.led_on_6.place(x = X3+50+dd,y = Y1 + 5*dY1)
        self.led_on_7  = Label(self.tab2, image=icon_on)
        self.led_on_7.image = icon_on
        self.led_on_7.place(x = X3+50+dd,y = Y1 + 6*dY1)
        self.led_on_8  = Label(self.tab2, image=icon_on)
        self.led_on_8.image = icon_on
        self.led_on_8.place(x = X3+50+dd,y = Y1 + 7*dY1)
        self.led_on_9  = Label(self.tab2, image=icon_on)
        self.led_on_9.image = icon_on
        self.led_on_9.place(x = X3+50+dd,y = Y1 + 8*dY1)        
        self.led_on_10  = Label(self.tab2, image=icon_on)
        self.led_on_10.image = icon_on
        self.led_on_10.place(x = X3+50+dd,y = Y1 + 9*dY1)        
        self.led_on_11  = Label(self.tab2, image=icon_on)
        self.led_on_11.image = icon_on
        self.led_on_11.place(x = X3+50+dd,y = Y1 + 10*dY1)
        self.led_on_12  = Label(self.tab2, image=icon_on)
        self.led_on_12.image = icon_on
        self.led_on_12.place(x = X3+50+dd,y = Y1 + 11*dY1)
        self.led_on_13  = Label(self.tab2, image=icon_on)
        self.led_on_13.image = icon_on
        self.led_on_13.place(x = X3+50+dd,y = Y1 + 12*dY1)
        self.led_on_14  = Label(self.tab2, image=icon_on)
        self.led_on_14.image = icon_on
        self.led_on_14.place(x = X3+50+dd,y = Y1 + 13*dY1)



        self.b_exit = Button(self.tab3,text="Exit", bg="#c5ccd1", fg="red",font=("Arial", 20),
                             height=2, width=20, command=self.checkExitButton).place(x =400,y = 600)
        
        # button1 = Button(self.tab3, text = "Send", command = self.checkExitButton, height = 100, width = 100) 


        # led_on_14.place_forget()
        # Clock.schedule_interval(self.timerCallback_1, .5)
        self.timer = threading.Timer(1.0, self.timerCallback_1)
        # self.timer.start()


    #--------------------------------------------------------------------------------------------------------
    #--------------------- DEFINE CALLBACK FUNCTIONS FOR PUMPS BUTTONS ---------------------------------------

    def timerCallback_1(self):  
        print('timer tick')
        self.timer = threading.Timer(1.0, self.timerCallback_1)
        self.timer.start()


    def checkExitButton(self):
        print("exit button pressed ...")
        self.timer.cancel()
        # self.root.destroy()
        sys.exit(0)

    def p1_b_Zinit_click(self):
         print("p1 Z initialized")

    def p1_b_Yinit_click(self):
         print("p1 Y initialized")

    def p2_b_Zinit_click(self):
         print("p2 Z initialized")

    def p2_b_Yinit_click(self):
         print("p2 Y initialized")

    def p1_b_abs_pos_click(self):
        print("p1_abs pos")
        s =   self.ent_abs_pos.get()
        print(s)
        # self.p1_cur_pos["text"]=  s

    def p1_b_pickup_pos_click(self):
        print("p1_pickup ")
        s =   self.ent_pickup_pos.get()
        print(s)

    def p1_b_dispense_pos_click(self):
        print("p1_dispense ")
        s =   self.ent_dispemse_pos.get()
        print(s)

    def p1_b_top_spd_click(self):
        print("p1_top speed")
        s =   self.ent_top_spd.get()
        print(s)

    def p2_b_abs_pos_click(self):
        print("p2_abs pos")
        s =   self.ent_abs_pos2.get()
        print(s)

    def p2_b_pickup_pos_click(self):
        print("p2_pickup ")
        s =   self.ent_pickup_pos2.get()
        print(s)

    def p2_b_dispense_pos_click(self):
        print("p2_dispense ")
        s =   self.ent_dispemse_pos2.get()
        print(s)

    def p2_b_top_spd_click(self):
        print("p2_top speed")
        s =   self.ent_top_spd2.get()
        print(s)
    #--------------------- DEFINE CALLBACK FUNCTIONS FOR VALVES BUTTONS ---------------------------------------
    def checkCombo1(self):
        print('-->'+self.combo1.get())

    def checkCombo3(self):
        print('-->'+self.combo3.get())

    def checkCombo5(self):
        print('-->'+self.combo5.get())

    def checkCombo9(self):
        print('-->'+self.combo9.get())        

    def checkCombo2(self):
        print('-->'+self.combo2.get())  

    def checkCombo4(self):
        print('-->'+self.combo4.get()) 

    def checkCombo6(self):
        print('-->'+self.combo6.get()) 

    def checkCombo7(self):
        print('-->'+self.combo7.get()) 

    def checkCombo8(self):
        print('-->'+self.combo8.get()) 
    #--------------------- DEFINE CALLBACK FUNCTIONS FOR BUTTONS ---------------------------------------
    def m1_b_abs_pos_click(self):
        print("m1_new_spd")
        s =   self.ent_m1_spd_.get()
        print(s)

    def checkCombo_mh(self):
        print('-->'+self.combo_mh.get())

    def checkCombo_mv(self):
        print('-->'+self.combo_mv.get())




# def main(): #run mianloop 
#     root = Tk()
#     app = GUI(root)
#     root.mainloop()

if __name__ == '__main__':
    # main()
    root = Tk()
    app = GUI(root)
    root.mainloop()
