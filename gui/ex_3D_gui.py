#!/usr/bin/env python

from __future__ import print_function
import os
import sys
from plugins.viewer3D import viewer3D
from PySide import QtGui

libs_dir_path = '/home/jwright/Documents/cadquery-x/gui/libs' #os.path.join(".", 'libs')
sys.path.insert(0, libs_dir_path)

from pyqode.core.modes import FileWatcherMode
from pyqode.python.widgets import PyCodeEdit

from plugins.codeViewer import codeViewer

# Need to set this for PyQode
os.environ['QT_API'] = 'pyside'

def Gui():
    class AppFrame(QtGui.QWidget):
        def __init__(self, parent=None):
            QtGui.QWidget.__init__(self, parent)
            self.setWindowTitle(self.tr("CadQuery GUI (Experimental)"))
            self.resize(640, 480)
            self.viewer = viewer3D.viewer3D(self)
            server_path = os.path.join('.', 'cq_server.py')
            ver = hex(sys.hexversion)
            interpreter = "python%s.%s" % (ver[2], ver[4])  # => 'python2.7'
            #self.codePane = PyCodeEdit(server_script=server_path, interpreter=interpreter, args=['-s', libs_dir_path]) #codeViewer.codeViewer(self)
            mainLayout = QtGui.QHBoxLayout()
            mainLayout.addWidget(self.viewer)
            #mainLayout.addWidget(self.codePane)
            mainLayout.setContentsMargins(0, 0, 0, 0)
            self.setLayout(mainLayout)

        def runTests(self):
            self.viewer._display.Test()

    app = QtGui.QApplication(sys.argv)
    frame = AppFrame()
    frame.show()
    frame.viewer.InitDriver()
    frame.runTests()
    1

if __name__ == "__main__":
    Gui()
