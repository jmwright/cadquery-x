#!/usr/bin/env python

import sys
from PySide import QtGui, QtCore
from plugins.viewer3D import viewer3D


class CQGui(QtGui.QMainWindow):
    def __init__(self):
        super(CQGui, self).__init__()

        self.initUI()

    def initUI(self):
        widge = QtGui.QWidget()

        editor1 = QtGui.QTextEdit()
        self.viewer = viewer3D.viewer3D(self)
        editor3 = QtGui.QTextEdit()

        editor3.setMaximumHeight(100)

        split1 = QtGui.QSplitter()
        split2 = QtGui.QSplitter()

        layout = QtGui.QVBoxLayout()

        container = QtGui.QWidget()
        container_layout = QtGui.QVBoxLayout()

        split1.addWidget(editor1)
        split1.addWidget(self.viewer)

        container_layout.addWidget(split1)
        container.setLayout(container_layout)

        split2.setOrientation(QtCore.Qt.Vertical)
        split2.addWidget(container)
        split2.addWidget(editor3)

        layout.addWidget(split2)

        widge.setLayout(layout)

        #The menu items
        newAction = QtGui.QAction('&New', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('New Script')
        openAction = QtGui.QAction('&Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open Script')
        saveAction = QtGui.QAction('&Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save Script')
        closeAction = QtGui.QAction('&Close', self)
        closeAction.setStatusTip('Close Script')
        exitAction = QtGui.QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit CadQuery')
        exitAction.triggered.connect(self.close)

        buildAction = QtGui.QAction('&Build', self)
        buildAction.setShortcut('F5')
        buildAction.setStatusTip('Build Script')

        #Prepare the menu bar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(closeAction)
        fileMenu.addAction(exitAction)
        buildMenu = menubar.addMenu('&Project')
        buildMenu.addAction(buildAction)
        helpMenu = menubar.addMenu('&Help')

        self.setCentralWidget(widge)

        self.setWindowTitle("CadQuery GUI (Experimental)")

        self.showMaximized()

def main():
    app = QtGui.QApplication(sys.argv)
    gui = CQGui()
    gui.viewer.InitDriver()
    gui.viewer._display.Test()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()