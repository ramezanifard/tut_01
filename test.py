import motor_1
import time
import Pump as P

if __name__ == "__main__":
    # sample application
    # sample application
    # m1 = motor_1.motor_1(0,.5)    
    # m1.set_speed(100)
    # time.sleep(2)
    # m1.set_speed(0.5)
    # time.sleep(2)
    # m1.stop()
    
    
    p1 = P.Pump()
    # p1.pump_init(1)

    
    
    p1.set_speed(1,6000)
    time.sleep(2)
    p1.set_pos_absolute(1, 1000)
    time.sleep(2)
    a = p1.get_plunger_position(1)    
    # print('plunger pos:', a)
    time.sleep(2)
    p1.set_pos_absolute(1, 500)
    time.sleep(2)
    a = p1.get_plunger_position(1)    
    # print('plunger pos:', a)
    # p1.set_pickup(1, 5000)
    # p1.set_dispense(1, 5000)

    # testing valve
    # p1.set_valve(1,'I')
    # time.sleep(1)
    # ss = p1.get_valve(1)
    # print('valve pos:', ss)
    # time.sleep(1)
    # p1.set_valve(1,'O')
    # time.sleep(1)
    # ss = p1.get_valve(1)
    # print('valve pos:', ss)

    