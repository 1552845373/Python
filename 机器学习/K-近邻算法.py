#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/3/15 9:52
# @Author : Cheng
# @File : 机器学习实训.py
# @Software : PyCharm


'''
1、获取数据集
2、数据基本处理（数据集划分等）
3、特征工程（标准化、归一化等）
4、机器学习（模型训练）
5、模型评估
'''


# # K近邻法
# from sklearn.neighbors import KNeighborsClassifier
#
# x = [[39, 0, 31], [3, 2, 65], [2, 3, 55], [9, 38, 2], [8, 34, 17], [5, 2, 57], [21, 17, 5], [45, 2, 9]]
# y = [1, 2, 3, 3, 3, 2, 1, 1]
#
# estimator = KNeighborsClassifier(n_neighbors=5)
# estimator.fit(x, y)
# print(estimator.predict([[23, 3, 17]]))


# 鸢尾花种类预测
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# 1、获取数据
iris = load_iris()
# 2、数据集划分
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)
# 3、特征工程（标准化）
transfer = StandardScaler() # 创建转换器
x_train = transfer.fit_transform(x_train) # 对训练集特征值进行标准化
x_test = transfer.fit_transform(x_test) # 对测试集特征值进行标准化
# 4、机器学习
estimator = KNeighborsClassifier() # 创建估计器
estimator = GridSearchCV(estimator, param_grid={'n_neighbors':[3,5,7]}, cv=3) # 交叉验证+网格搜索
estimator.fit(x_train, y_train) # 模型训练
# 5、模型评估
score = estimator.score(x_test, y_test) # 计算模型准确率
y_predict = estimator.predict(x_test)
print(y_predict == y_test)
print("直接计算准确率：\n", score)
print("最好的参数模型：\n", estimator.best_estimator_)
print("每次交叉验证后的准确率结果：\n", estimator.cv_results_)
