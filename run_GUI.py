import GUI
from tkinter import * 


class ex(GUI.GUI):
    def __init__(self,root):
        super().__init__( root)

        
    def timerCallback_1(self):  
        print('--->timer tick')
        self.timer = GUI.threading.Timer(1.0, self.timerCallback_1)
        self.timer.start()


    def p1_b_abs_pos_click(self):
        print("----> p1_abs pos")
        s =   self.ent_abs_pos.get()
        print(s)
        self.p1_cur_pos["text"]=  s



def main(): #run mianloop 
    root = Tk()
    # app = GUI.GUI(root)
    ex(root)

    root.mainloop()

if __name__ == '__main__':
    main()