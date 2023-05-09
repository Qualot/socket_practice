#!/usr/bin/env python3
import socket
import threading

# 送信用関数
def send_thread():
    UDP_IP = "127.0.0.1" # 送受信するIPアドレス
    UDP_PORT = 5005 # 送信するポート番号
    MESSAGE = "Hello, World!"

    print("hoge_send")
    # UDPソケットを作成し、送信するIPアドレスとポート番号を設定
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #sock.bind(('', 0)) # 送信ポート番号を自動割り当て
    #sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # アドレスを再利用できるように設定

    # データを送信
    sock.sendto(MESSAGE.encode(), (UDP_IP, 5006))
    print("hoge_sent")
    sock.close()

# 受信用関数
def receive_thread():
    UDP_IP = "127.0.0.1" # 送受信するIPアドレス
    UDP_PORT = 5006 # 受信するポート番号

    print("hoge_receive")
    # UDPソケットを作成し、受信するIPアドレスとポート番号を設定
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    # データを受信
    data, addr = sock.recvfrom(1024)
    print(f"Received message: {data}")
    print("hoge_received")
    sock.close()

# 送信スレッドを作成し実行
send_t = threading.Thread(target=send_thread)
send_t.start()

# 受信スレッドを作成し実行
receive_t = threading.Thread(target=receive_thread)
receive_t.start()

# スレッドが終了するまで待機
send_t.join()
receive_t.join()
