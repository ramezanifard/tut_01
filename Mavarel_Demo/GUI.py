# !/usr/bin/python3  
from tkinter import *  
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import sys

class GUI():
      def __init__(self, root):
            Font1 = 'sans 13' # fixed label text font
            Font2 = 'sans 11 italic' #variable label text font
            Font3 = 'sans 15'  # titles label text font 
            Font4 = 'sans 20'  # large title labels text font
            Font5 = 'Arial 16'  #valves title label text font
            Font6 = "Verdana 10 " # combo box text font
            Font7 = "Arial 14" # larger text for terminate/start/stop buttons

            Color1 = '#D9D9D9'  #label background color (gray)
            Color2 = "#c5ccd1"  #Button bg color (gray)
            Color3 = "red"   # buttons text color

            Title_large = 'red'
            Title_mid = 'blue'

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
            self.tab3 = Frame(self.tabControl, bg=Color1)
            self.tabControl.add(self.tab1, text ='Pumps/Valves') 
            self.tabControl.add(self.tab2, text ='Motors') 
            self.tabControl.add(self.tab3, text ='Config.') 
            self.tabControl.pack(expand = 1, fill ="both") 
            #---------------------  PUMP TAB ----------------------------------------------------
            
            #------------- Draw Lines -------------------------------------------------
            # # Create a self.canvas2 widget
            self.canvas1=Canvas(self.tab1, width=1200, height=800,bg=Color1)
            self.canvas1.pack()
            # Add a line in self.canvas1 widget
            self.canvas1.create_line(0,5,1200,5, fill='gray', width=1)      #horizontal 
            self.canvas1.create_line(0,65,1000,65, fill='gray', width=1)      #horizontal col 2
            self.canvas1.create_line(0,67,1000,67, fill='gray', width=1)      #horizontal col 2
            self.canvas1.create_line(250,190,500,190, fill='gray', width=1)      #horizontal col 2
            self.canvas1.create_line(250,315,500,315, fill='gray', width=1)      #horizontal col 2
            self.canvas1.create_line(250,440,500,440, fill='gray', width=1)      #horizontal col 2
            self.canvas1.create_line(250,565,500,565, fill='gray', width=1)      #horizontal col 2

            self.canvas1.create_line(250,5,250,800, fill='gray', width=1)  #vertical
            self.canvas1.create_line(500,5,500,800, fill='gray', width=1)  #vertical
            self.canvas1.create_line(750,5,750,800, fill='gray', width=1)  #vertical
            self.canvas1.create_line(1000,5,1000,800, fill='gray', width=1)  #vertical

            # self.canvas1.create_line(750,65,1000,65, fill='gray', width=1)      #horizontal col 4
            # self.canvas1.create_line(750,67,1000,67, fill='gray', width=1)      #horizontal col 4
            self.canvas1.create_line(750,190,1000,190, fill='gray', width=1)      #horizontal col 4
            self.canvas1.create_line(750,315,1000,315, fill='gray', width=1)      #horizontal col 4
            self.canvas1.create_line(750,440,1000,440, fill='gray', width=1)      #horizontal col 4
            self.canvas1.create_line(750,565,1000,565, fill='gray', width=1)      #horizontal col 4
            
            #--------------------- DEFINE PUMP 1 --------------------------------------

            dY1 = 42
            XX1 = 20 # first col. of labels
            Y1 = 150
            XX2 = 120 # second col of labels
            XX3 = 60 #  3rd col of labels
            Label(self.tab1, text = "PUMP 1",font=Font4 , bg=Color1, 
                  fg= Title_large).place(x = XX1+60,y = 10)  
            Label(self.tab1, text = "Pump Config.",font=Font3, bg=Color1,
                  fg=Title_mid ).place(x = XX1+60,y = 80)           
            self.comboCfg1 = ttk.Combobox(self.tab1,  width=26, font=Font6)
            self.comboCfg1['values'] = ("1) 60mm x 1000 ul full steps","2) 60mm x 1000 ul micro steps",
                                          "3) 60mm x 500 ul full steps","4) 60mm x 500 ul micro steps",
                                          "5) 60mm x 250 ul full steps,", "6) 60mm x 250 ul micro steps",
                                          "7) 30mm x 2500 ul full steps", "8) 30mm x 2500 ul micro steps",
                                          "9) Full steps", "10) Microsteps")
            self.comboCfg1.current(0)
            self.comboCfg1.place(x = XX1+0 ,y = Y1-40)
            self.comboCfg1.bind("<<ComboboxSelected>>", self.checkComboCfg1)
            Label(self.tab1, text = "Position",font=Font3, bg=Color1,
                  fg=Title_mid ).place(x = XX1+70,y =Y1-0)  
            Label(self.tab1, text = "Current Pos",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = Y1 + dY1)  
            self.p1_cur_pos = Label(self.tab1, text = "----",font=Font2 )
            self.p1_cur_pos.pack()
            self.p1_cur_pos.place(x =XX1 + XX2,y = Y1 + dY1)  
            Label(self.tab1, text = "Absolute Pos",font=Font1 , bg=Color1
                  ,fg='black').place(x = XX1,y = Y1 + 2*dY1)  
            self.ent_abs_pos = Entry(self.tab1, width=8)
            self.ent_abs_pos.pack()
            self.ent_abs_pos.place(x = XX1 + XX2,y = Y1 + 2*dY1 ) 
            self.b_abs_pos = Button(self.tab1,text="set", bg=Color2, fg=Color3, 
                                    command=self.p1_b_abs_pos_click).place(x = XX1 + XX2+60, 
                                                                        y = Y1 + 2*dY1 - 2)
            Label(self.tab1, text = "Pickup Pos",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = Y1 + 3*dY1)  
            self.ent_pickup_pos = Entry(self.tab1, width=8) 
            self.ent_pickup_pos.pack()
            self.ent_pickup_pos.place(x = XX1 + XX2,y = Y1 + 3*dY1, )
            self.b_pickup_pos = Button(self.tab1,text="set", bg=Color2, 
                                    fg=Color3,command=self.p1_b_pickup_pos_click).place(x = XX1 + XX2+XX3, 
                                                                              y = Y1 + 3*dY1 - 2)
            Label(self.tab1, text = "Dispense Pos",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = Y1 + 4*dY1)  
            self.ent_dispemse_pos = Entry(self.tab1, width=8)
            self.ent_dispemse_pos.pack()
            self.ent_dispemse_pos.place(x = XX1 + XX2,y = Y1 + 4*dY1, ) 
            self.b_dispense_pos = Button(self.tab1,text="set", bg=Color2, fg=Color3,
                                          command=self.p1_b_dispense_pos_click).place(x = XX1 + XX2+XX3,
                                                                                    y = Y1 + 4*dY1 - 2)
            Label(self.tab1, text = "Speed",font=Font3 , bg=Color1,
                  fg=Title_mid).place(x = XX1+70,y =  Y1 + 5.5*dY1)  
            Label(self.tab1, text = "Cur Top Spd",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = Y1 + 6.5*dY1)  
            self.p1_cur_spd = Label(self.tab1, text = "----",font=Font2 )
            self.p1_cur_spd.pack()
            self.p1_cur_spd.place(x =XX1 + XX2,y = Y1 + 6.5*dY1)  
            Label(self.tab1, text = "Top Speed",font=Font1, bg=Color1,
                  fg='black' ).place(x = XX1,y = Y1 + 7.5*dY1)  
            self.ent_top_spd = Entry(self.tab1, width=8)
            self.ent_top_spd.pack()
            self.ent_top_spd.place(x = XX1 + XX2,y = Y1 + 7.5*dY1 ) 
            self.b_top_spd = Button(self.tab1,text="set", bg=Color2, fg=Color3, 
                                    command=self.p1_b_top_spd_click).place(x = XX1 + XX2+XX3,
                                                                        y = Y1 + 7.5*dY1 - 2)
            
            Label(self.tab1, text = "Until Bubble Sensor",font=Font3 , bg=Color1,
                  fg=Title_mid).place(x = XX1+15 ,y = Y1 + 9*dY1)  
            Label(self.tab1, text = "Select BS",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = Y1 + 10*dY1)  
            self.combo0 = ttk.Combobox(self.tab1,  width=5, font=Font6)
            self.combo0['values'] = ("BS1","BS2","BS3","BS4","BS5","BS6","BS7","BS8"
                                    ,"BS9","BS10","BS11","BS12","BS13","BS14")
            self.combo0.current(0)
            self.combo0.place(x = XX1 + XX2,y = Y1 + 10*dY1)
            self.combo0.bind("<<ComboboxSelected>>", self.checkCombo0)
            Label(self.tab1, text = "Pickup mode",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = Y1 + 11*dY1)  
            self.b_pickupUntillbubble = Button(self.tab1,
                                                text="   start   ", bg=Color2, fg=Color3,font=("Arial", 10),
                                                command=self.p1_b_pickupUntillbubble).place(x = XX1 + XX2,
                                                                                          y = Y1 + 11*dY1)
            Label(self.tab1, text = "Dispense mode",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = Y1 + 12*dY1)  
            self.b_dispenseUntillbubble = Button(self.tab1,text="   start   ", bg=Color2, 
                                                fg=Color3,font=("Arial", 10),
                                                command=self.p1_b_dispenseUntillbubble).place(x = XX1 + XX2,
                                                                                                y = Y1 + 12*dY1)
            
            self.b_terminatedP1 = Button(self.tab1,text="     Terminate      ", bg=Color2, fg=Color3,
                                          font=Font7,command=self.p1_b_teminateP1).place(x = XX1+ 20,
                                                                                                y = Y1 + 13*dY1)

            # #--------------------- DEFINE PUMP 2 ---------------------------------------
            dY1 = 42
            XX1 = 520
            Y10 = 150#200
            XX2 = 120
            XX3 = 60 #  3rd col of labels
            Label(self.tab1, text = "PUMP 2",font=Font4 , bg=Color1,
                  fg=Title_large).place(x = XX1+60,y = 10)          
            Label(self.tab1, text = "Pump Config.",font=Font3, bg=Color1,
                  fg=Title_mid ).place(x = XX1+60,y = 80)           
            self.comboCfg2 = ttk.Combobox(self.tab1,  width=26, font=Font6)
            self.comboCfg2['values'] = ("1) 60mm x 1000 ul full steps","2) 60mm x 1000 ul micro steps",
                                          "3) 60mm x 500 ul full steps","4) 60mm x 500 ul micro steps",
                                          "5) 60mm x 250 ul full steps,", "6) 60mm x 250 ul micro steps",
                                          "7) 30mm x 2500 ul full steps", "8) 30mm x 2500 ul micro steps",
                                          "9) Full steps", "10) Microsteps")
            self.comboCfg2.current(0)
            self.comboCfg2.place(x = XX1+0 ,y = Y1-40)
            self.comboCfg2.bind("<<ComboboxSelected>>", self.checkComboCfg2)        

            Label(self.tab1, text = "Position",font=Font3, bg=Color1,
                  fg=Title_mid ).place(x = XX1+70,y = Y10-0)  
            Label(self.tab1, text = "Current Pos",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = Y10 + dY1)  
            self.p_cur_pos2 = Label(self.tab1, text = "----",font=Font2 ).place(x =XX1 + XX2,
                                                                                          y = Y10 + dY1)  
            Label(self.tab1, text = "Absolute Pos",font=Font1, bg=Color1,
                  fg='black' ).place(x = XX1,y = Y10 + 2*dY1)  
            self.ent_abs_pos2 = Entry(self.tab1, width=8)
            self.ent_abs_pos2.pack()
            self.ent_abs_pos2.place(x = XX1 + XX2,y = Y10 + 2*dY1 ) 
            self.b_abs_pos2 = Button(self.tab1,text="set", bg=Color2, fg=Color3, 
                                    command=self.p2_b_abs_pos_click).place(x = XX1 + XX2+XX3,
                                                                              y = Y10 + 2*dY1 - 2)
            Label(self.tab1, text = "Pickup Pos",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = Y10 + 3*dY1)  
            self.ent_pickup_pos2 = Entry(self.tab1, width=8) 
            self.ent_pickup_pos2.pack()
            self.ent_pickup_pos2.place(x = XX1 + XX2,y = Y10 + 3*dY1, )
            self.b_pickup_pos2 = Button(self.tab1,text="set", bg=Color2, fg=Color3, 
                                          command=self.p2_b_pickup_pos_click).place(x = XX1 + XX2+XX3,
                                                                                    y = Y10 + 3*dY1 - 2)
            Label(self.tab1, text = "Dispense Pos",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = Y10 + 4*dY1)  
            self.ent_dispemse_pos2 = Entry(self.tab1, width=8)
            self.ent_dispemse_pos2.pack()
            self.ent_dispemse_pos2.place(x = XX1 + XX2,y = Y10 + 4*dY1, ) 
            self.b_dispense_pos2 = Button(self.tab1,text="set", bg=Color2, fg=Color3, 
                                          command=self.p2_b_dispense_pos_click).place(x = XX1 + XX2+XX3,
                                                                                    y = Y10 + 4*dY1 - 2)
            Label(self.tab1, text = "Speed",font=Font3 , bg=Color1,
                  fg=Title_mid).place(x = XX1+70,y =  Y10 + 5.5*dY1)  
            Label(self.tab1, text = "Cur Top Spd",font=Font1, bg=Color1,
                  fg='black' ).place(x = XX1,y = Y10 + 6.5*dY1)  
            self.p1_cur_spd2 = Label(self.tab1, text = "----",font=Font2 ).place(x =XX1 + XX2,
                                                                                          y = Y10 + 6.5*dY1)  
            Label(self.tab1, text = "Top Speed",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = Y10 + 7.5*dY1)  
            self.ent_top_spd2 = Entry(self.tab1, width=8)
            self.ent_top_spd2.pack()
            self.ent_top_spd2.place(x = XX1 + XX2,y = Y10 + 7.5*dY1, ) 
            self.b_top_spd2 = Button(self.tab1,text="set", bg=Color2, fg=Color3, 
                                    command=self.p2_b_top_spd_click).place(x = XX1 + XX2 + XX3,
                                                                              y = Y10 + 8*dY1 - 2)
            
            Label(self.tab1, text = "Until Bubble Sensor",font=Font3 , bg=Color1,
                  fg=Title_mid).place(x = XX1+15 ,y = Y1 + 9*dY1)  
            
            Label(self.tab1, text = "Select BS",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = Y1 + 10*dY1)  
            self.combob1 = ttk.Combobox(self.tab1,  width=5, font=Font6)
            self.combob1['values'] = ("BS1","BS2","BS3","BS4","BS5","BS6","BS7",
                                    "BS8","BS9","BS10","BS11","BS12","BS13","BS14")
            self.combob1.current(0)
            self.combob1.place(x = XX1 + XX2,y = Y1 + 10*dY1)
            self.combob1.bind("<<ComboboxSelected>>", self.checkCombob1)


            Label(self.tab1, text = "Pickup mode",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = Y1 + 11*dY1)  

            Label(self.tab1, text = "Dispense mode",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = Y1 + 12*dY1)          
            self.b_terminatedP2 = Button(self.tab1,text="     Terminate      ", 
                                          bg=Color2, fg=Color3,font=Font7,
                                          command=self.p1_b_teminateP2).place(x = XX1+ 20, 
                                                                              y = Y1 + 13*dY1)

            

            #---------------------  VALVE   TAB ---------------------------------------
            dY1 = 30
            XX1 = 265  #1st col of labels
            Y1 = 90
            XX2 = 110  #2nd col of labels
            XX3 = 50   #3rd col of labels
            #--------------------- COLUMN 2: VALVES 1,3, 5, 9 ---------------------------------------

            Label(self.tab1, text = "TITRANT LINE",font=Font4 , bg=Color1,
                  fg=Title_large).place(x = XX1+10,y = Y1-80)  
            Label(self.tab1, text = "1: PUMP VALVE",font=Font5 , bg=Color1,
                  fg=Title_mid).place(x = XX1+25,y = Y1-10)  
            # Label(self.tab1, text = "Current Pos",font=Font1 , bg=Color1,
            Label(self.tab1, text = "Current Pos",font=Font1, bg=Color1,
                  fg='black').place(x = XX1,y = Y1 + dY1)  
            self.v1_cur_pos = Label(self.tab1, text = "----",font=Font2 )
            self.v1_cur_pos.pack()
            self.v1_cur_pos.place(x =XX1 + XX2-14,y = Y1 + dY1)  
            Label(self.tab1, text = "New Pos",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = Y1 + 2*dY1)  
            self.combo1 = ttk.Combobox(self.tab1,  width=15, font=Font6)
            # self.combo1['values'] = (" I"," O"," B"," E")
            self.combo1['values'] = ("Pump to Air (P1)","Air to Gas (P2)","Gas to Line (P3)",
                                    "Line to Pump (P4)")
            self.combo1.current(0)
            self.combo1.place(x = XX1 + XX2-20,y = Y1 + 2*dY1)
            self.combo1.bind("<<ComboboxSelected>>", self.checkCombo1)  
            
            yy = 125
            Label(self.tab1, text = "3: LOOP VALVE",font=Font5 , bg=Color1,
                  fg=Title_mid).place(x = XX1+25,y = yy+Y1-10)  
            Label(self.tab1, text = "Current Pos",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = yy+Y1 + dY1)  
            self.v3_cur_pos = Label(self.tab1, text = "----",
                                    font=Font1 ).place(x =XX1 + XX2,y = yy+Y1 + dY1)  
            Label(self.tab1, text = "New Pos",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = yy+Y1 + 2*dY1)  
            self.combo3 = ttk.Combobox(self.tab1,  width=3, font=Font6)
            self.combo3['values'] = (1,2,3,4,5,"Text")
            self.combo3.current(3)
            self.combo3.place(x = XX1 + XX2,y =yy+ Y1 + 2*dY1)
            self.combo3.bind("<<ComboboxSelected>>", self.checkCombo3) 
            
            yy = 125*2
            Label(self.tab1, text = "5: PIPETTE VALVE",font=Font5 , bg=Color1,
                  fg=Title_mid).place(x = XX1+10,y = yy+Y1-10)  
            Label(self.tab1, text = "Current Pos",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = yy+Y1 + dY1)  
            self.v5_cur_pos = Label(self.tab1, text = "----",
                                    font=Font1 ).place(x =XX1 + XX2, y = yy+Y1 + dY1)  
            Label(self.tab1, text = "New Pos",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = yy+Y1 + 2*dY1)  
            self.combo5 = ttk.Combobox(self.tab1,  width=3, font=Font6)
            self.combo5['values'] = (1,2,3,4,5,"Text")
            self.combo5.current(3)
            self.combo5.place(x = XX1 + XX2,y =yy+ Y1 + 2*dY1)
            self.combo5.bind("<<ComboboxSelected>>", self.checkCombo5) 
            
            yy = 125*3
            Label(self.tab1, text = "7: CLEANING VALVE",font=Font5 , bg=Color1,
                  fg=Title_mid).place(x = XX1+0,y = yy+Y1-10)  
            Label(self.tab1, text = "Current Pos",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = yy+Y1 + dY1)  
            self.v5_cur_pos = Label(self.tab1, text = "----",
                                    font=Font1 ).place(x =XX1 + XX2,y = yy+Y1 + dY1)  
            Label(self.tab1, text = "New Pos",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = yy+Y1 + 2*dY1)  
            self.combo9 = ttk.Combobox(self.tab1,  width=3, font=Font6)
            self.combo9['values'] = (1,2,3,4,5,"Text")
            self.combo9.current(3)
            self.combo9.place(x = XX1 + XX2,y =yy+ Y1 + 2*dY1)
            self.combo9.bind("<<ComboboxSelected>>", self.checkCombo9) 
            
            #--------------------- COLUMN 4:   VALVES 2, 4, 6, 7, 8 --------------------
            dx_t2 = 770   
            Label(self.tab1, text = "SAMPLE LINE",font=Font4 , bg=Color1,
                  fg=Title_large).place(x =dx_t2 +20,y = Y1-80)  
            Label(self.tab1, text = "2: PUMP VALVE",font=Font5 , bg=Color1,
                  fg=Title_mid).place(x = dx_t2 +20,y = Y1-10)  
            Label(self.tab1, text = "Current Pos",font=Font1 , bg=Color1,
                  fg='black').place(x = dx_t2,y = Y1 + dY1)  
            self.v2_cur_pos = Label(self.tab1, text = "----",
                                    font=Font1 ).place(x =XX2 + dx_t2,y = Y1 + dY1)  
            Label(self.tab1, text = "New Pos",font=Font1, bg=Color1,
                  fg='black' ).place(x = dx_t2,y = Y1 + 2*dY1)  
            self.combo2 = ttk.Combobox(self.tab1,  width=2, font=Font6)
            self.combo2['values'] = (1,2,3,4,5,"Text")
            self.combo2.current(3)
            self.combo2.place(x = XX2 + dx_t2,y = Y1 + 2*dY1)
            self.combo2.bind("<<ComboboxSelected>>", self.checkCombo2) 
            
            yy = 125
            Label(self.tab1, text = "4: LOOP VALVE",font=Font5 , bg=Color1,
                  fg=Title_mid).place(x = dx_t2 +20,y=yy+Y1-10)  
            Label(self.tab1, text = "Current Pos",font=Font1 , bg=Color1,
                  fg='black').place(x = dx_t2,y = yy+Y1 + dY1)  
            self.v4_cur_pos = Label(self.tab1, text = "----",
                                    font=Font1 ).place(x =XX2 + dx_t2,y = yy+Y1 + dY1)  
            Label(self.tab1, text = "New Pos",font=Font1, bg=Color1,
                  fg='black' ).place(x = dx_t2,y = yy+Y1 + 2*dY1)  
            self.combo4 = ttk.Combobox(self.tab1,  width=2, font=Font6)
            self.combo4['values'] = (1,2,3,4,5,"Text")
            self.combo4.current(3)
            self.combo4.place(x = XX2 + dx_t2,y = yy+Y1 + 2*dY1)
            self.combo4.bind("<<ComboboxSelected>>", self.checkCombo4) 
            
            yy = 125*2
            Label(self.tab1, text = "6: TITRANT PORT VALVE",font=Font5 , bg=Color1,
                  fg=Title_mid).place(x = dx_t2 -18,y=yy+Y1-10)  
            Label(self.tab1, text = "Current Pos",font=Font1 , bg=Color1,
                  fg='black').place(x = dx_t2,y = yy+Y1 + dY1)  
            self.v6_cur_pos = Label(self.tab1, text = "----",
                                    font=Font1 ).place(x =XX2 + dx_t2,y = yy+Y1 + dY1)  
            Label(self.tab1, text = "New Pos",font=Font1, bg=Color1,
                  fg='black' ).place(x = dx_t2,y = yy+Y1 + 2*dY1)  
            self.combo6 = ttk.Combobox(self.tab1,  width=2, font=Font6)
            self.combo6['values'] = (1,2,3,4,5,"Text")
            self.combo6.current(3)
            self.combo6.place(x = XX2 + dx_t2,y = yy+Y1 + 2*dY1)
            self.combo6.bind("<<ComboboxSelected>>", self.checkCombo6) 
            
            yy = 125*3
            Label(self.tab1, text = "8: DEGASSER VALVE",font=Font5 , bg=Color1,
                  fg=Title_mid).place(x = dx_t2 -1,y=yy+Y1-10)  
            Label(self.tab1, text = "Current Pos",font=Font1 , bg=Color1,
                  fg='black').place(x = dx_t2,y = yy+Y1 + dY1)  
            self.v7_cur_pos = Label(self.tab1, text = "----",
                                    font=Font1 ).place(x =XX2 + dx_t2,y = yy+Y1 + dY1)  
            Label(self.tab1, text = "New Pos",font=Font1 , bg=Color1,
                  fg='black').place(x = dx_t2,y = yy+Y1 + 2*dY1)  
            self.combo7 = ttk.Combobox(self.tab1,  width=2, font=Font6)
            self.combo7['values'] = (1,2,3,4,5,"Text")
            self.combo7.current(3)
            self.combo7.place(x = XX2 + dx_t2,y =yy+ Y1 + 2*dY1)
            self.combo7.bind("<<ComboboxSelected>>", self.checkCombo7) 
            
            yy = 125*4
            Label(self.tab1, text = "9: CLEANING VALVE",font=Font5 , bg=Color1,
                  fg=Title_mid).place(x = dx_t2 +0,y=yy+Y1-10)  
            Label(self.tab1, text = "Current Pos",font=Font1 , bg=Color1,
                  fg='black').place(x = dx_t2,y = yy+Y1 + dY1)  
            self.v8_cur_pos = Label(self.tab1, text = "----",
                                    font=Font1 ).place(x =XX2 + dx_t2,y = yy+Y1 + dY1)  
            Label(self.tab1, text = "New Pos",font=Font1 , bg=Color1,
                  fg='black').place(x = dx_t2,y = yy+Y1 + 2*dY1)  
            self.combo8 = ttk.Combobox(self.tab1,  width=2, font=Font6)
            self.combo8['values'] = (1,2,3,4,5,"Text")
            self.combo8.current(3)
            self.combo8.place(x = XX2 + dx_t2,y =yy+ Y1 + 2*dY1)
            self.combo8.bind("<<ComboboxSelected>>", self.checkCombo8) 


      # #--------------------- COLUMN 4: BUBBLE SENSORS ---------------------------------------
            X3 = 1050
            Y1 = 100
            dY1 = 40

            image1 = Image.open('./Images/led-green-off.png')
            image1 = image1.resize((24, 24))
            icon_off = ImageTk.PhotoImage(image1)
            image1 = Image.open('./Images/led-green-on.png')
            image1 = image1.resize((24, 24))
            icon_on = ImageTk.PhotoImage(image1)
            image1 = Image.open('./Images/arrow_red.png')
            image1 = image1.resize((24, 16))
            icon_arrow = ImageTk.PhotoImage(image1)

            Label(self.tab1, text = "BUB. SENS.",font=Font4 , bg=Color1,
                  fg='black') 
            Label(self.tab1, text = "BS1",font=Font1 , bg=Color1,
                  fg='black').place(x = X3,y = Y1 + 0*dY1)  
            Label(self.tab1, text = "BS2",font=Font1 , bg=Color1,
                  fg='black').place(x = X3,y = Y1 + 1*dY1)  
            Label(self.tab1, text = "BS3",font=Font1 , bg=Color1,
                  fg='black').place(x = X3,y = Y1 + 2*dY1)  
            Label(self.tab1, text = "BS4",font=Font1 , bg=Color1,
                  fg='black').place(x = X3,y = Y1 + 3*dY1)
            Label(self.tab1, text = "BS5",font=Font1 , bg=Color1,
                  fg='black').place(x = X3,y = Y1 + 4*dY1)
            Label(self.tab1, text = "BS6",font=Font1 , bg=Color1,
                  fg='black').place(x = X3,y = Y1 + 5*dY1)
            Label(self.tab1, text = "BS7",font=Font1 , bg=Color1,
                  fg='black').place(x = X3,y = Y1 + 6*dY1)
            Label(self.tab1, text = "BS8",font=Font1 , bg=Color1,
                  fg='black').place(x = X3,y = Y1 + 7*dY1)
            Label(self.tab1, text = "BS9",font=Font1 , bg=Color1,
                  fg='black').place(x = X3,y = Y1 + 8*dY1)
            Label(self.tab1, text = "BS10",font=Font1 , bg=Color1,
                  fg='black').place(x = X3,y = Y1 + 9*dY1)
            Label(self.tab1, text = "BS11",font=Font1 , bg=Color1,
                  fg='black').place(x = X3,y = Y1 + 10*dY1)
            Label(self.tab1, text = "BS12",font=Font1 , bg=Color1,
                  fg='black').place(x = X3,y = Y1 + 11*dY1)
            Label(self.tab1, text = "BS13",font=Font1 , bg=Color1,
                  fg='black').place(x = X3,y = Y1 + 12*dY1)
            Label(self.tab1, text = "BS14",font=Font1 , bg=Color1,
                  fg='black').place(x = X3,y = Y1 + 13*dY1)
            self.led_off_1 = Label(self.tab1, image=icon_off)
            self.led_off_1.image = icon_off
            self.led_off_1.place(x = X3+50,y = Y1 + 0*dY1)
            self.led_off_2 = Label(self.tab1, image=icon_off)
            self.led_off_2.image = icon_off
            self.led_off_2.place(x = X3+50,y = Y1 + 1*dY1)
            self.led_off_3 = Label(self.tab1, image=icon_off)
            self.led_off_3.image = icon_off
            self.led_off_3.place(x = X3+50,y = Y1 + 2*dY1)
            self.led_off_4 = Label(self.tab1, image=icon_off)
            self.led_off_4.image = icon_off
            self.led_off_4.place(x = X3+50,y = Y1 + 3*dY1)
            self.led_off_5 = Label(self.tab1, image=icon_off)
            self.led_off_5.image = icon_off
            self.led_off_5.place(x = X3+50,y = Y1 + 4*dY1)
            self.led_off_6 = Label(self.tab1, image=icon_off)
            self.led_off_6.image = icon_off
            self.led_off_6.place(x = X3+50,y = Y1 + 5*dY1)
            self.led_off_7 = Label(self.tab1, image=icon_off)
            self.led_off_7.image = icon_off
            self.led_off_7.place(x = X3+50,y = Y1 + 6*dY1)
            self.led_off_8 = Label(self.tab1, image=icon_off)
            self.led_off_8.image = icon_off
            self.led_off_8.place(x = X3+50,y = Y1 + 7*dY1)
            self.led_off_9 = Label(self.tab1, image=icon_off)
            self.led_off_9.image = icon_off
            self.led_off_9.place(x = X3+50,y = Y1 + 8*dY1)
            self.led_off_10 = Label(self.tab1, image=icon_off)
            self.led_off_10.image = icon_off
            self.led_off_10.place(x = X3+50,y = Y1 + 9*dY1)
            self.led_off_11 = Label(self.tab1, image=icon_off)
            self.led_off_11.image = icon_off
            self.led_off_11.place(x = X3+50,y = Y1 + 10*dY1)
            self.led_off_12 = Label(self.tab1, image=icon_off)
            self.led_off_12.image = icon_off
            self.led_off_12.place(x = X3+50,y = Y1 + 11*dY1)
            self.led_off_13 = Label(self.tab1, image=icon_off)
            self.led_off_13.image = icon_off
            self.led_off_13.place(x = X3+50,y = Y1 + 12*dY1)
            self.led_off_14 = Label(self.tab1, image=icon_off)
            self.led_off_14.image = icon_off
            self.led_off_14.place(x = X3+50,y = Y1 + 13*dY1)

            dd=50
            self.led_on_1  = Label(self.tab1, image=icon_on)
            self.led_on_1 .image = icon_on
            self.led_on_1 .place(x =X3+50+dd,y = Y1 + 0*dY1)
            self.led_on_2  = Label(self.tab1, image=icon_on)
            self.led_on_2.image = icon_on
            self.led_on_2.place(x = X3+50+dd,y = Y1 + 1*dY1)
            self.led_on_3  = Label(self.tab1, image=icon_on)
            self.led_on_3.image = icon_on
            self.led_on_3.place(x = X3+50+dd,y = Y1 + 2*dY1)        
            self.led_on_4  = Label(self.tab1, image=icon_on)
            self.led_on_4.image = icon_on
            self.led_on_4.place(x = X3+50+dd,y = Y1 + 3*dY1)        
            self.led_on_5  = Label(self.tab1, image=icon_on)
            self.led_on_5.image = icon_on
            self.led_on_5.place(x = X3+50+dd,y = Y1 + 4*dY1)
            self.led_on_6  = Label(self.tab1, image=icon_on)
            self.led_on_6.image = icon_on
            self.led_on_6.place(x = X3+50+dd,y = Y1 + 5*dY1)
            self.led_on_7  = Label(self.tab1, image=icon_on)
            self.led_on_7.image = icon_on
            self.led_on_7.place(x = X3+50+dd,y = Y1 + 6*dY1)
            self.led_on_8  = Label(self.tab1, image=icon_on)
            self.led_on_8.image = icon_on
            self.led_on_8.place(x = X3+50+dd,y = Y1 + 7*dY1)
            self.led_on_9  = Label(self.tab1, image=icon_on)
            self.led_on_9.image = icon_on
            self.led_on_9.place(x = X3+50+dd,y = Y1 + 8*dY1)        
            self.led_on_10  = Label(self.tab1, image=icon_on)
            self.led_on_10.image = icon_on
            self.led_on_10.place(x = X3+50+dd,y = Y1 + 9*dY1)        
            self.led_on_11  = Label(self.tab1, image=icon_on)
            self.led_on_11.image = icon_on
            self.led_on_11.place(x = X3+50+dd,y = Y1 + 10*dY1)
            self.led_on_12  = Label(self.tab1, image=icon_on)
            self.led_on_12.image = icon_on
            self.led_on_12.place(x = X3+50+dd,y = Y1 + 11*dY1)
            self.led_on_13  = Label(self.tab1, image=icon_on)
            self.led_on_13.image = icon_on
            self.led_on_13.place(x = X3+50+dd,y = Y1 + 12*dY1)
            self.led_on_14  = Label(self.tab1, image=icon_on)
            self.led_on_14.image = icon_on
            self.led_on_14.place(x = X3+50+dd,y = Y1 + 13*dY1)


            self.lbs1 = Label(self.tab1, text = "==>",font=Font3 , 
                              bg=Color1,fg='red')
            self.lbs1.pack()
            self.lbs1.place(x = X3-40,y = Y1 + 0*dY1) 
            self.lbs2 = Label(self.tab1, text = "==>",font=Font3 , 
                              bg=Color1,fg='red')
            self.lbs2.pack()
            self.lbs2.place(x = X3-40,y = Y1 + 1*dY1)  
            self.lbs3 = Label(self.tab1, text = "==>",font=Font3 , 
                              bg=Color1,fg='red')
            self.lbs3.pack()
            self.lbs3.place(x = X3-40,y = Y1 + 2*dY1)  
            self.lbs4 = Label(self.tab1, text = "==>",font=Font3 , 
                              bg=Color1,fg='red')
            self.lbs4.pack()
            self.lbs4.place(x = X3-40,y = Y1 + 3*dY1)
            self.lbs5 = Label(self.tab1, text = "==>",font=Font3 , 
                              bg=Color1,fg='red')
            self.lbs5.pack()
            self.lbs5
            self.lbs6 = Label(self.tab1, text = "==>",font=Font3 , 
                              bg=Color1,fg='red')
            self.lbs6.pack()
            self.lbs6.place(x = X3-40,y = Y1 + 4*dY1)
            self.lbs7 = Label(self.tab1, text = "==>",font=Font3 , 
                              bg=Color1,fg='red')
            self.lbs7.pack()
            self.lbs7.place(x = X3-40,y = Y1 + 6*dY1)
            self.lbs8 = Label(self.tab1, text = "==>",font=Font3 , 
                              bg=Color1,fg='red')
            self.lbs8.pack()
            self.lbs8.place(x = X3-40,y = Y1 + 7*dY1)
            self.lbs9 = Label(self.tab1, text = "==>",font=Font3 , 
                              bg=Color1,fg='red')
            self.lbs9.pack()
            self.lbs9.place(x = X3-40,y = Y1 + 8*dY1)
            self.lbs10 = Label(self.tab1, text = "==>",font=Font3 , 
                              bg=Color1,fg='red')
            self.lbs10.pack()
            self.lbs10.place(x = X3-40,y = Y1 + 9*dY1)
            self.lbs11 = Label(self.tab1, text = "==>",font=Font3 , 
                              bg=Color1,fg='red')
            self.lbs11.pack()
            self.lbs11.place(x = X3-40,y = Y1 + 10*dY1)
            self.lbs12 = Label(self.tab1, text = "==>",font=Font3 ,
                              bg=Color1,fg='red')
            self.lbs12.pack()
            self.lbs12.place(x = X3-40,y = Y1 + 11*dY1)
            self.lbs13 = Label(self.tab1, text = "==>",font=Font3 , 
                              bg=Color1,fg='red')
            self.lbs13.pack()
            self.lbs13.place(x = X3-40,y = Y1 + 12*dY1)
            self.lbs14 = Label(self.tab1, text = "==>",font=Font3 , 
                              bg=Color1,fg='red')
            self.lbs14.pack()
            self.lbs14.place(x = X3-40,y = Y1 + 13*dY1)


            self.lbs2.place_forget()
            self.lbs3.place_forget()
            self.lbs4.place_forget()
            self.lbs5.place_forget()
            self.lbs6.place_forget()
            self.lbs7.place_forget()
            self.lbs8.place_forget()
            self.lbs9.place_forget()
            self.lbs10.place_forget()
            self.lbs11.place_forget()
            self.lbs12.place_forget()
            self.lbs13.place_forget()
            self.lbs14.place_forget()
            # dd=50
            # self.led_arrow_1  = Label(self.tab1, image=icon_arrow)
            # self.led_arrow_1.image = icon_arrow
            # self.led_arrow_1.place(x = X3-20,y = Y1 + 0*dY1)
            
            # led_on_14.place_forget()
            # #---------------------  MOTORS TAB ---------------------------------------
            # # Create a canvas widget
            self.canvas2=Canvas(self.tab2, width=1200, height=800,bg=Color1)
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
            Label(self.tab2, text = "MOTOR 1 ",font=Font4 , bg=Color1,
                  fg=Title_large).place(x = XX1+40,y = 40)  
            Label(self.tab2, text = "Current Spd",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = Y1 + dY1)  
            self.m1_cur_spd = Label(self.tab2, text = "----",font=Font1 )
            self.m1_cur_spd.pack()
            self.m1_cur_spd.place(x =XX1 + XX2,y = Y1 + dY1)  
            Label(self.tab2, text = "New Spd",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = Y1 + 2*dY1)  
            self.ent_m1_spd_ = Entry(self.tab2, width=8)
            self.ent_m1_spd_.pack()
            self.ent_m1_spd_.place(x = XX1 + XX2,y = Y1 + 2*dY1 ) 
            self.b_m1_spd = Button(self.tab2,text="set", bg=Color2, 
                                    fg=Color3, 
                                    command=self.m1_b_abs_pos_click).place(x = XX1 + XX2+XX3,
                                                                        y = Y1 + 2*dY1 - 2)
            #--------------------- COLUMN 2: Gantry Horizontal ---------------------------------------
            XX1 = 350
            Label(self.tab2, text = "GANTRY HORIZ.",font=Font4 , bg=Color1,
                  fg=Title_large).place(x = XX1-10,y = 40)  
            Label(self.tab2, text = "Current Spd",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = Y1 + dY1)  
            self.m2_cur_spd = Label(self.tab2, text = "----",
                                    font=Font1 ).place(x =XX1 + XX2,y = Y1 + dY1)  
            Label(self.tab2, text = "New Spd",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = Y1 + 2*dY1)  
            self.combo_mh = ttk.Combobox(self.tab2,  width=2, font=Font6)
            self.combo_mh['values'] = (1,2,3,4,5,"Text")
            self.combo_mh.current(3)
            self.combo_mh.place(x = XX1 + XX2,y = Y1 + 2*dY1)
            Button(self.tab2, bg=Color2, fg=Color3,text="set", 
                  command=self.checkCombo_mh).place(x = XX1 + XX2+50,y = Y1 + 2*dY1 - 2)
            #--------------------- COLUMN 3: Gantry vertical ---------------------------------------
            XX1 = 650
            Label(self.tab2, text = "GANTRY VER.",font=Font4 , bg=Color1,
                  fg=Title_large).place(x = XX1-0,y = 40)  
            Label(self.tab2, text = "Current Spd",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = Y1 + dY1)  
            self.m3_cur_spd = Label(self.tab2, text = "----",
                                    font=Font1 ).place(x =XX1 + XX2,y = Y1 + dY1)  
            Label(self.tab2, text = "New Spd",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = Y1 + 2*dY1)  
            self.combo_mv = ttk.Combobox(self.tab2,  width=2, font=Font6)
            self.combo_mv['values'] = (1,2,3,4,5,"Text")
            self.combo_mv.current(3)
            self.combo_mv.place(x = XX1 + XX2,y = Y1 + 2*dY1)
            Button(self.tab2, bg=Color2, fg=Color3,text="set", 
                  command=self.checkCombo_mv).place(x = XX1 + XX2+50,y = Y1 + 2*dY1 - 2)

            #--------------------- COLUMN 4: TEC controller ---------------------------------------
            XX1 = 950
            Label(self.tab2, text = "TEMP. CONTROLLER",font=Font4 , bg=Color1,
                  fg=Title_large).place(x = XX1-40,y = 40)  
            Label(self.tab2, text = "Current Tmp.",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = Y1 + dY1)  
            self.tec_cur_tmp = Label(self.tab2, text = "----",font=Font1 )
            self.tec_cur_tmp.pack()
            self.tec_cur_tmp.place(x =XX1 + XX2,y = Y1 + dY1)          
            Label(self.tab2, text = "Target temp",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = Y1 + 2*dY1)  
            self.tec_desired_tmp = Label(self.tab2, text = '-----',font=Font1 )
            self.tec_desired_tmp.pack()
            self.tec_desired_tmp.place(x =XX1 + XX2 ,y = Y1 +2* dY1)  
            Label(self.tab2, text = "New Tmp.",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = Y1 + 3*dY1)  
            self.ent_tmp = Entry(self.tab2, width=5,font=Font1) 
            self.ent_tmp.pack()
            self.ent_tmp.place(x = XX1 + XX2,y = Y1 + 3* dY1 )
            Button(self.tab2,text="set", bg=Color2, fg=Color3, 
                  command=self.tec_b_tmpset_click).place(x = XX1 + XX2+XX3+10,
                                                            y = Y1 + 3*dY1 - 2)        
            self.t_status = Label(self.tab2, text = '-----',font=Font1 )
            self.t_status.pack()
            self.t_status.place(x =XX1 + XX2 ,y = Y1 +4* dY1)  
            Label(self.tab2, text = "Cur. Status",font=Font1 , bg=Color1,
                  fg='black').place(x = XX1,y = Y1 + 4*dY1)  

            Button(self.tab2,text="   START  ", bg=Color2, fg=Color3,font=Font7, 
                  command=self.tec_b_start_click).place(x = XX1-10  ,y = Y1 + 5*dY1 - 2)
            Button(self.tab2,text="   STOP   ", bg=Color2, fg=Color3,font=Font7, 
                  command=self.tec_b_stop_click).place(x = XX1 + XX2+10,y = Y1 + 5*dY1 - 2)
            
            #---------------------------- EXIT BUTTON ----------------------------------------

            self.b_exit = Button(self.tab1,text="Exit\n Application", bg="#fc9d9d", fg='black',font=Font4,
                              height=4, width=14, 
                              command=self.checkExitButton).place(x =260,y = 590)
        
  

            #---------------------------- TAB #: CONFIG ----------------------------------------

            # Font1 = 'sans 13' # fixed label text font
            # Font2 = 'sans 11 italic' #variable label text font
            # Font3 = 'sans 15'  # titles label text font 
            # Font4 = 'sans 20'  # large title labels text font
            # Font5 = 'Arial 16'  #valves title label text font
            # Font6 = "Verdana 10 " # combo box text font
            # Font7 = "Arial 14" # larger text for terminate/start/stop buttons

            dY1 = 40
            XX1 = 80 # first col. of labels
            Y1 = 120
            XX2 = 240 # second col of labels

            Label(self.tab3, text = "PORT ASSINGMENT",font=Font4 , bg=Color1,
                  fg=Title_large).place(x = XX1,y=Y1-80)  
            Label(self.tab3, text = "TEC Controller Port:",font=Font3 , bg=Color1,
                  fg='black').place(x = XX1,y = Y1)  
            self.Ltecport= Label (self.tab3, text = "----",font='sans 15 italic' , bg=Color1,
                                  fg='green')
            self.Ltecport.pack()
            self.Ltecport.place(x = XX1+XX2,y = Y1)

            Label(self.tab3, text = "PUMP1 Port:",font=Font3 , bg=Color1,
                  fg='black').place(x = XX1,y = Y1+2*dY1)  
            self.Lpump1port = Label(self.tab3, text = "----",font='sans 15 italic' , bg=Color1,
                                    fg='green')
            self.Lpump1port.pack()
            self.Lpump1port.place(x = XX1+XX2,y = Y1+2*dY1)
            
            Label(self.tab3, text = "MOTOR1 Port:",font=Font3 , bg=Color1,
                  fg='black').place(x = XX1,y = Y1+4*dY1)  
            self.Lmotor1port = Label(self.tab3, text = "----",font='sans 15 italic' , bg=Color1,
                                    fg='green')
            self.Lmotor1port.pack()
            self.Lmotor1port.place(x = XX1+XX2,y = Y1+4*dY1)

            # Clock.schedule_interval(self.timerCallback_1, .5)
            # self.timer = threading.Timer(1.0, self.timerCallback_1)
            # self.timer.start()


      #-------------------------------------------------------------------------
      #--------------------- DEFINE CALLBACK FUNCTIONS FOR PUMPS BUTTONS -------

      # def timerCallback_1(self):  
      #     print('parent: timer tick')
      #     self.timer = threading.Timer(1.0, self.timerCallback_1)
      #     self.timer.start()


      def checkExitButton(self):
            print("exit button pressed ...")
            self.timer.cancel()
            # self.root.destroy()
            sys.exit(0)


      def checkComboCfg1(self, event):
            # def option_selected(event):
            s = self.comboCfg1.get()
            print('parent :', s)
            ss=s.partition(')')
            # index = self.comboCfg1.get(0, "end") 
            index = ss[0]
            return index
            # print("INDEX = ", index)

      def checkComboCfg2(self, event):
            # def option_selected(event):
            print(self.comboCfg1.get())


      # def p1_b_Zinit_click(self):
      #      print("p1 Z initialized")

      # def p1_b_Yinit_click(self):
      #      print("p1 Y initialized")

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
            print("parent: p1_pickup ")
            s =   self.ent_pickup_pos.get()
            print(s)

      def p1_b_dispense_pos_click(self):
            print("parent: p1_dispense ")
            s =   self.ent_dispemse_pos.get()
            print(s)


      def p1_b_pickupUntillbubble(self):
            print("paretn: pickup until bubble")

      def p1_b_dispenseUntillbubble(self):
            print("paretn: dispense until bubble")

      def p1_b_teminateP1(self):
            print('parent: termnate p1')
            
      def p1_b_teminateP2(self):
            print('parent: termnate p2')

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

      def tec_b_tmpset_click(self):
            print("parent: TECt new tmp:")
            s =   self.ent_tmp.get()
            print(s)

      def tec_b_start_click(self):
            print("parent: TEC start")
            pass

      def tec_b_stop_click(self):
            print("parent: TEC stop")
            pass


      #--------------------- DEFINE CALLBACK FUNCTIONS FOR VALVES BUTTONS -----------------
      
      def checkCombo0(self,event):        
            print("parent:", self.combo0.get())
      
      def checkCombob1(self, event):
            print("parent:", self.combob1.get())


      def checkComboP1(self,event):
            print('pump1 mode selected')
            print(self.comboP1.get())


      def checkCombo1(self,event):
            print('-->'+self.combo1.get())

      def checkCombo3(self, event):
            print('-->'+self.combo3.get())

      def checkCombo5(self, event):
            print('-->'+self.combo5.get())

      def checkCombo9(self, event):
            print('-->'+self.combo9.get())        

      def checkCombo2(self, event):
            print('-->'+self.combo2.get())  

      def checkCombo4(self,event):
            print('-->'+self.combo4.get()) 

      def checkCombo6(self,event):
            print('-->'+self.combo6.get()) 

      def checkCombo7(self,event):
            print('-->'+self.combo7.get()) 

      def checkCombo8(self,event):
            print('-->'+self.combo8.get()) 
      #--------------------- DEFINE CALLBACK FUNCTIONS FOR BUTTONS -----------------
      def m1_b_abs_pos_click(self):
            print("parent: m1_new_spd")
            s =   self.ent_m1_spd_.get()
            print(s)
            # if (is_float(s) == True):
            #     print('it\'s a number:', float(s))
            # else:
            #     print("nut a number")

      def checkCombo_mh(self):
            print('-->'+self.combo_mh.get())

      def checkCombo_mv(self):
            print('-->'+self.combo_mv.get())


      # def p1_ustep(self):
      #     print('------------', self.chk_state)
      #     if (self.chk_state.get() == 0 ):
      #         print("unckecked ...")            
      #     else:
      #         print("ckecked...")
        
        



# def main(): #run mianloop 
#     root = Tk()
#     app = GUI(root)
#     root.mainloop()

if __name__ == '__main__':
    # main()
    root = Tk()
    app = GUI(root)
    root.mainloop()
