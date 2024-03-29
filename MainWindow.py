# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1058, 660)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("app.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1051, 631))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(10, 50, 47, 13))
        self.label_11.setObjectName("label_11")
        self.fromEdit = QtWidgets.QLineEdit(self.tab)
        self.fromEdit.setGeometry(QtCore.QRect(60, 50, 131, 20))
        self.fromEdit.setObjectName("fromEdit")
        self.randButton = QtWidgets.QPushButton(self.tab)
        self.randButton.setGeometry(QtCore.QRect(200, 50, 75, 23))
        self.randButton.setObjectName("randButton")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(10, 90, 61, 16))
        self.label_12.setObjectName("label_12")
        self.distEdit = QtWidgets.QLineEdit(self.tab)
        self.distEdit.setGeometry(QtCore.QRect(80, 90, 113, 20))
        self.distEdit.setObjectName("distEdit")
        self.findFlyButton = QtWidgets.QPushButton(self.tab)
        self.findFlyButton.setGeometry(QtCore.QRect(0, 120, 75, 23))
        self.findFlyButton.setObjectName("findFlyButton")
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(20, 160, 321, 401))
        self.listWidget.setObjectName("listWidget")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label_13.setObjectName("label_13")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(60, 10, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.map_widget = QtWidgets.QWidget(self.tab)
        self.map_widget.setGeometry(QtCore.QRect(380, 20, 661, 571))
        self.map_widget.setObjectName("map_widget")
        self.mapButton = QtWidgets.QPushButton(self.tab)
        self.mapButton.setGeometry(QtCore.QRect(280, 50, 75, 23))
        self.mapButton.setObjectName("mapButton")
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(210, 10, 61, 16))
        self.label_16.setObjectName("label_16")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(740, 570, 161, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboMaxSize = QtWidgets.QComboBox(self.tab)
        self.comboMaxSize.setGeometry(QtCore.QRect(270, 10, 100, 22))
        self.comboMaxSize.setObjectName("comboMaxSize")
        self.copyToComButton = QtWidgets.QPushButton(self.tab)
        self.copyToComButton.setGeometry(QtCore.QRect(20, 570, 141, 23))
        self.copyToComButton.setObjectName("copyToComButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.icaoEdit = QtWidgets.QLineEdit(self.tab_2)
        self.icaoEdit.setGeometry(QtCore.QRect(50, 10, 113, 20))
        self.icaoEdit.setObjectName("icaoEdit")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(20, 10, 47, 13))
        self.label.setObjectName("label")
        self.nameEdit = QtWidgets.QLineEdit(self.tab_2)
        self.nameEdit.setGeometry(QtCore.QRect(60, 50, 113, 20))
        self.nameEdit.setObjectName("nameEdit")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 47, 13))
        self.label_2.setObjectName("label_2")
        self.cityEdit = QtWidgets.QLineEdit(self.tab_2)
        self.cityEdit.setGeometry(QtCore.QRect(250, 50, 113, 20))
        self.cityEdit.setObjectName("cityEdit")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(180, 50, 47, 13))
        self.label_3.setObjectName("label_3")
        self.countryEdit = QtWidgets.QLineEdit(self.tab_2)
        self.countryEdit.setGeometry(QtCore.QRect(60, 90, 113, 20))
        self.countryEdit.setObjectName("countryEdit")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 47, 13))
        self.label_4.setObjectName("label_4")
        self.code_countryEdit = QtWidgets.QLineEdit(self.tab_2)
        self.code_countryEdit.setGeometry(QtCore.QRect(250, 90, 113, 20))
        self.code_countryEdit.setObjectName("code_countryEdit")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(180, 90, 61, 16))
        self.label_5.setObjectName("label_5")
        self.latEdit = QtWidgets.QLineEdit(self.tab_2)
        self.latEdit.setGeometry(QtCore.QRect(60, 130, 113, 20))
        self.latEdit.setObjectName("latEdit")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(10, 130, 47, 13))
        self.label_6.setObjectName("label_6")
        self.longEdit = QtWidgets.QLineEdit(self.tab_2)
        self.longEdit.setGeometry(QtCore.QRect(250, 130, 113, 20))
        self.longEdit.setObjectName("longEdit")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(180, 130, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(180, 180, 71, 16))
        self.label_8.setObjectName("label_8")
        self.runwayEdit = QtWidgets.QLineEdit(self.tab_2)
        self.runwayEdit.setGeometry(QtCore.QRect(60, 180, 113, 20))
        self.runwayEdit.setObjectName("runwayEdit")
        self.evevEdit = QtWidgets.QLineEdit(self.tab_2)
        self.evevEdit.setGeometry(QtCore.QRect(250, 180, 113, 20))
        self.evevEdit.setObjectName("evevEdit")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(10, 180, 47, 13))
        self.label_9.setObjectName("label_9")
        self.findButton = QtWidgets.QPushButton(self.tab_2)
        self.findButton.setGeometry(QtCore.QRect(170, 10, 61, 23))
        self.findButton.setObjectName("findButton")
        self.addButton = QtWidgets.QPushButton(self.tab_2)
        self.addButton.setGeometry(QtCore.QRect(10, 230, 141, 23))
        self.addButton.setObjectName("addButton")
        self.tableMyPorts = QtWidgets.QTableWidget(self.tab_2)
        self.tableMyPorts.setGeometry(QtCore.QRect(370, 10, 671, 521))
        self.tableMyPorts.setObjectName("tableMyPorts")
        self.tableMyPorts.setColumnCount(10)
        self.tableMyPorts.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableMyPorts.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableMyPorts.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableMyPorts.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableMyPorts.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableMyPorts.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableMyPorts.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableMyPorts.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableMyPorts.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableMyPorts.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableMyPorts.setHorizontalHeaderItem(9, item)
        self.tableMyPorts.horizontalHeader().setStretchLastSection(True)
        self.findButtonApinfo = QtWidgets.QPushButton(self.tab_2)
        self.findButtonApinfo.setGeometry(QtCore.QRect(230, 10, 61, 23))
        self.findButtonApinfo.setObjectName("findButtonApinfo")
        self.showAllButton = QtWidgets.QPushButton(self.tab_2)
        self.showAllButton.setGeometry(QtCore.QRect(930, 540, 91, 23))
        self.showAllButton.setObjectName("showAllButton")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(10, 280, 201, 16))
        self.label_10.setObjectName("label_10")
        self.coordEdit = QtWidgets.QLineEdit(self.tab_2)
        self.coordEdit.setGeometry(QtCore.QRect(0, 320, 251, 20))
        self.coordEdit.setObjectName("coordEdit")
        self.coordButton = QtWidgets.QPushButton(self.tab_2)
        self.coordButton.setGeometry(QtCore.QRect(0, 350, 75, 23))
        self.coordButton.setObjectName("coordButton")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(230, 210, 120, 80))
        self.groupBox.setObjectName("groupBox")
        self.radioButtonM = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonM.setGeometry(QtCore.QRect(20, 20, 82, 17))
        self.radioButtonM.setChecked(True)
        self.radioButtonM.setObjectName("radioButtonM")
        self.radioButtonF = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonF.setGeometry(QtCore.QRect(20, 40, 82, 17))
        self.radioButtonF.setObjectName("radioButtonF")
        self.delButton = QtWidgets.QPushButton(self.tab_2)
        self.delButton.setGeometry(QtCore.QRect(360, 540, 75, 23))
        self.delButton.setObjectName("delButton")
        self.writeButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.writeButton_2.setGeometry(QtCore.QRect(440, 540, 75, 23))
        self.writeButton_2.setObjectName("writeButton_2")
        self.findButtonSky = QtWidgets.QPushButton(self.tab_2)
        self.findButtonSky.setGeometry(QtCore.QRect(290, 10, 71, 23))
        self.findButtonSky.setObjectName("findButtonSky")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tablePath = QtWidgets.QTableWidget(self.tab_3)
        self.tablePath.setGeometry(QtCore.QRect(10, 30, 621, 161))
        self.tablePath.setMinimumSize(QtCore.QSize(621, 0))
        self.tablePath.setMaximumSize(QtCore.QSize(621, 16777215))
        self.tablePath.setObjectName("tablePath")
        self.tablePath.setColumnCount(1)
        self.tablePath.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablePath.setHorizontalHeaderItem(0, item)
        self.tablePath.horizontalHeader().setCascadingSectionResizes(False)
        self.tablePath.horizontalHeader().setStretchLastSection(True)
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setGeometry(QtCore.QRect(20, 10, 91, 16))
        self.label_14.setObjectName("label_14")
        self.pushAddPath = QtWidgets.QPushButton(self.tab_3)
        self.pushAddPath.setGeometry(QtCore.QRect(640, 30, 75, 23))
        self.pushAddPath.setObjectName("pushAddPath")
        self.pushDelPatch = QtWidgets.QPushButton(self.tab_3)
        self.pushDelPatch.setGeometry(QtCore.QRect(640, 60, 75, 23))
        self.pushDelPatch.setObjectName("pushDelPatch")
        self.pushFindNullPorts = QtWidgets.QPushButton(self.tab_3)
        self.pushFindNullPorts.setGeometry(QtCore.QRect(10, 200, 201, 23))
        self.pushFindNullPorts.setObjectName("pushFindNullPorts")
        self.tableLostPac = QtWidgets.QTableWidget(self.tab_3)
        self.tableLostPac.setGeometry(QtCore.QRect(10, 240, 621, 301))
        self.tableLostPac.setObjectName("tableLostPac")
        self.tableLostPac.setColumnCount(2)
        self.tableLostPac.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableLostPac.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLostPac.setHorizontalHeaderItem(1, item)
        self.tableLostPac.horizontalHeader().setCascadingSectionResizes(True)
        self.tableLostPac.horizontalHeader().setStretchLastSection(True)
        self.findDubleButton = QtWidgets.QPushButton(self.tab_3)
        self.findDubleButton.setGeometry(QtCore.QRect(730, 30, 75, 23))
        self.findDubleButton.setObjectName("findDubleButton")
        self.tableDouble = QtWidgets.QTableWidget(self.tab_3)
        self.tableDouble.setGeometry(QtCore.QRect(730, 90, 301, 451))
        self.tableDouble.setObjectName("tableDouble")
        self.tableDouble.setColumnCount(3)
        self.tableDouble.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableDouble.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDouble.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDouble.setHorizontalHeaderItem(2, item)
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(730, 70, 111, 16))
        self.label_15.setObjectName("label_15")
        self.line = QtWidgets.QFrame(self.tab_3)
        self.line.setGeometry(QtCore.QRect(710, 30, 20, 511))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushDelDub = QtWidgets.QPushButton(self.tab_3)
        self.pushDelDub.setGeometry(QtCore.QRect(950, 550, 75, 23))
        self.pushDelDub.setObjectName("pushDelDub")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1058, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Find the aero path"))
        self.label_11.setText(_translate("MainWindow", "From"))
        self.randButton.setText(_translate("MainWindow", "Random"))
        self.label_12.setText(_translate("MainWindow", "Max dist, nm"))
        self.distEdit.setText(_translate("MainWindow", "100"))
        self.findFlyButton.setText(_translate("MainWindow", "Find"))
        self.label_13.setText(_translate("MainWindow", "Aircrafts"))
        self.mapButton.setText(_translate("MainWindow", "Show map"))
        self.label_16.setText(_translate("MainWindow", "Max.size ft."))
        self.copyToComButton.setText(_translate("MainWindow", "Copy to community"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Find route"))
        self.label.setText(_translate("MainWindow", "ICAO"))
        self.label_2.setText(_translate("MainWindow", "Название"))
        self.label_3.setText(_translate("MainWindow", "Город"))
        self.label_4.setText(_translate("MainWindow", "Страна"))
        self.label_5.setText(_translate("MainWindow", "Код страны"))
        self.label_6.setText(_translate("MainWindow", "Широта"))
        self.label_7.setText(_translate("MainWindow", "Долгота"))
        self.label_8.setText(_translate("MainWindow", "Превышение"))
        self.label_9.setText(_translate("MainWindow", "Полоса"))
        self.findButton.setText(_translate("MainWindow", "🔍 в базе"))
        self.addButton.setText(_translate("MainWindow", "Добавить в мои порты"))
        item = self.tableMyPorts.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ICAO"))
        item = self.tableMyPorts.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Название"))
        item = self.tableMyPorts.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Город"))
        item = self.tableMyPorts.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Страна"))
        item = self.tableMyPorts.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Код стр."))
        item = self.tableMyPorts.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Полоса м."))
        item = self.tableMyPorts.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Широта"))
        item = self.tableMyPorts.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Долгота"))
        item = self.tableMyPorts.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Превышение"))
        item = self.tableMyPorts.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "ID"))
        self.findButtonApinfo.setText(_translate("MainWindow", "🔍 apinfo"))
        self.showAllButton.setText(_translate("MainWindow", "Показать все"))
        self.label_10.setText(_translate("MainWindow", "Пересчет координат"))
        self.coordButton.setText(_translate("MainWindow", "Пересчитать"))
        self.groupBox.setTitle(_translate("MainWindow", "Длина в "))
        self.radioButtonM.setText(_translate("MainWindow", "Метрах"))
        self.radioButtonF.setText(_translate("MainWindow", "Футах"))
        self.delButton.setText(_translate("MainWindow", "Удалить"))
        self.writeButton_2.setText(_translate("MainWindow", "Записать"))
        self.findButtonSky.setText(_translate("MainWindow", "🔍 skyvector"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Add aiport"))
        item = self.tablePath.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Path"))
        self.label_14.setText(_translate("MainWindow", "Пути к аддонам:"))
        self.pushAddPath.setText(_translate("MainWindow", "Добавить"))
        self.pushDelPatch.setText(_translate("MainWindow", "Удалить"))
        self.pushFindNullPorts.setText(_translate("MainWindow", "Проверить пропущенные порты"))
        item = self.tableLostPac.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ICAO"))
        item = self.tableLostPac.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Pacets"))
        self.findDubleButton.setText(_translate("MainWindow", "Найти дубли"))
        item = self.tableDouble.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableDouble.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "icao_code"))
        item = self.tableDouble.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "name_eng"))
        self.label_15.setText(_translate("MainWindow", "Найденные дубли:"))
        self.pushDelDub.setText(_translate("MainWindow", "Удалить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Utils"))
