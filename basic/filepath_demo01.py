# coding: utf-8

"""
    打印python正在运行本程序的当前文件及目录的绝对路径
"""
import os

print("当前目录的绝对路径： %s" % os.getcwd())
print("当前目录的绝对路径： %s" % os.path.abspath('.')) 
print("当前正在运行的文件的绝对路径： %s" % os.path.abspath(__file__))