import u6
import time
TIMEOUT = 7 #time out for detecting bubble
THRESHOLD = 2 #Threshold for bubble detection

d = u6.U6()
print (d.configU6())
print (d.getCalibrationData())
d.writeRegister(50590, 15)
print (d.configU6())
print (d.getCalibrationData())

start_time = time.time()
while (True):
    input0 = (d.getAIN(0))
    input1 = (d.getAIN(1))
    input2 = (d.getAIN(2))
    input3 = (d.getAIN(3))
    input4 = (d.getAIN(4))
    input5 = (d.getAIN(5))
    run_time = time.time() - start_time
    
    # print('bubble detector run time:', run_time)
    if ((input0 > THRESHOLD)   or (run_time > TIMEOUT)):
        break
    # print (timestamp, input0, input1, input2, input3, input4, input5)
    # print("AI0={:0.2f}".format(input0))
    time.sleep(.01)