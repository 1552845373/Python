#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/7/12 17:07
# @Author : Cheng
# @File : first.py
# @Software : PyCharm

import sys
import untitled
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = untitled.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
