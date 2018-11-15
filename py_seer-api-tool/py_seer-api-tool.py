#-*- encoding: utf-8 -*-
import socket
if __name__=="__main__":
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("192.168.173.1", 19204))             #seer主机，状态API端口
    s.send(b'\x5A\x01\x00\x01\x00\x00\x00\x00\x03\xE8\x00\x00\x00\x00\x00\x00') #API报文结构：包头+数据区十六进制
    buff=[]
    #接收数据结构化预留#
    buff.append(s.recv(1024))
    print('当前机器人状态为：\n', buff)

    #判断验证预留#
    if "" in buff:
        print('yes')
    else:
        print('no')
    s.close()
    #输出报表TXT预留#

