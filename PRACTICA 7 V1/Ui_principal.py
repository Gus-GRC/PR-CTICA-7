# Form implementation generated from reading ui file 'c:\Users\gusta\Downloads\P12\principal.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Messenger(object):
    def setupUi(self, Messenger):
        Messenger.setObjectName("Messenger")
        Messenger.resize(493, 414)
        self.centralwidget = QtWidgets.QWidget(parent=Messenger)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.txtMsgs = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.txtMsgs.setEnabled(True)
        self.txtMsgs.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.txtMsgs.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.txtMsgs.setReadOnly(True)
        self.txtMsgs.setObjectName("txtMsgs")
        self.gridLayout.addWidget(self.txtMsgs, 0, 0, 1, 2)
        self.txtSend = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtSend.setMaxLength(1023)
        self.txtSend.setObjectName("txtSend")
        self.gridLayout.addWidget(self.txtSend, 1, 0, 1, 1)
        self.btnSend = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnSend.setObjectName("btnSend")
        self.gridLayout.addWidget(self.btnSend, 1, 1, 1, 1)
        Messenger.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Messenger)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 493, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(parent=self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        Messenger.setMenuBar(self.menubar)
        self.actionConectar = QtGui.QAction(parent=Messenger)
        self.actionConectar.setObjectName("actionConectar")
        self.actionSalir = QtGui.QAction(parent=Messenger)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionConectar)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(Messenger)
        QtCore.QMetaObject.connectSlotsByName(Messenger)

    def retranslateUi(self, Messenger):
        _translate = QtCore.QCoreApplication.translate
        Messenger.setWindowTitle(_translate("Messenger", "Messenger"))
        self.btnSend.setText(_translate("Messenger", "Enviar"))
        self.menuArchivo.setTitle(_translate("Messenger", "&Archivo"))
        self.actionConectar.setText(_translate("Messenger", "Co&nectar"))
        self.actionConectar.setShortcut(_translate("Messenger", "Ctrl+C"))
        self.actionSalir.setText(_translate("Messenger", "&Salir"))
        self.actionSalir.setShortcut(_translate("Messenger", "Ctrl+X"))
