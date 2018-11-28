#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import serial

# 你想通过串行端口读写数据，典型场景就是和一些硬件设备打交道 (比如一个机器人或传感器)

ser = serial.Serial('/dev/tty.usbmodem641',  # Device name varies
                    baudrate=9600,
                    bytesize=8,
                    parity='N',
                    stopbits=1)

"""
设备名对于不同的设备和操作系统是不一样的。比如，在 Windows 系统上，你可
以使用 0, 1 等表示的一个设备来打开通信端口” COM0”和” COM1”。一旦端口打开，
那就可以使用 read()， readline() 和 write() 函数读写数据了。例如：
"""

ser.write(b'G1 X50 Y50\r\n')
resp = ser.readline()

"""
时刻记住所有涉及到串口的 I/O 都是二进制模式的。因此，确保你的代码使用的
是字节而不是文本 (或有时候执行文本的编码/解码操作)。另外当你需要创建二进制编
码的指令或数据包的时候， struct 模块也是非常有用的。
"""
