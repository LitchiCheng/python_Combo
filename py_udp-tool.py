import socket
import time
import struct

address = ('192.168.192.4', 5014)
so = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # so.settimeout(0.05)
    arg = [0xffffffff]
    msg = struct.pack('<' + str(len(arg) + 1) + 'I', 0x0000101A, *arg)
    so.sendto(msg, address)
    # time.sleep(10)
    data, addr = so.recvfrom(1024)
    print(" %s:%s" %addr)
    print(" %s" %data)
so.close() 