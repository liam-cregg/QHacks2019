import serial

ser = serial.Serial('/dev/tty96B0', 9600)


def clockwise(deg):
    cmd = 'a' + '{:03d}'.format(deg) + '.'
    sendCMD(cmd)


def counterClockwise(deg):
    cmd = 'b' + '{:03d}'.format(deg) + '.'
    sendCMD(cmd)


def launch(n):
    cmd = 'c' + '{:03d}'.format(n) + '.'
    sendCMD(cmd)


def sendCMD(data):
    for i in data:
        ser.write(ord(i).to_bytes(1, byteorder='big'))
