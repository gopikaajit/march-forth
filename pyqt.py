# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'w2.ui'
#
# Created: Fri Nov 17 07:08:46 2017
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!


#WINDOW 2

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
from w3 import Ui_w3
from w8 import Ui_Dialog
class Ui_w2(object):
    def openwindow(self):
	self.window=QtGui.QDialog()
	self.ui=Ui_w3()
	self.ui.setupUi(self.window)
	self.window.show()
    def op(self):
	self.wi=QtGui.QDialog()
	self.ui=Ui_Dialog()
	self.ui.setupUi(self.wi)
    	self.wi.show()
    def setupUi(self, w2):
        w2.setObjectName(_fromUtf8("w2"))
        w2.resize(800, 600)
        self.centralwidget = QtGui.QWidget(w2)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 170, 111, 20))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.reservation = QtGui.QPushButton(self.centralwidget)
        self.reservation.setGeometry(QtCore.QRect(280, 150, 241, 28))
        self.reservation.setObjectName(_fromUtf8("reservation"))

	self.reservation.clicked.connect(self.openwindow)

        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 210, 241, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
	
	self.pushButton_2.clicked.connect(self.op)

        #self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        #self.pushButton_3.setGeometry(QtCore.QRect(280, 260, 241, 28))
        #self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        #self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        #self.pushButton_4.setGeometry(QtCore.QRect(280, 310, 241, 28))
        #self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        #self.logout = QtGui.QPushButton(self.centralwidget)
        #self.logout.setGeometry(QtCore.QRect(280, 360, 90, 28))
        #self.logout.setObjectName(_fromUtf8("logout"))
        #self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        #self.pushButton_6.setGeometry(QtCore.QRect(430, 360, 90, 28))
        #self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        w2.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(w2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuTRAIN_RESERVATION_SYSTEM = QtGui.QMenu(self.menubar)
        self.menuTRAIN_RESERVATION_SYSTEM.setObjectName(_fromUtf8("menuTRAIN_RESERVATION_SYSTEM"))
        w2.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(w2)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        w2.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuTRAIN_RESERVATION_SYSTEM.menuAction())

        self.retranslateUi(w2)
        QtCore.QMetaObject.connectSlotsByName(w2)

    def retranslateUi(self, w2):
        w2.setWindowTitle(QtGui.QApplication.translate("w2", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.reservation.setText(QtGui.QApplication.translate("w2", "Make a reservation", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("w2", "Show ticket status", None, QtGui.QApplication.UnicodeUTF8))
        #self.pushButton_3.setText(QtGui.QApplication.translate("w2", "Show train details", None, QtGui.QApplication.UnicodeUTF8))
        #self.pushButton_4.setText(QtGui.QApplication.translate("w2", "Reservation chart", None, QtGui.QApplication.UnicodeUTF8))
        #self.logout.setText(QtGui.QApplication.translate("w2", "LOGOUT", None, QtGui.QApplication.UnicodeUTF8))
        #self.pushButton_6.setText(QtGui.QApplication.translate("w2", "EXIT", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTRAIN_RESERVATION_SYSTEM.setTitle(QtGui.QApplication.translate("w2", "TRAIN RESERVATION SYSTEM", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    w2 = QtGui.QMainWindow()
    ui = Ui_w2()
    ui.setupUi(w2)
    w2.show()
    sys.exit(app.exec_())



#WINDOW 3


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'w3.ui'
#
# Created: Sun Nov 19 09:04:39 2017
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import cx_Oracle

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_w3(object):
    def take_input(self):
	con = cx_Oracle.connect('oracle/oracle@localhost/xe')
	cur = con.cursor()
  	nam=self.tname.text()
	f=self.fro.text()
	too=self.to.text()
	pnam=self.pname.text()
	ad=self.adults.text()
	a=int(ad)
	b=a*40
	cmd="INSERT INTO train (tname,fr,t,pname,adult,tfare) VALUES ('%s','%s','%s','%s','%s','%s')" % (nam,f,too,pnam,ad,b)	
	cur.execute(cmd)
	cur.execute("commit")
	cur.close()
	con.close()    
    def setupUi(self, w3):
        w3.setObjectName(_fromUtf8("w3"))
        w3.resize(407, 365)
        self.label = QtGui.QLabel(w3)
        self.label.setGeometry(QtCore.QRect(50, 40, 241, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(w3)
        self.line.setGeometry(QtCore.QRect(510, 50, 20, 241))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_3 = QtGui.QFrame(w3)
        self.line_3.setGeometry(QtCore.QRect(160, 40, 361, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(w3)
        self.line_4.setGeometry(QtCore.QRect(10, 40, 31, 16))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.line_5 = QtGui.QFrame(w3)
        self.line_5.setGeometry(QtCore.QRect(0, 50, 20, 241))
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.label_4 = QtGui.QLabel(w3)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 91, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tname = QtGui.QLineEdit(w3)
        self.tname.setGeometry(QtCore.QRect(170, 120, 181, 21))
        self.tname.setObjectName(_fromUtf8("tname"))
        self.line_9 = QtGui.QFrame(w3)
        self.line_9.setGeometry(QtCore.QRect(10, 290, 511, 16))
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.pushButton = QtGui.QPushButton(w3)
        self.pushButton.setGeometry(QtCore.QRect(140, 310, 101, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

	self.pushButton.clicked.connect(self.take_input)

        self.label_6 = QtGui.QLabel(w3)
        self.label_6.setGeometry(QtCore.QRect(20, 150, 71, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(w3)
        self.label_7.setGeometry(QtCore.QRect(20, 180, 71, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.to = QtGui.QLineEdit(w3)
        self.to.setGeometry(QtCore.QRect(170, 180, 181, 21))
        self.to.setObjectName(_fromUtf8("to"))
        self.fro = QtGui.QLineEdit(w3)
        self.fro.setGeometry(QtCore.QRect(170, 150, 181, 21))
        self.fro.setObjectName(_fromUtf8("fro"))
        self.label_9 = QtGui.QLabel(w3)
        self.label_9.setGeometry(QtCore.QRect(20, 240, 131, 20))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(w3)
        self.label_10.setGeometry(QtCore.QRect(20, 210, 131, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.pname = QtGui.QLineEdit(w3)
        self.pname.setGeometry(QtCore.QRect(170, 210, 181, 21))
        self.pname.setObjectName(_fromUtf8("pname"))
        self.adults = QtGui.QLineEdit(w3)
        self.adults.setGeometry(QtCore.QRect(170, 240, 181, 21))
        self.adults.setObjectName(_fromUtf8("adults"))

        self.retranslateUi(w3)
        QtCore.QMetaObject.connectSlotsByName(w3)

    def retranslateUi(self, w3):
        w3.setWindowTitle(QtGui.QApplication.translate("w3", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("w3", "TRAIN DETAILS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("w3", "TRAIN NAME:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("w3", "BOOK TICKET", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("w3", " FROM:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("w3", "TO:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("w3", "TOTAL ADULT NO:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("w3", "PASSENGER NAME:", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    w3 = QtGui.QDialog()
    ui = Ui_w3()
    ui.setupUi(w3)
    w3.show()
    sys.exit(app.exec_())


#WINDOW 8


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'w8.ui'
#
# Created: Sun Nov 19 08:48:16 2017
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import cx_Oracle
#connection=cx_Oracle.connect(oracle/oracle/xe)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def loaddata(self):
	con = cx_Oracle.connect('oracle/oracle@localhost/xe')
	cur = con.cursor()
	cur.execute('SELECT * FROM TRAIN')
	results=cur.fetchall()

	for row in range(0,len(results)):
		self.tableWidget.insertRow(row)
		record=results[row]
		for column in range (0,len(record)):
			newitem=QtGui.QTableWidgetItem(str(record[column]))
			self.tableWidget.setItem(row,column,newitem)

	cur.close()
	con.close()         
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(672, 428)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(280, 10, 201, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 30, 91, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(550, 30, 91, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(20, 51, 641, 331))
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(350, 30, 91, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(150, 30, 91, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(250, 30, 91, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.btn_load = QtGui.QPushButton(Dialog)
        self.btn_load.setGeometry(QtCore.QRect(280, 390, 90, 28))
        self.btn_load.setObjectName(_fromUtf8("btn_load"))

	self.btn_load.clicked.connect(self.loaddata)

        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(450, 30, 91, 20))
        self.label_9.setObjectName(_fromUtf8("label_9"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "TICKET STATUS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "TRAIN NAME", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "TOTAL FARE", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "P_NAME", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "FROM", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "TO", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_load.setText(QtGui.QApplication.translate("Dialog", "SHOW", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "ADULT", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


