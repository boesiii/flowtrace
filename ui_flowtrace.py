# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_flowtrace.ui'
#
# Created: Thu Feb 20 12:42:18 2014
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_flowTrace(object):
    def setupUi(self, flowTrace):
        flowTrace.setObjectName(_fromUtf8("flowTrace"))
        flowTrace.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(flowTrace)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(flowTrace)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), flowTrace.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), flowTrace.reject)
        QtCore.QMetaObject.connectSlotsByName(flowTrace)

    def retranslateUi(self, flowTrace):
        flowTrace.setWindowTitle(QtGui.QApplication.translate("flowTrace", "flowTrace", None, QtGui.QApplication.UnicodeUTF8))

