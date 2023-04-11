import random
import socket

tcpclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpclient.connect(("20.28.230.252", 65432))
ret = tcpclient.recv(1024)
print(ret.decode('utf-8'))


while 1:
    # while 1:
    data = random.choice(["1\n", "2\n", "3\n"])
    tcpclient.send(data.encode('utf-8'))
    ret = tcpclient.recv(1024)
    print(ret.decode('utf-8'))
    if len(ret.decode('utf-8')) == 4:
        # ret = tcpclient.recv(1024)
        # print(ret.decode('utf-8'))
        print(str(ret.decode('utf-8')) == "Z\nA\n")

        print("***")
        print(ret.decode('utf-8')[0])
        print(ret.decode('utf-8')[1])
        print(ret.decode('utf-8')[2])
        print("***")
        break
