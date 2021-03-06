# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(427, 677)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(427, 677))
        MainWindow.setMaximumSize(QtCore.QSize(427, 677))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("background-color: #1F1F2B;")
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 10, 411, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAutoFillBackground(False)
        self.title.setStyleSheet("color: white;")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.list_operation = QtWidgets.QListWidget(self.centralwidget)
        self.list_operation.setGeometry(QtCore.QRect(60, 100, 211, 161))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.list_operation.setFont(font)
        self.list_operation.setStyleSheet("QListWidget::item{\n"
"color: white;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"background-color: #27DBB4;\n"
"}")
        self.list_operation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.list_operation.setDragEnabled(False)
        self.list_operation.setViewMode(QtWidgets.QListView.ListMode)
        self.list_operation.setModelColumn(0)
        self.list_operation.setObjectName("list_operation")
        item = QtWidgets.QListWidgetItem()
        self.list_operation.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_operation.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_operation.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_operation.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_operation.addItem(item)
        self.subscribe_on = QtWidgets.QCheckBox(self.centralwidget)
        self.subscribe_on.setGeometry(QtCore.QRect(20, 550, 351, 31))
        self.subscribe_on.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.subscribe_on.setStyleSheet("\n"
"\n"
"color: white;\n"
"")
        self.subscribe_on.setChecked(True)
        self.subscribe_on.setObjectName("subscribe_on")
        self.list_device = QtWidgets.QListWidget(self.centralwidget)
        self.list_device.setGeometry(QtCore.QRect(290, 100, 81, 101))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.list_device.setFont(font)
        self.list_device.setStyleSheet("QListWidget::item{\n"
"color: white;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"background-color: #27DBB4;\n"
"}")
        self.list_device.setObjectName("list_device")
        item = QtWidgets.QListWidgetItem()
        self.list_device.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_device.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_device.addItem(item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-80, 340, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 450, 221, 31))
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 410, 221, 31))
        self.label_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 490, 221, 31))
        self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.pause_time = QtWidgets.QLineEdit(self.centralwidget)
        self.pause_time.setGeometry(QtCore.QRect(290, 490, 61, 31))
        self.pause_time.setStyleSheet("color: white;")
        self.pause_time.setAlignment(QtCore.Qt.AlignCenter)
        self.pause_time.setObjectName("pause_time")
        self.likes_on = QtWidgets.QCheckBox(self.centralwidget)
        self.likes_on.setGeometry(QtCore.QRect(20, 580, 351, 31))
        self.likes_on.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.likes_on.setStyleSheet("color: white;")
        self.likes_on.setChecked(True)
        self.likes_on.setObjectName("likes_on")
        self.comments_on = QtWidgets.QCheckBox(self.centralwidget)
        self.comments_on.setGeometry(QtCore.QRect(20, 610, 401, 31))
        self.comments_on.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comments_on.setStyleSheet("color: white;")
        self.comments_on.setChecked(True)
        self.comments_on.setObjectName("comments_on")
        self.button_start = QtWidgets.QPushButton(self.centralwidget)
        self.button_start.setGeometry(QtCore.QRect(290, 220, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.button_start.setFont(font)
        self.button_start.setAutoFillBackground(False)
        self.button_start.setStyleSheet("color: white; background: #2A2F3A;")
        self.button_start.setObjectName("button_start")
        self.post_num = QtWidgets.QLineEdit(self.centralwidget)
        self.post_num.setGeometry(QtCore.QRect(290, 450, 61, 31))
        self.post_num.setStyleSheet("color: white;")
        self.post_num.setAlignment(QtCore.Qt.AlignCenter)
        self.post_num.setObjectName("post_num")
        self.max_users = QtWidgets.QLineEdit(self.centralwidget)
        self.max_users.setGeometry(QtCore.QRect(290, 410, 61, 31))
        self.max_users.setStyleSheet("color: white;")
        self.max_users.setAlignment(QtCore.Qt.AlignCenter)
        self.max_users.setPlaceholderText("")
        self.max_users.setObjectName("max_users")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 280, 61, 31))
        self.label_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_5.setStyleSheet("color: white;")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(150, 280, 221, 31))
        self.username.setStyleSheet("color: white;")
        self.username.setText("")
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.setObjectName("username")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 320, 61, 31))
        self.label_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_6.setStyleSheet("color: white;")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(150, 320, 221, 31))
        self.password.setStyleSheet("color: white;")
        self.password.setInputMask("")
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(130, 650, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:#666;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.list_operation.setCurrentRow(2)
        self.list_device.setCurrentRow(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Instagram bot"))
        self.title.setText(_translate("MainWindow", "Instagram bot"))
        __sortingEnabled = self.list_operation.isSortingEnabled()
        self.list_operation.setSortingEnabled(False)
        item = self.list_operation.item(0)
        item.setText(_translate("MainWindow", "?????????????? ??????????????????????"))
        item = self.list_operation.item(1)
        item.setText(_translate("MainWindow", "?????????????? ????????????????"))
        item = self.list_operation.item(2)
        item.setText(_translate("MainWindow", "???????????????? ?? ??????????"))
        item = self.list_operation.item(3)
        item.setText(_translate("MainWindow", "??????????????"))
        item = self.list_operation.item(4)
        item.setText(_translate("MainWindow", "???????????????? ????????????????????????"))
        self.list_operation.setSortingEnabled(__sortingEnabled)
        self.subscribe_on.setText(_translate("MainWindow", "?????????????????????????? ???? ??????????????, ?????????? ??????????????"))
        __sortingEnabled = self.list_device.isSortingEnabled()
        self.list_device.setSortingEnabled(False)
        item = self.list_device.item(0)
        item.setText(_translate("MainWindow", "iPhone"))
        item = self.list_device.item(1)
        item.setText(_translate("MainWindow", "Galaxy"))
        item = self.list_device.item(2)
        item.setText(_translate("MainWindow", "Pixel"))
        self.list_device.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"))
        self.label_2.setText(_translate("MainWindow", "???????????????????? ????????????:"))
        self.label_3.setText(_translate("MainWindow", "????????. ?????????? ??????????????????????????:"))
        self.label_4.setText(_translate("MainWindow", "?????????? ?? ????????????????:"))
        self.pause_time.setText(_translate("MainWindow", "18"))
        self.likes_on.setText(_translate("MainWindow", "???????????????? ?????????? ???????????????? ??????????????????????????"))
        self.comments_on.setText(_translate("MainWindow", "???????????????? ?????????????????????? ???????????????? ??????????????????????????"))
        self.button_start.setText(_translate("MainWindow", "??????????"))
        self.post_num.setText(_translate("MainWindow", "2"))
        self.max_users.setText(_translate("MainWindow", "1000"))
        self.label_5.setText(_translate("MainWindow", "??????????:"))
        self.username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.label_6.setText(_translate("MainWindow", "????????????:"))
        self.password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.label_7.setText(_translate("MainWindow", "Telegram: @Dori_12"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
