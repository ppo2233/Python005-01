import socket
import os
import json
import struct
import threading


""" echo server 传输单个文件的客户端 """


HOST = 'localhost'
PORT = 20000
DOWNLOAD_DIR = 'D:\\python\\Python005\\week02\\download'


try:
    import myutils  # 自定义通用积累库
    myutils.mkdir_if_not(DOWNLOAD_DIR)
except:
    def mkdir_if_not(dir_):
        if dir_:
            if not os.path.isdir(dir_):
                os.makedirs(dir_)

    mkdir_if_not(DOWNLOAD_DIR)


def perform_echo(s, file_name):
    """ 执行echo """
    # 1. 发送数据到服务端
    s.sendall(file_name.encode())

    # 2. 接收服务端数据，并以写的方式打开文件
    # 第一步：先收报头的长度
    obj = s.recv(1024)
    header_size = struct.unpack('i', obj)[0]
    # 第二步：再收报头
    header_bytes = s.recv(header_size)

    print('---- get recv --->', header_bytes)
    # 第三步：从报头中解析出对真实数据的描述信息
    header_json = header_bytes.decode('utf-8')
    header_dic = json.loads(header_json)

    fname = header_dic['filename']
    fsize = header_dic['file_size']
    fp = os.path.join(DOWNLOAD_DIR, fname)  # 下文文件路径

    # 第四步：接收真实的数据
    with open(fp, 'wb') as wf:
        recv_size = 0
        while recv_size < fsize:
            content = s.recv(1024)
            recv_size += len(content)
            wf.write(content)
            print(f'总大小: [{fsize}]，已下载:[{recv_size}]')


# def multithreading_echo_client(s):
#     """ 多线程处理echo 的client端 """
#     for i in range(5):
#         t = threading.Thread(target=perform_echo, args=(s, f'book0'))
#         t = threading.Thread(target=perform_echo, args=(s, f'book{i}'))
#         t.start()


def echo_client():
    """ Echo Server 的 Client 端 """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:

        # 设定退出条件
        file_name = input('请输入要下载的文件名称，如"book"(当前只支持输入"book")> ')
        if file_name == 'exit':
            break
        elif file_name != 'book':
            print('当前只支持输入"book",退出请输入"exit"')
            continue

        perform_echo(s, 'book')
        # multithreading_echo_client(s)  # 多线程执行

    print('--- 客户端已退出连接 ----')
    s.close()


if __name__ == '__main__':
    echo_client()
