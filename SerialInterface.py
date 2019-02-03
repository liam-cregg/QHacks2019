"""

"""

import serial

SER = serial.Serial('/dev/tty96B0', 9600)


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


def launch(n):
    """


    :param n:
    :return:
    """
    cmd = 'c' + '{:03d}'.format(n) + '.'
    send_cmd(cmd)


def send_cmd(data):
    """


    :param data:
    :return:
    """
    for i in data:
        SER.write(ord(i).to_bytes(1, byteorder='big'))
