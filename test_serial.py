import serial
import time
import test2

def coder(rw, id, reg, val):
    command = 'M'
    command += chr((rw<<7) + id)
    command += chr((reg<<2) + (val>>8))
    command += chr(val % 256)
    return command


com = serial.Serial('/dev/ttyO2', 460800)

com.write(coder(1,1,30,500))

#while(1):
#    com.write(coder(0,1,36,0))
#    low=com.read()
#    com.write(coder(0,1,37,0))
#    high=com.read()
#    print (ord(high)<<8)+ord(low)


