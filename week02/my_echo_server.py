#!/usr/bin/env python
import socket
import os
import struct
import json


""" echo server 传输单个文件的服务端 """


HOST = 'localhost'
PORT = 20000
SHARE_DIR = 'D:\\python\\Python005\\week02\\share'


def get_file_path(file_name):
    """ 获取文件路径 """
    return os.path.join(SHARE_DIR, f'{file_name}.json')


def echo_server():
    """ Echo Server 的 Server 端 """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(10)
    while True:  # 通信循环
        print('准备建立通信中...')
        conn, addr = s.accept()
        print(f'建立成功，客户端为：[{addr}]')

        # 1. 接收命令
        res = conn.recv(1024)

        # 2. 解析命令，提取响应命令参数
        if not res:
            break

        filename = res.decode('utf-8').strip()
        fp = get_file_path(filename)

        # 3. 以读的形式打开文件，读取内容发送给客户端
        #    1. 制作固定长度的报头
        header_dic = {
            'filename': f'{filename}.json',  # 文件名
            'file_size': os.path.getsize(fp)  # 文件大小
        }
        header_json = json.dumps(header_dic)
        header_bytes = header_json.encode('utf-8')

        #    2. 先发送报头的长度
        conn.send(struct.pack('i', len(header_bytes)))

        #    3. 再发报头
        conn.send(header_bytes)

        #    4. 再发真实的数据
        with open(fp, 'rb') as f:
            for line in f:
                conn.send(line)

    print('--- 服务端已退出连接 ---')
    s.close()


if __name__ == '__main__':
    echo_server()  # 启动echo server
