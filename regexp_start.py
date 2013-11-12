#GUI do przetwarzania regular expressions
#start: 12-11-2013
#koniec: 
#DK

#TO DO: podzial na linijki!!!

import sys
import re
from PyQt4 import QtCore, QtGui

from reui import Ui_RegExper

class MainRE(QtGui.QMainWindow):
	
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui=Ui_RegExper()
		self.ui.setupUi(self)
		QtCore.QObject.connect(self.ui.wykonaj,QtCore.SIGNAL("clicked()"), self.makeRegExp)
	
	def searchre(self,word_lst):
		finded=''
		for w in word_lst:
			if self.rx.search(w):
				print w
				finded+=(w+' ')
		return finded
	
	def cutText(self,txt):
		cutted=list()
		m=txt.split('\n')
		for i in m:
			for j in i.split(' '):
				cutted.append(j)
		return cutted

	def makeRegExp(self):
		mess=self.cutText(str(self.ui.message.toPlainText()).decode('utf-8'))
		rexp=str(self.ui.regexp.toPlainText())
		print mess
		try:
			self.rx=re.compile(rexp.decode('utf-8'), re.UNICODE)
			result=self.searchre(mess)	
			self.ui.results.setText(result)

		except Exception:
			QtGui.QMessageBox(QtGui.QMessageBox.Warning,
                "Error", "Wrong sign in regular expression.\n Change it and try again!",
                QtGui.QMessageBox.NoButton, self).show()

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	myapp = MainRE()
	myapp.show()
	sys.exit(app.exec_())
