#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/4/13 20:06
# @Author : Cheng
# @File : 线性回归.py
# @Software : PyCharm

# from sklearn.linear_model import LinearRegression
#
# x = [[80, 86], [82, 80], [85, 78], [90, 90], [86, 82], [82, 90], [78, 80]]
# y = [84.2, 80.6, 80.1, 90, 83.2, 87.6, 79.4]
# estimator = LinearRegression() # 实例化估计器
# estimator.fit(x, y) # 使用fit方法训练模型
# print(estimator.coef_) # estimator.coef_是回归系数
# print(estimator.predict([[100, 80]]))


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

with open(r'C:\Users\陌离\Desktop\新建文件夹\well17vpjj1.txt','r') as f:
    data = f.read().split()
    x1 = list(map(eval, data))

with open(r'C:\Users\陌离\Desktop\新建文件夹\well17vpkx1.txt','r') as f:
    data = f.read().split()
    x2 = list(map(eval, data))

with open(r'C:\Users\陌离\Desktop\新建文件夹\well17vprlx1.txt','r') as f:
    data = f.read().split()
    x3 = list(map(eval, data))

with open(r'C:\Users\陌离\Desktop\新建文件夹\well17vp1.txt','r') as f:
    data = f.read().split()
    y = list(map(eval, data))

x = [[x1[i], x2[i], x3[i]] for i in range(len(x1))]

estimator = LinearRegression() # 实例化估计器
estimator.fit(x, y) # 使用fit方法训练模型

score = estimator.score(x, y)
y_predict = estimator.predict(x)
error = mean_squared_error(y, y_predict)
print("\t准确率为:", score)
print("\t回归系数为:", estimator.coef_)
print("\t偏置:", estimator.intercept_)
print("\t均方误差为:", error)


# # 波士顿房价预测
# """
# 1、获取数据
# 2、数据集划分
# 3、特征工程（标准化）
# 4、机器学习
# 5、模型评估
# """

# from sklearn.datasets import load_boston
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LinearRegression, SGDRegressor
# from sklearn.metrics import mean_squared_error
#
# def machine_learning(estimator):
#     # 1、获取数据
#     boston = load_boston()
#     # 2、数据集划分
#     x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2, random_state=22)
#     # 3、特征工程（标准化）
#     transfer = StandardScaler()
#     x_train = transfer.fit_transform(x_train)
#     x_test = transfer.fit_transform(x_test)
#     # 4、机器学习
#     estimator.fit(x_train, y_train)
#     # 5、模型评估
#     score = estimator.score(x_test, y_test)
#     y_predict = estimator.predict(x_test)
#     error = mean_squared_error(y_test, y_predict)
#     print("\t准确率为:", score)
#     print("\t回归系数为:", estimator.coef_)
#     # print("\t偏置:", estimator.intercept_)
#     # print("预测值为:\n", y_predict)
#     # print("真实值为:\n", y_test)
#     print("\t误差为:", error)
#
# def estimator1():
#     estimator = LinearRegression()
#     return estimator
#
# def estimator2():
#     estimator = SGDRegressor()
#     return estimator
#
# if __name__ == '__main__':
#     estimator1 = estimator1()
#     estimator2 = estimator2()
#     print("正规方程:")
#     machine_learning(estimator1)
#     print("梯度下降:")
#     machine_learning(estimator2)
