"""

"""

import serial

ser = serial.Serial('/dev/tty.usbmodem14101', 9600)


def clockwise(deg):
    """


    :param deg:
    :return:
    """
    cmd = 'a' + '{:03d}'.format(deg) + '.'
    send_cmd(cmd)


def counter_clockwise(deg):
    """


    :param deg:
    :return:
    """
    cmd = 'b' + '{:03d}'.format(deg) + '.'
    send_cmd(cmd)


def launch():
    cmd = 'c000.'
    send_cmd(cmd)


def send_cmd(data):
    """


    :param data:
    :return:
    """
    for i in data:
        ser.write(ord(i).to_bytes(1, byteorder='big'))
