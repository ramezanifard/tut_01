import serial

class Pump():
    def __init__(self,position=0, speed=1000, acceleration=30000):
        self.position = position
        self.speed = speed
        self.acceleration = acceleration
        self.ser = serial.Serial()
        self.ser.baudrate = 9600
        self.ser.timeout = 3
        self.ser.port = 'COM8'
        # print(self.ser)

        self.ser.open()
        # print("port is open?", self.ser.is_open)

        # clear buffers
        self.ser.reset_output_buffer()
        self.ser.reset_input_buffer()
        
        
    def pump_init(self):
        self.ser.write(b'/1ZR\r\n')
        self.ser.flush()


    def set_pos_absolute(self, position):
        
        str1 = '/1A'+str(position)+'R\r\n'
        self.ser.write(str1.encode())
        # self.ser.write(b'/1A1000R\r\n')
        # self.ser.write(b'/1A0R\r\n')


    def set_pickup(self, position):
        str1 = '/1P'+str(position)+'R\r\n'
        self.ser.write(str1.encode())

    def set_dispense(self, position):
        str1 = '/1D'+str(position)+'R\r\n'
        self.ser.write(str1.encode())


    def set_speed(self, speed):
        str1 = '/1V'+str(speed)+'R\r\n'
        # print('set speed:',str1)
        self.ser.write(str1.encode())

    def set_valve(self, pos):
        str1 = '/1'+pos+'R\r\n'
        # print('set speed:',str1)
        self.ser.write(str1.encode())
        pass
        

    def close(self):
        self.ser.close()



    def read(self):
        try:


            cr = "\r".encode()
            response_frame = b''
            response_byte = self._read(size=1)  # read one byte at a time, timeout is set on instance level

            # read until stop byte
            while response_byte != cr:
                response_frame += response_byte
                
                response_byte = self._read(size=1)
                # print(response_byte)
        except:
            print("excepton!!")
        else:    
            print(response_frame)
        # res = ser.readline()




    def _read(self, size):
        """
        Read n=size bytes from serial, if <n bytes are received (serial.read() return because of timeout), raise a timeout.
        """
        recv = self.ser.read(size=size)
        if len(recv) < size:
            print("miatake!!!")
        else:
            return recv


def is_float(element: any) -> bool:
    #If you expect None to be passed:
    if element is None: 
        return False
    try:
        float(element)
        return True
    except ValueError:
        return False