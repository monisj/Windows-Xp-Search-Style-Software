from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QDialog
from PyQt5 import QtCore
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os
import Blink_Button
import os, fnmatch
import re
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(874, 596)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(MainWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addWidget(self.centralwidget)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 871, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(43, 0, 20, 41))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(180, 0, 20, 41))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 40, 221, 541))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 191, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 201, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 191, 16))
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(10, 250, 201, 141))
        self.groupBox.setObjectName("groupBox")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(10, 20, 70, 17))
        self.checkBox.setShortcut("")
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 50, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 80, 70, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 110, 111, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(10, 200, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 200, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 874, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSearch_From_Specific_Location = QtWidgets.QAction(MainWindow)
        self.actionSearch_From_Specific_Location.setObjectName("actionSearch_From_Specific_Location")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionClear_List = QtWidgets.QAction(MainWindow)
        self.actionClear_List.setObjectName("actionClear_List")
        self.actionSelect_All = QtWidgets.QAction(MainWindow)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionProperties = QtWidgets.QAction(MainWindow)
        self.actionProperties.setObjectName("actionProperties")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSearch_From_Specific_Location)
        self.menuFile.addAction(self.actionDelete)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionClear_List)
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuTools.addAction(self.actionProperties)
        self.menuTools.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        #Search column View
        #self.columnView = QtWidgets.QColumnView(self.centralwidget)
        #self.columnView.setGeometry(QtCore.QRect(220, 50, 651, 521))
        #self.columnView.setResizeGripsVisible(True)
        #self.columnView.setObjectName("columnView")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(220, 50, 651, 521))
        
        self.treeView.setObjectName("columnView")
        self.horizontalLayout.addWidget(self.treeView)
        path = QDir.rootPath()
        
        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath(QDir.rootPath())
        
        self.fileModel = QFileSystemModel()
        self.fileModel.setFilter(QDir.NoDotAndDotDot |  QDir.Files)
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath((QtCore.QDir.rootPath()))
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.dirModel.index(path))
        self.treeView.doubleClicked.connect(self.on_clicked)
        self.treeView.setObjectName("treeView")
        self.treeView.setColumnWidth(0,300)

        logoPath = QDir.homePath()
        self.logoModel = QFileSystemModel()
        self.logoModel.setRootPath(logoPath)
        self.logoModel.setFilter(QDir.NoDotAndDotDot | QDir.Files | QDir.NoSymLinks)
        print(logoPath)

        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 201, 31))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 100, 201, 31))
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 160, 201, 31))
        self.comboBox_3.setEditable(True)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.setModel(self.logoModel)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Search for files or folders"))
        self.label_2.setText(_translate("MainWindow", "Containing text (for wordprocessor files)"))
        self.label_3.setText(_translate("MainWindow", "Look in (Directory)"))
        self.groupBox.setTitle(_translate("MainWindow", "Options"))
        self.checkBox.setText(_translate("MainWindow", "Date"))
        self.checkBox_2.setText(_translate("MainWindow", "Size"))
        self.checkBox_3.setText(_translate("MainWindow", "Type"))
        self.checkBox_4.setText(_translate("MainWindow", "Advance Options"))
        
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.pushButton.clicked.connect(self.search)
        self.pushButton_2.setText(_translate("MainWindow", "Stop"))
        self.pushButton_2.clicked.connect(self.stop)
        
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSearch_From_Specific_Location.setText(_translate("MainWindow", "Search From Specific Location"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionClear_List.setText(_translate("MainWindow", "Clear List"))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All"))
        self.actionProperties.setText(_translate("MainWindow", "Properties"))

    def on_clicked(self, index):
        path = self.fileModel.fileInfo(index).absoluteFilePath()
        #Tab Reading for index values 
        os.startfile(path)
        
    def stop(self):
        print("Program Stoped")
        self.pushButton.setEnabled(True)

    def search(self):
        print("Search started")
        self.pushButton.setEnabled(False)
        file_name=self.comboBox.currentText()
        print(file_name)
        path_tmp1 = self.comboBox_3.currentText()
        print(path_tmp1)
        path_tmp = re.findall("[A-Z]:",path_tmp1)
        print(path_tmp[-1])
        cur_dir=path_tmp[-1]+'/'''
        print(cur_dir)
       
        result = []
        # Wlaking top-down from the root
        for root, dir, files in os.walk(cur_dir):
            for i in files:
                b=re.findall(".*"+file_name+".*.*",i,re.IGNORECASE)
                if b==[]:
                    pass
                elif b!=[]:
                    for i in files:
                        if b[-1]==i:
                            result.append(os.path.join(root, b[-1]))
        if result!=[]:
            for i in result:
                print(i)
            self.pushButton.setEnabled(True)
                
        else:
            print("No match")
            self.pushButton.setEnabled(True)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
