# coding: utf-8

"""
    socket server端
"""

import socket                   # 导入socket模块

s = socket.socket()             # 创建socket对象
host = socket.gethostname()     # 获取本地主机名
port = 8080                     # 设置端口
addr = (host, port)
s.bind(addr)                    # 绑定端口

s.listen(5)                     # 等待客户端连接
while True:
    c, addr = s.accept()
    print 'address: ', addr     # 打印连接地址
    # 提示输入要发送的数据
    input_str = raw_input('input data: ')
    c.send(input_str)           # 发送输入的数据
    c.close()                   # 关闭连接
