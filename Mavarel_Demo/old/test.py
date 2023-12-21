import motor_1
import time
import Pump as P
if __name__ == "__main__":
    # sample application
    # m1 = motor_1.motor_1(0,.5)    
    # m1.set_speed(100)
    # time.sleep(2)
    # m1.set_speed(0.5)
    # time.sleep(2)
    # m1.stop()
    
    p1 = P.Pump()
    p1.set_speed(1000)
    time.sleep(2)
    p1.set_pos_absolute(1000)
    time.sleep(2)
    p1.set_pos_relative(1000)
    p1.close()