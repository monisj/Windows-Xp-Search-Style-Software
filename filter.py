from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QDialog
from PyQt5 import QtCore
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
class TestSortFilterProxyModel(QtGui.QSortFilterProxyModel,result):
    def __init__(self, parent=None):
        super(TestSortFilterProxyModel, self).__init__(parent)
        self.filter = ['folder0/file0', 'folder1/file1'];

    def filterAcceptsRow(self, source_row, source_parent):
        index0 = self.sourceModel().index(source_row, 0, source_parent)
        filePath = self.sourceModel().filePath(index0) 

        for folder in self.filter:
            if filePath.startsWith(folder) or QtCore.QString(folder).startsWith(filePath):
                return True;        
        return False 
