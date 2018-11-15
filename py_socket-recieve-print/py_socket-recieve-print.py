import socket

BUF_SIZE = 1024
server_addr = ('192.168.192.5',10000)

#socket的类型是socket.SOCK_DGRAM(udp使用的)
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#服务端照例绑定地址
server.bind(server_addr)

#循环接受客户端发送数据,并将数据发回

count=0
flag=1
f=open('zidonglianjie.exe','rb')
while True:
    if count==0:
        print ("Are You Ready?")
        data,client_addr = server.recvfrom(BUF_SIZE)
        print ('来自',client_addr,' 的数据是: ',data.decode('utf-8'))

    data=f.read(BUF_SIZE)
    if str(data)!="b''":
        server.sendto(data,client_addr)
        print(data)#此处打印注意被刷屏,仅测试用
    else:
        server.sendto('end'.encode('utf-8'),client_addr)#此处为文件结束,发送结束通知给客户端
        break

    data,client_addr = server.recvfrom(BUF_SIZE)
    print ('接受自 ',client_addr,' 收到数据为 : ',data.decode('utf-8'))
    count+=1
print('循环了'+str(count))
server.close()