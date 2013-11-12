#GUI do przetwarzania regular expressions
#start: 12-11-2013
#koniec: 
#DK

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
		
	def makeRegExp(self):
		mess=str(self.ui.message.toPlainText()).split(' ')
		rexp=str(self.ui.regexp.toPlainText())
		try:
			self.rx=re.compile(rexp.decode('utf-8'), re.UNICODE)
		except sre_constants.error:
			print 'blad'
			#wstawic okienko bledu
		result=self.searchre(mess)
		
		self.ui.results.setText(result)
		print result

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	myapp = MainRE()
	myapp.show()
	sys.exit(app.exec_())
