# -*- coding:utf-8 -*-
import socket

# host = "localhost" #お使いのサーバーのホスト名を入れます
host = "192.168.0.102" #お使いのサーバーのホスト名を入れます
port = 10080 #適当なPORTを指定してあげます

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #オブジェクトの作成をします

client.connect((host, port)) #これでサーバーに接続します

print 'connected with', client.getpeername()
# client.send("from nadechin") #適当なデータを送信します（届く側にわかるように）
# 
# response = client.recv(4096) #レシーブは適当な2進数にします（大きすぎるとダメ）
# 
# print response
# client.send("hi")

client.settimeout(5)

while True:
    s_msg = raw_input()
    if s_msg == '':
      break
    client.sendall(s_msg) #メッセージを返します

#   res=client.recv(4096)
#   print res
#   client.send(res)

# issue
# サーバが落ちたときに　見えないメッセージがいっぱい届く
# ハンドリング　サーバー無しの時の処理
# ハンドリング　サーバが接続後に落ちたとき
# 