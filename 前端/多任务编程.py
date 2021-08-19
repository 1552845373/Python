#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/4/1 19:09
# @Author : Cheng
# @File : 多任务编程.py
# @Software : PyCharm


# # 多进程
# # 子进程会拷贝主进程中的变量、函数（方法）
# import multiprocessing
# import time
#
# def dance():
#     for i in range(3):
#         print('跳舞中...')
#         time.sleep(0.2)
#
# def sing():
#     for i in range(3):
#         print('唱歌中...')
#         time.sleep(0.2)
#
# # 主模块的作用
# # 1、防止别人调用时执行（程序测试时使用）
# # 2、防止子进程拷贝，陷入无限递归
# if __name__ == '__main__':
#     # 创建子进程
#     dance_process = multiprocessing.Process(target=dance)
#     sing_process = multiprocessing.Process(target=sing)
#     # 执行子进程
#     dance_process.start()
#     # 等待第一个子进程执行结束后执行第二个子进程
#     dance_process.join()
#     sing_process.start()


# 多线程
import threading
import time

g_num = 0
lock = threading.Lock()

def add_num1():
    global g_num
    lock.acquire()
    for i in range(1000000):
        g_num += 1
    lock.release()
    print(f'sum1:{g_num}')

def add_num2():
    global g_num
    lock.acquire()
    for i in range(1000000):
        g_num += 1
    lock.release()
    print(f'sum2:{g_num}')

if __name__ == '__main__':
    start_time = time.time()

    first_thread = threading.Thread(target=add_num1)
    second_thread = threading.Thread(target=add_num2)

    first_thread.start()
    second_thread.start()

    end_time = time.time()
    # 主线程等待第二个线程执行完成以后代码再继续执行
    # 线程同步：一个任务执行完成以后另外一个任务才能执行，同一个时刻只有一个任务在执行
    second_thread.join()
    print(f'g_num:{g_num}\n执行时间：{end_time-start_time}')
