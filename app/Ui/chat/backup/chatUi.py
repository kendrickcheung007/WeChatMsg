# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1280, 720)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setAutoFillBackground(False)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(580, 570, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(480, 50, 800, 520))
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(480, 600, 800, 120))
        self.textEdit.setObjectName("textEdit")
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(1240, 0, 47, 51))
        self.toolButton.setObjectName("toolButton")
        self.sendMsg = QtWidgets.QPushButton(Dialog)
        self.sendMsg.setGeometry(QtCore.QRect(1162, 670, 121, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.sendMsg.setFont(font)
        self.sendMsg.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sendMsg.setMouseTracking(False)
        self.sendMsg.setAutoFillBackground(False)
        self.sendMsg.setStyleSheet("QPushButton {\n"
"    background-color: #f0f0f0;\n"
"    \n"
"    padding: 10px;\n"
"    color:rgb(5,180,104);\n"
"}")
        self.sendMsg.setIconSize(QtCore.QSize(40, 40))
        self.sendMsg.setCheckable(False)
        self.sendMsg.setAutoDefault(True)
        self.sendMsg.setObjectName("sendMsg")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(480, 570, 800, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(480, 50, 800, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(480, 0, 3, 720))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalScrollBar = QtWidgets.QScrollBar(Dialog)
        self.verticalScrollBar.setGeometry(QtCore.QRect(460, 50, 16, 671))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(Dialog)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(1260, 50, 16, 520))
        self.verticalScrollBar_2.setStyleSheet("background-color: #f0f0f0;")
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 50, 300, 80))
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setText("")
        self.pushButton_2.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_2.setObjectName("pushButton_2")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 200, 318, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout1 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout1.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout1.setContentsMargins(10, 10, 10, 10)
        self.gridLayout1.setSpacing(10)
        self.gridLayout1.setObjectName("gridLayout1")
        self.label_time = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_time.setFont(font)
        self.label_time.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_time.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_time.setObjectName("label_time")
        self.gridLayout1.addWidget(self.label_time, 0, 2, 1, 1)
        self.label_remark = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_remark.setFont(font)
        self.label_remark.setObjectName("label_remark")
        self.gridLayout1.addWidget(self.label_remark, 0, 1, 1, 1)
        self.label_msg = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_msg.setFont(font)
        self.label_msg.setObjectName("label_msg")
        self.gridLayout1.addWidget(self.label_msg, 1, 1, 1, 2)
        self.label_avatar = QtWidgets.QLabel(self.layoutWidget)
        self.label_avatar.setMinimumSize(QtCore.QSize(60, 60))
        self.label_avatar.setMaximumSize(QtCore.QSize(60, 60))
        self.label_avatar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_avatar.setAutoFillBackground(False)
        self.label_avatar.setStyleSheet("background-color: #ffffff;")
        self.label_avatar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_avatar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_avatar.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_avatar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_avatar.setObjectName("label_avatar")
        self.gridLayout1.addWidget(self.label_avatar, 0, 0, 2, 1)
        self.gridLayout1.setColumnStretch(0, 1)
        self.gridLayout1.setColumnStretch(1, 6)
        self.gridLayout1.setRowStretch(0, 5)
        self.gridLayout1.setRowStretch(1, 3)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 160, 111, 402))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_msg = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_msg.setMinimumSize(QtCore.QSize(0, 80))
        self.btn_msg.setObjectName("btn_msg")
        self.verticalLayout_2.addWidget(self.btn_msg)
        self.btn_contact = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_contact.setMinimumSize(QtCore.QSize(0, 80))
        self.btn_contact.setObjectName("btn_contact")
        self.verticalLayout_2.addWidget(self.btn_contact)
        self.btn_addC = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_addC.setMinimumSize(QtCore.QSize(0, 80))
        self.btn_addC.setObjectName("btn_addC")
        self.verticalLayout_2.addWidget(self.btn_addC)
        self.btn_delC = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_delC.setMinimumSize(QtCore.QSize(0, 80))
        self.btn_delC.setObjectName("btn_delC")
        self.verticalLayout_2.addWidget(self.btn_delC)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(100, 80))
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)
        self.myavatar = QtWidgets.QLabel(Dialog)
        self.myavatar.setGeometry(QtCore.QRect(10, 30, 100, 100))
        self.myavatar.setObjectName("myavatar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.toolButton.setText(_translate("Dialog", "..."))
        self.sendMsg.setText(_translate("Dialog", "发送"))
        self.label_time.setText(_translate("Dialog", "22/12/17"))
        self.label_remark.setText(_translate("Dialog", "西北工业大学财务处"))
        self.label_msg.setText(_translate("Dialog", "我没去"))
        self.label_avatar.setText(_translate("Dialog", "TextLabel"))
        self.btn_msg.setText(_translate("Dialog", "聊天"))
        self.btn_contact.setText(_translate("Dialog", "联系人"))
        self.btn_addC.setText(_translate("Dialog", "添加联系人"))
        self.btn_delC.setText(_translate("Dialog", "删除联系人"))
        self.pushButton_6.setText(_translate("Dialog", "设置"))
        self.myavatar.setText(_translate("Dialog", "avatar"))