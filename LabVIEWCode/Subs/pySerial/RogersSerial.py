import serial,time

ser = None

def InitSerial(port,baudrate,timeout):
    global ser

    reply = 'None'
    try:
        ser = serial.Serial(port,baudrate = baudrate,timeout = timeout)  # open serial port
    except Exception as e:
        reply = e
    return reply

def N_Serial():
    global ser
    n = ser.inWaiting()
    return str(n)

def WriteSerial(text):
    global ser
    send = bytes(text, 'ascii')
    n = ser.write(send)
    return str(n)

def ReadSerial(len):
    global ser
    return str(ser.read(len))
    #return ser.read(len).decode("utf=8")

def CloseSerial():
    global ser
    ser.close()             # close port