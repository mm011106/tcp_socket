# -*- coding:utf-8 -*-
import socket

# host = "localhost" #お使いのサーバーのホスト名を入れます
host ='192.168.0.102' 
port = 10080 #クライアントと同じPORTをしてあげます

# Socket オブジェクトの作成　アドレス：インターネット、ソケット型：ストリーム
serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Socket オプションの指定　API層でのオプション：ソケット解放後すぐに再利用可能
serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


serversock.bind((host,port)) #IPとPORTを指定してバインドします
serversock.listen(10) #接続の待ち受けをします（キューの最大数を指定）

print 'Waiting for connections...'
clientsock, client_address = serversock.accept() #接続されればデータを格納


print 'connected with :' ,client_address
clientsock.settimeout(5) # server expect getting data within 5 sec after the last transfer
print 'timeout was :' , clientsock.gettimeout()

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     s.bind((host, port))
#     s.listen(1)
#     print 'open the socket'
#     conn, addr = s.accept()
#     with conn:
#         print('Connected by', addr)
#         while True:
#             data = conn.recv(1024)
#             if not data: break
#             print data
#             conn.sendall(data)
# 
# print 'connection was closed'
with open('readings.txt','a') as f:
    while True:
        rcvmsg = clientsock.recv(1024)
        print 'Received -> %s' % (rcvmsg)
        f.write(rcvmsg)
        clientsock.sendall('!')
        if rcvmsg == '':
            break
#     print 'Type message...'
#     s_msg = raw_input()
#     if s_msg == '':
#       break
#    print 'Wait...',

#     clientsock.sendall(s_msg) #メッセージを返します

clientsock.close()

