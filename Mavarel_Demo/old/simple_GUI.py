#!/usr/bin/env python


import math
import time

import kivy
from kivy.config import Config
Config.set('graphics', 'resizable', False)
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
#import kivy.properties as kyprops
import motor_1 as M1



Window.size = (1200, 800)
# Window.top = 100
# Window.left = 100

colors = {
    "Teal": {
        "50": "e4f8f9",
        "100": "bdedf0",
        "200": "97e2e8",
        "300": "79d5de",
        "400": "6dcbd6",
        "500": "6ac2cf",
        "600": "63b2bc",
        "700": "5b9ca3",
        "800": "54888c",
        "900": "486363",
        "A100": "bdedf0",
        "A200": "97e2e8",
        "A400": "6dcbd6",
        "A700": "5b9ca3",
    },
    "Blue": {
        "50": "e3f3f8",
        "100": "b9e1ee",
        "200": "91cee3",
        "300": "72bad6",
        "400": "62acce",
        "500": "589fc6",
        "600": "5191b8",
        "700": "487fa5",
        "800": "426f91",
        "900": "35506d",
        "A100": "b9e1ee",
        "A200": "91cee3",
        "A400": "62acce",
        "A700": "487fa5",
    },
    "Red": {
        "50": "FFEBEE",
        "100": "FFCDD2",
        "200": "EF9A9A",
        "300": "E57373",
        "400": "EF5350",
        "500": "F44336",
        "600": "E53935",
        "700": "D32F2F",
        "800": "C62828",
        "900": "B71C1C",
        "A100": "FF8A80",
        "A200": "FF5252",
        "A400": "FF1744",
        "A700": "D50000",
    },
    "Light": {
        "StatusBar": "E0E0E0",
        "AppBar": "F5F5F5",
        "Background": "FAFAFA",
        "CardsDialogs": "FFFFFF",
        "FlatButtonDown": "cccccc",
    },
    "Dark": {
        "StatusBar": "000000",
        "AppBar": "212121",
        "Background": "303030",
        "CardsDialogs": "424242",
        "FlatButtonDown": "999999",
    }
}

class TutorialApp(MDApp):
    dx1 = -.05#0.03
    dx2 = - 0.012
    dx3 = 0.025
    dx4 = 0.045
    col1_left = .12
    col2_left = .3
    col3_left = .48
    col4_left = .68
    col5_left = .88
    edit_box_size = .055
    row1=0.96
    row2=0.92
    row3=0.88
    row4=0.82 -.03
    row5=0.78 -.03
    row6=0.74 -.03
    row7=0.68 -.06
    row8=0.64 -.06
    row9=0.60 -.06    
    row10=0.54 -.09
    row11=0.50 -.09
    row12=0.46 -.09
    row13=0.40 -.12
    row14=0.36 -.12
    row15=0.32 -.12   
    row16=0.26 -.14
    row17=0.22 -.14
    row18=0.18 -.14
    off1 = .065
    bs_row1=.9
    bs_row2= 0.9 - off1
    bs_row3=0.9 - 2 * off1
    bs_row4=0.9 - 3 * off1
    bs_row5=0.9 - 4 * off1
    bs_row6=0.9 - 5 * off1
    bs_row7=0.9 - 6 * off1
    bs_row8=0.9 - 7 *  off1
    bs_row9=0.9 - 8 * off1
    bs_row10=0.9 - 9 * off1
    bs_row11=0.9 - 10 * off1
    bs_row12=0.9 - 11 * off1
    bs_row13=0.9 - 12 * off1
    bs_row14=0.9 - 13 * off1



    control_left = .75
    control_top = .55
    joging_left = .2
    joging_top = .55#self.gui_packet
    uid_left = .83
    uid_top = .95
    arm_left = .31
    arm_top = .9
    message_top = .04
    message_left = .12
    state_top = .05
    state_left = .7
    mode_top = .02
    mode_left = .7
    motor_data_left = 10
    pump1_cur = 0
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file('Images/ui_01.kv')
        # self.screen.ids.pump1_cur.text ="%.1f"%(123.45)
        self.screen.ids.pump1_new.text = "0"
        self.screen.ids.motor1_cur.text = "0"
        self.screen.ids.motor1_new.text = "0"
        # self.motor1 = M1.motor_1(0,.5)
        Clock.schedule_interval(self.timerCallback_1, .5)

    def build(self):
        self.title = 'GUI - Master'
        self.initil_center = Window.center

        #self.theme_cls.primary_palette =  "Green" #"Purple"#"Red"
        self.theme_cls.theme_style = "Light" #"Dark"
        return self.screen


    def timerCallback_1(self,dt):     

        self.screen.ids.pump1_cur.text ="%.1f"%(self.pump1_cur)
        self.pump1_cur += .1
        out = self.screen.ids.pump1_new.text
        # if is_float(out):
        #     # print("{} is equal to {}".format(out, float(out)))
        #     print("{} is equal to {} --> integer conversion:{}".format(out, out,int(float(out))))
        
    ##--------------- END OF CONTROL ------------------------


    def motor1_set(self, *args):
        print('--------------- motor 1 is pressed -------------------')
        m1_speed = self.screen.ids.motor1_new.text
        if is_float(m1_speed):
            motor1_speed = float(m1_speed)
            print("motor 1 speed: ", motor1_speed)
            valid = self.motor1.set_speed(motor1_speed)
            if (valid == True):
                self.screen.ids.motor1_cur.text = m1_speed



def is_float(element: any) -> bool:
    #If you expect None to be passed:
    if element is None: 
        return False
    try:
        float(element)
        return True
    except ValueError:
        return False



if __name__ == '__main__':
    try:

        
        time.sleep(2)
        TutorialApp().run()

    except:
        print('exception happened')


