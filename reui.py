# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regexpgui.ui'
#
# Created: Tue Nov 12 18:13:11 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_RegExper(object):
    def setupUi(self, RegExper):
        RegExper.setObjectName(_fromUtf8("RegExper"))
        RegExper.resize(581, 302)
        self.centralwidget = QtGui.QWidget(RegExper)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.regexp = QtGui.QTextEdit(self.centralwidget)
        self.regexp.setGeometry(QtCore.QRect(10, 180, 281, 41))
        self.regexp.setObjectName(_fromUtf8("regexp"))
        self.wykonaj = QtGui.QPushButton(self.centralwidget)
        self.wykonaj.setGeometry(QtCore.QRect(220, 230, 75, 23))
        self.wykonaj.setObjectName(_fromUtf8("wykonaj"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 160, 121, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.message = QtGui.QTextEdit(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(10, 20, 281, 131))
        self.message.setObjectName(_fromUtf8("message"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 121, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.results = QtGui.QTextEdit(self.centralwidget)
        self.results.setGeometry(QtCore.QRect(310, 20, 251, 241))
        self.results.setObjectName(_fromUtf8("results"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 0, 121, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        RegExper.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(RegExper)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 581, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        RegExper.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(RegExper)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        RegExper.setStatusBar(self.statusbar)

        self.retranslateUi(RegExper)
        QtCore.QMetaObject.connectSlotsByName(RegExper)

    def retranslateUi(self, RegExper):
        RegExper.setWindowTitle(_translate("RegExper", "REG EXPER v0.01", None))
        self.wykonaj.setText(_translate("RegExper", "Do it!", None))
        self.label.setText(_translate("RegExper", "Your Regular Expresion", None))
        self.label_2.setText(_translate("RegExper", "Your text", None))
        self.label_3.setText(_translate("RegExper", "Matches", None))

