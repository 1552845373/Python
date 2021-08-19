#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/9/9 20:34
# @Author : Cheng
# @File : 链表.py
# @Software : PyCharm

class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class SingleList(object):
    def __init__(self):
        self.__head = None

