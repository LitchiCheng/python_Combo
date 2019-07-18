# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dictionary.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import shutil
import docx,os,sys
from PyQt5 import QtCore, QtGui, QtWidgets

def make_folder(path):
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path) 
        return True
    else:
        return False

def del_file(path):
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        return True
    else:
        shutil.rmtree(path)
        return False

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2000, 1500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.total_num = QtWidgets.QLabel(self.centralwidget)
        self.total_num.setObjectName("total_num")
        self.gridLayout.addWidget(self.total_num, 2, 0, 1, 1)
        self.keyword = QtWidgets.QLabel(self.centralwidget)
        self.keyword.setObjectName("keyword")
        self.gridLayout.addWidget(self.keyword, 0, 0, 1, 1)
        self.text = QtWidgets.QLabel(self.centralwidget)
        self.text.setObjectName("text")
        self.gridLayout.addWidget(self.text, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 1, 1, 1, 5)
        self.insert_pb = QtWidgets.QPushButton(self.centralwidget)
        self.insert_pb.setObjectName("insert_pb")
        self.gridLayout.addWidget(self.insert_pb, 0, 3, 1, 1)
        self.query_pb = QtWidgets.QPushButton(self.centralwidget)
        self.query_pb.setObjectName("query_pb")
        self.gridLayout.addWidget(self.query_pb, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        mkpath="\\dictionary\\"        #填你想命名的文件夹名
        pwd = os.getcwd()
        pwd = pwd.replace('\\','\\\\')
        self.dictionary_file = pwd + mkpath
        if(not os.path.exists(self.dictionary_file)):
            del_file(self.dictionary_file)         #先删掉
            make_folder(self.dictionary_file)        #创建当前目录下的文件夹

        self.insert_pb.clicked.connect(self.insertPB)
        self.query_pb.clicked.connect(self.queryPB)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "小熊专用"))
        self.query_pb.setText(_translate("MainWindow", "query"))
        self.total_num.setText(_translate("MainWindow", "total:"))
        self.keyword.setText(_translate("MainWindow", "keyword"))
        self.lineEdit.setText(_translate("MainWindow", ""))
        self.text.setText(_translate("MainWindow", "text"))
        self.insert_pb.setText(_translate("MainWindow", "save"))

    def insertPB(self):
        text_name = self.lineEdit.text()
        key_word_file = self.dictionary_file + "\\\\" + text_name + ".md"
        file = open(key_word_file,'w+', encoding='utf-8')
        # print(self.plainTextEdit.toPlainText())
        file.write(self.plainTextEdit.toPlainText())
        file.close
    # def queryPB(self):
    #     text_name2 = self.lineEdit.text()
    #     key_word_file = self.dictionary_file + "\\\\" + text_name2 + ".txt"
    #     if(os.path.exists(key_word_file)):
    #         file = open(key_word_file,'r+')
    #         text = file.read()
    #         self.plainTextEdit.setPlainText(text)
    #         file.close()
    #     else:
    #         self.plainTextEdit.setPlainText("词库中未录入该关键词")
    
    def queryPB(self):
        self.plainTextEdit.clear()
        pwd = os.getcwd()
        address = pwd + "\\source"
        filenames=os.listdir(address)
        for filename in filenames:
            filepath = address+'\\'+filename
            ext = os.path.splitext(filepath)[1]
            if ext == ".docx":
                document = docx.opendocx(filepath)  #打开文件demo.docx
                docx_lines = docx.getdocumenttext(document)
                docx_lines_num = len(docx_lines)
            elif ext == ".md":
                document = open(filepath,'r',encoding = "utf-8")  #打开文件demo.docx
                docx_lines = document.readlines()
                docx_lines_num = len(docx_lines)
                print(docx_lines_num)
            last_head = 0
            last_tail = 0
            for index,line in enumerate(docx_lines):
                if self.lineEdit.text() in line or self.lineEdit.text().capitalize() in line:
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
                            # print("来源尾1：" + str(now_index_tail))
                            now_index_tail = now_index_tail + 1
                            break
                    if (last_head != now_index_head) or (last_tail != now_index_tail):
                        last_head = now_index_head
                        last_tail = now_index_tail
                        for i in docx_lines[now_index_head:now_index_tail]:
                            #print(i)
                            string.append(i + "\n")
                        #print("\n")
                        string.append("\n")
                        #print("".join(string))
                        # self.plainTextEdit.append("".join(string))
                        self.plainTextEdit.appendPlainText("".join(string))

class MyMainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # plainTextEdit.setPlainText("sdfsdfs")
        
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyMainWindow()
    ui.setupUi(MainWindow)
    # ui.plainTextEdit.setPlainText("dsf")
    # print(ui.plainTextEdit.toPlainText())
    MainWindow.show()
    sys.exit(app.exec_())