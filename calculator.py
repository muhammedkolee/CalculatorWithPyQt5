# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(1080, 721)
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(290, 60, 481, 501))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 90, 481, 409))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.plus_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plus_button.sizePolicy().hasHeightForWidth())
        self.plus_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.plus_button.setFont(font)
        self.plus_button.setObjectName("plus_button")
        self.gridLayout.addWidget(self.plus_button, 3, 3, 1, 1)
        self.two_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.two_button.sizePolicy().hasHeightForWidth())
        self.two_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.two_button.setFont(font)
        self.two_button.setObjectName("two_button")
        self.gridLayout.addWidget(self.two_button, 3, 1, 1, 1)
        self.toggle_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggle_button.sizePolicy().hasHeightForWidth())
        self.toggle_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.toggle_button.setFont(font)
        self.toggle_button.setObjectName("toggle_button")
        self.gridLayout.addWidget(self.toggle_button, 4, 0, 1, 1)
        self.four_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.four_button.sizePolicy().hasHeightForWidth())
        self.four_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.four_button.setFont(font)
        self.four_button.setObjectName("four_button")
        self.gridLayout.addWidget(self.four_button, 2, 0, 1, 1)
        self.minus_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minus_button.sizePolicy().hasHeightForWidth())
        self.minus_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.minus_button.setFont(font)
        self.minus_button.setObjectName("minus_button")
        self.gridLayout.addWidget(self.minus_button, 2, 3, 1, 1)
        self.nine_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nine_button.sizePolicy().hasHeightForWidth())
        self.nine_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.nine_button.setFont(font)
        self.nine_button.setObjectName("nine_button")
        self.gridLayout.addWidget(self.nine_button, 1, 2, 1, 1)
        self.three_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.three_button.sizePolicy().hasHeightForWidth())
        self.three_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.three_button.setFont(font)
        self.three_button.setObjectName("three_button")
        self.gridLayout.addWidget(self.three_button, 3, 2, 1, 1)
        self.six_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.six_button.sizePolicy().hasHeightForWidth())
        self.six_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.six_button.setFont(font)
        self.six_button.setObjectName("six_button")
        self.gridLayout.addWidget(self.six_button, 2, 2, 1, 1)
        self.five_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.five_button.sizePolicy().hasHeightForWidth())
        self.five_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.five_button.setFont(font)
        self.five_button.setObjectName("five_button")
        self.gridLayout.addWidget(self.five_button, 2, 1, 1, 1)
        self.zero_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zero_button.sizePolicy().hasHeightForWidth())
        self.zero_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.zero_button.setFont(font)
        self.zero_button.setObjectName("zero_button")
        self.gridLayout.addWidget(self.zero_button, 4, 1, 1, 1)
        self.times_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.times_button.sizePolicy().hasHeightForWidth())
        self.times_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.times_button.setFont(font)
        self.times_button.setObjectName("times_button")
        self.gridLayout.addWidget(self.times_button, 1, 3, 1, 1)
        self.eight_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eight_button.sizePolicy().hasHeightForWidth())
        self.eight_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.eight_button.setFont(font)
        self.eight_button.setObjectName("eight_button")
        self.gridLayout.addWidget(self.eight_button, 1, 1, 1, 1)
        self.seven_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seven_button.sizePolicy().hasHeightForWidth())
        self.seven_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.seven_button.setFont(font)
        self.seven_button.setObjectName("seven_button")
        self.gridLayout.addWidget(self.seven_button, 1, 0, 1, 1)
        self.one_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.one_button.sizePolicy().hasHeightForWidth())
        self.one_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.one_button.setFont(font)
        self.one_button.setObjectName("one_button")
        self.gridLayout.addWidget(self.one_button, 3, 0, 1, 1)
        self.point_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.point_button.sizePolicy().hasHeightForWidth())
        self.point_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.point_button.setFont(font)
        self.point_button.setObjectName("point_button")
        self.gridLayout.addWidget(self.point_button, 4, 2, 1, 1)
        self.clear_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_button.sizePolicy().hasHeightForWidth())
        self.clear_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        self.clear_button.setFont(font)
        self.clear_button.setObjectName("clear_button")
        self.gridLayout.addWidget(self.clear_button, 0, 0, 1, 1)
        self.equal_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equal_button.sizePolicy().hasHeightForWidth())
        self.equal_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        self.equal_button.setFont(font)
        self.equal_button.setObjectName("equal_button")
        self.gridLayout.addWidget(self.equal_button, 4, 3, 1, 1)
        self.percent_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.percent_button.sizePolicy().hasHeightForWidth())
        self.percent_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.percent_button.setFont(font)
        self.percent_button.setObjectName("percent_button")
        self.gridLayout.addWidget(self.percent_button, 0, 1, 1, 1)
        self.divide_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.divide_button.sizePolicy().hasHeightForWidth())
        self.divide_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.divide_button.setFont(font)
        self.divide_button.setObjectName("divide_button")
        self.gridLayout.addWidget(self.divide_button, 0, 2, 1, 1)
        self.backspace_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backspace_button.sizePolicy().hasHeightForWidth())
        self.backspace_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.backspace_button.setFont(font)
        self.backspace_button.setObjectName("backspace_button")
        self.gridLayout.addWidget(self.backspace_button, 0, 3, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, -1, 481, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.result_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.result_label.sizePolicy().hasHeightForWidth())
        self.result_label.setSizePolicy(sizePolicy)
        self.result_label.setLineWidth(1)
        self.result_label.setText("")
        self.result_label.setObjectName("result_label")
        self.horizontalLayout.addWidget(self.result_label)
        self.horizontalLayout.setStretch(0, 3)
        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 26))
        self.menubar.setObjectName("menubar")
        Calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "MainWindow"))
        self.plus_button.setText(_translate("Calculator", "+"))
        self.two_button.setText(_translate("Calculator", "2"))
        self.toggle_button.setText(_translate("Calculator", "+/-"))
        self.four_button.setText(_translate("Calculator", "4"))
        self.minus_button.setText(_translate("Calculator", "-"))
        self.nine_button.setText(_translate("Calculator", "9"))
        self.three_button.setText(_translate("Calculator", "3"))
        self.six_button.setText(_translate("Calculator", "6"))
        self.five_button.setText(_translate("Calculator", "5"))
        self.zero_button.setText(_translate("Calculator", "0"))
        self.times_button.setText(_translate("Calculator", "✖"))
        self.eight_button.setText(_translate("Calculator", "8"))
        self.seven_button.setText(_translate("Calculator", "7"))
        self.one_button.setText(_translate("Calculator", "1"))
        self.point_button.setText(_translate("Calculator", "."))
        self.clear_button.setText(_translate("Calculator", "C"))
        self.equal_button.setText(_translate("Calculator", "="))
        self.percent_button.setText(_translate("Calculator", "%"))
        self.divide_button.setText(_translate("Calculator", "/"))
        self.backspace_button.setText(_translate("Calculator", "⬅"))
