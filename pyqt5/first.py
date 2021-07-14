#!/usr/bin/python3
# -*- coding : utf-8 -*-
# @Time : 2021/7/12 17:07
# @Author : Cheng
# @File : first.py
# @Software : PyCharm

# import sys
# import untitled
# from PyQt5.QtWidgets import QApplication,QMainWindow
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     mainWindow = QMainWindow()
#     ui = untitled.Ui_MainWindow()
#     ui.setupUi(mainWindow)
#     mainWindow.show()
#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("第一个主窗口应用")
        self.resize(400,300)
        self.status = self.statusBar()
        self.status.showMessage("只存在五秒",msecs=5000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = FirstMainWin()
    mainWindow.show()
    sys.exit(app.exec_())

