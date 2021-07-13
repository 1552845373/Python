# 读取单个txt并绘图
# import matplotlib.pyplot as plt
#
# def openfile(filepath='C:\\Users\\陌离\\Desktop\\munk.txt'):
#     x, y = [], []
#     with open(filepath, 'r') as f:
#         for line in f:
#             line = line.replace('/','').strip().split()
#             ystr, xstr = line
#             x.append(eval(xstr)), y.append(eval(ystr))
#         return x, y
#
# def drawing(x, y):
#     fig, ax = plt.subplots(1, 1)
#     plt.scatter(x, y)
#     ax.invert_yaxis()
#     plt.show()
#
# if __name__ == '__main__':
#     x, y = openfile()
#     drawing(x, y)

# 批量读取指定路径下的.txt文件并绘图
import matplotlib.pyplot as plt
import os

def getfilepath(folderpath='C:\\Users\\陌离\\Desktop\\o1t1'):
    filepaths = []
    folder = os.listdir(folderpath)
    for filepath in folder:
        if os.path.splitext(filepath)[1] == '.txt':
            filepaths.append(folderpath+'\\'+filepath)
    return filepaths

def openfile(folderpath='C:\\Users\\陌离\\Desktop\\o1t1', filepaths=[]):
    x, y = [], []
    for filepath in filepaths:
        with open(filepath, 'r') as f:
            if filepath in [folderpath+'\\'+'result.txt',folderpath+'\\'+'output.txt']:
                for line in f.readlines()[:-2]:
                    line = line.strip().split()
                    zstr, ystr, xstr = line
                    x.append(eval(xstr)), y.append(eval(ystr))
            else:
                for line in f.readlines():
                    line = line.strip().split()
                    zstr, ystr, xstr = line
                    x.append(eval(xstr)), y.append(eval(ystr))
    return x, y

def drawing(x, y):
    fig, ax = plt.subplots(1, 1)
    plt.scatter(x, y)
    ax.invert_yaxis()
    plt.show()

if __name__ == '__main__':
    folderpath = 'C:\\Users\\陌离\\Desktop\\o1t1'
    filepaths = getfilepath(folderpath)
    x, y = openfile(folderpath, filepaths)
    drawing(x, y)
