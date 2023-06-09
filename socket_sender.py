#!/usr/bin/env python3
import socket
#import rospy

UDP_IP = "127.0.0.1" # 受信するIPアドレス
UDP_PORT = 5005 # 受信するポート番号
MESSAGE = "Hello, World!"

#rospy.init_node('udp_node', anonymous=True) # ROSノードを初期化

# UDPソケットを作成し、受信するIPアドレスとポート番号を設定
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
     try:
        # データを送信
        sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
        print(f"Sent message: {MESSAGE}")

     except KeyboardInterrupt:                      
         print('end')
         break
sock.close()
