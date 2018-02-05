# coding: utf-8

"""
    socket client端
"""

import socket                   # 导入socket模块

while True:
    s = socket.socket()         # 创建socket对象
    host = socket.gethostname() # 获取本机主机名
    port = 8080                 # 设置端口
    addr = (host, port)
    s.connect(addr)             # 绑定端口
    print s.recv(1024)          # 打印接收的数据
    s.close()                   # 关闭连接