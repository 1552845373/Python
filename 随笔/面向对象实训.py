#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/3/25 11:04
# @Author : Cheng
# @File : 面向对象实训.py
# @Software : PyCharm

# # 应用--烤地瓜
# class SweetPotato():
#
#     def __init__(self):
#         self.cook_time = 0
#         self.static = '生'
#         self.spices = []
#
#     def cook(self, time):
#         """烤地瓜的方法"""
#         self.cook_time += time
#         if 0 <= self.cook_time < 3:
#             self.static = '生'
#         elif 3 <= self.cook_time <= 5:
#             self.static = '熟'
#         else:
#             self.static = '糊'
#
#     def add_spices(self, spices):
#         self.spices.append(spices)
#
#     def __str__(self):
#         return f'这个地瓜烤了{self.cook_time}分钟, 状态是{self.static}, 添加的调料有{self.spices}'
#
# sweetpotato1 = SweetPotato()
# print(sweetpotato1)
# sweetpotato1.cook(7)
# sweetpotato1.add_spices('香料')
# print(sweetpotato1)
# help(sweetpotato1.cook)


# # 应用--搬家具
# class Furniture():
#     def __init__(self, name, area):
#         self.name = name
#         self.area = area
#
# class Home():
#     def __init__(self, position, area):
#         self.position = position
#         self.area = area
#         self.rest_area = area
#         self.furniture = []
#
#     def add_furniture(self, furniture):
#         if furniture.area <= self.rest_area:
#             self.furniture.append(furniture.name)
#             self.rest_area -= furniture.area
#         else:
#             print('房屋剩余空间不足')
#
#     def __str__(self):
#         return f'房屋地理位置是:{self.position},面积:{self.area},剩余面积:{self.rest_area},拥有的家具:{self.furniture}'
#
# bed = Furniture('床', 10)
# home = Home('上海', 120)
# home.add_furniture(bed)
# print(home)
