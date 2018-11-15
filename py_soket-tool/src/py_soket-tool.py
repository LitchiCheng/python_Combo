
import socket
import struct
import time
import sys
import os
F4kCommandPort = 15003
F4kAddr = ('192.168.192.4', F4kCommandPort)
def f4kernelcommand(packHead, arg):
    if arg == []:
        arg = [0xffffffff]
    msg = struct.pack('<' + str(len(arg) + 1) + 'I', packHead, *arg)
    so = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    so.settimeout(0.05)
    so.sendto(msg, F4kAddr)
    so.close()

while(1):
    print("1.陀螺仪断电（次数建议100以上） 2.提高陀螺仪数据冻结阈值(次数建议1000以上)")
    command = int(input("选择序号并回车："))
    time1 = int(input("输入连续发送指令次数并回车："))
    if(command == 1):
        while(time1):
            f4kernelcommand(0x0000101A,[0x03])
            time1 = time1 - 1
            time.sleep(1)
    elif(command == 2):
        while (time1):
            f4kernelcommand(0x0000101A, [0x0D])
            time1 = time1 - 1
            time.sleep(0.001)

