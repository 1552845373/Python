#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/6/17 14:21
# @Author : Cheng
# @File : TCP客户端、服务端开发.py
# @Software : PyCharm


# # TCP客户端程序开发
# import socket
#
# # 1.创建客户端套接字对象
# tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET：ipv4；SOCK_STREAM：tcp传输协议
# # 2.和服务端套接字建立连接
# tcp_client_socket.connect(('192.168.164.1', 8080))
# # 3.发送数据
# send_data = '你好'.encode('gbk') # 按gbk编码方式转成二进制，windows中是gbk，linux和mac中是utf-8。
# tcp_client_socket.send(send_data)
# # 4,接收数据
# recv_data = tcp_client_socket.recv(1024) # 这次接收的数据最大字节数是1024
# print(recv_data.decode('gbk'))
# # 5.关闭客户端套接字
# tcp_client_socket.close()


# TCP服务端程序开发
import socket
import threading

# 定义处理客户端数据的函数
def handle_info(new_socket, client_ip_socket):
    while True:
        # 5.接收数据
        recv_data = new_socket.recv(1024)
        if recv_data:
            print(f'用户{client_ip_socket[0]}:',recv_data.decode('gbk'))
            # 6.发送数据
            str = '数据已接受'
            send_data = str.encode('gbk')
            new_socket.send(send_data)
        else:
            print(f'已与用户{client_ip_socket[0]}断开连接')
            break
    new_socket.close()

if __name__ == '__main__':

    # 1.创建服务端端套接字对象
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True) # 设置端口号复用
    # 2.绑定端口号
    tcp_server_socket.bind(('', 8080))
    # 3.设置监听
    tcp_server_socket.listen(128)
    while True:
        # 4.等待接受客户端的连接请求
        new_socket, client_ip_socket = tcp_server_socket.accept()
        print(f'用户{client_ip_socket[0]}连接成功')
        # 创建接收客户端数据的子线程
        handle_thread = threading.Thread(target=handle_info, args=(new_socket, client_ip_socket), daemon=True)
        handle_thread.start()

    # 7.关闭套接字
    # tcp_server_socket.close()
