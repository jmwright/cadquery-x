import os
import sys
from PySide import QtCore, QtGui
from pyqode.core.modes import FileWatcherMode
from pyqode.python.widgets import PyCodeEdit

class codeViewer(QtGui.QWidget):
    def __init__(self, *kargs):
        server_path = os.path.join('.', 'cq_server.py')
        libs_dir_path = '/home/jwright/Documents/cadquery-x/gui/libs'

        ver = hex(sys.hexversion)
        interpreter = "python%s.%s" % (ver[2], ver[4])  # => 'python2.7'

        PyCodeEdit(server_script=server_path, interpreter=interpreter, args=['-s', libs_dir_path])