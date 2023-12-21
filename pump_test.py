import serial
import time

def _read( size):
    """
    Read n=size bytes from serial, if <n bytes are received (serial.read() return because of timeout), raise a timeout.
    """
    recv = ser.read(size=size)
    if len(recv) < size:
        print("miatake!!!")
    else:
        return recv
    

ser = serial.Serial()
ser.baudrate = 9600
ser.timeout = 3
ser.port = 'COM8'
print(ser)

ser.open()
print("port is open?", ser.is_open)

# clear buffers
ser.reset_output_buffer()
ser.reset_input_buffer()
# ser.write('/1ZR\r\n'.encode())
# ser.write(b'/1A6000R\r\n')
# ser.write(b'/1V500R')
# ser.write(b'/1A1000R\r\n')


# ser.write(b'/1V1000R\r\n')
# time.sleep(1)
# ser.flush()
# time.sleep(1)
# ser.write(b'/1A1000R\r\n')
# time.sleep(10)
# ser.write(b'/1V100R\r\n')
# time.sleep(1)
# ser.write(b'/1A0R\r\n')



ser.flush()



try:


    cr = "\r".encode()
    response_frame = b''
    response_byte = _read(size=1)  # read one byte at a time, timeout is set on instance level

    # read until stop byte
    while response_byte != cr:
        response_frame += response_byte
        
        response_byte = _read(size=1)
        print(response_byte)
except:
    print("excepton!!")
else:    
    print(response_frame)
# res = ser.readline()




ser.close()

