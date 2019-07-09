# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'query.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import docx,re,os,sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 722, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.query)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "小熊专用查询器"))
        self.lineEdit.setText(_translate("MainWindow", "输入查询的词"))
        self.pushButton.setText(_translate("MainWindow", "查询"))
    
    def query(self):
        self.textBrowser.clear()
        pwd = os.getcwd()
        address = pwd + "\\source"
        filenames=os.listdir(address)
        for filename in filenames:
            filepath = address+'\\'+filename
            document = docx.opendocx(filepath)  #打开文件demo.docx
            docx_lines = docx.getdocumenttext(document)
            docx_lines_num = len(docx_lines)
            for index,line in enumerate(docx_lines):
                if self.lineEdit.text() in line:
                    # print(line)
                    string = []
                    string.append("文件位置：" + filepath + "\n")
                    now_index_head = index
                    now_index_tail = index
                    while True:
                        now_index_head = now_index_head - 1
                        if "来源" in docx_lines[now_index_head]:
                            # print("来源头：" + str(now_index_head))
                            break
                    while True:
                        now_index_tail = now_index_tail + 1
                        if "来源" in docx_lines[now_index_tail]:
                            # print("来源尾：" + str(now_index_tail))
                            break
                        if now_index_tail == (docx_lines_num -1):
                            # print("来源尾：" + str(now_index_tail))
                            break
                    for i in docx_lines[now_index_head:now_index_tail]:
                        # print(i)
                        string.append(i + "\n")
                    # print("\n")
                    string.append("\n")
                    print("".join(string))
                    self.textBrowser.append("".join(string))
                

class MyMainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # plainTextEdit.setPlainText("sdfsdfs")
        
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


