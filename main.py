import math
import random
import sys  # sys нужен для передачи argv в QApplication

import dataset
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QApplication, QFileDialog
from loguru import logger

import MainWindow  # Это наш конвертированный файл дизайна
from utils.map import create_map
from utils.utils import data_from_skyvector, get_param_from_db, set_param_to_db, community_ikao

logger.add("error.log", level="ERROR", rotation="100 MB", format="{time} - {level} - {message}")


class Validator(QtGui.QValidator):

    def validate(self, string, pos):
        translate_to_eng = {
            'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p',
            'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k', 'д': 'l',
            'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n', 'ь': 'm',
        }

        def translate(ch):
            return translate_to_eng[ch] if ch in translate_to_eng else ch

        new_string = ''.join([translate(ch) for ch in string])

        return QtGui.QValidator.Acceptable, new_string.upper(), pos  # (state, string, index)


class IcaoApp(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.tabWidget.setCurrentIndex(0)
        self.db = dataset.connect('sqlite:///data/icao_base.db')
        self.findButton.clicked.connect(self.filter_my_ports)
        self.findButtonSky.clicked.connect(self.find_skyvector)
        self.pushAddPath.clicked.connect(self.add_patch)
        self.pushDelPatch.clicked.connect(self.rem_patch)
        self.pushFindNullPorts.clicked.connect(self.find_null_ports)
        self.findButtonApinfo.clicked.connect(self.find_appinfo)
        self.showAllButton.clicked.connect(self.fill_my_ports)
        self.addButton.clicked.connect(self.add_my_port)
        self.mapButton.clicked.connect(self.show_port_map)
        self.coordButton.clicked.connect(self.calc_coord)
        self.randButton.clicked.connect(self.find_rand_port)
        self.findFlyButton.clicked.connect(self.find_flights)
        self.delButton.clicked.connect(self.del_record)
        self.writeButton_2.clicked.connect(self.write_edit)
        self.ports = None
        self.port_depart = None
        self.len = 0
        self.fill_my_ports()
        self.set_aircrafts()
        self.metr_fut = 1  # 3.281
        self.radioButtonM.toggled.connect(self.setMeter)
        self.radioButtonF.toggled.connect(self.setFut)
        self.validator = Validator(self)
        self.icaoEdit.setValidator(self.validator)
        self.fromEdit.setValidator(self.validator)
        self.comboBox.activated[str].connect(self.combo_handler)
        #     add map view
        self.web = QWebView(self.tab)

        self.paths = []
        self.fill_path_find()
        self.crafts = None
        self.listWidget.currentItemChanged.connect(self.item_clicked)
        self.port_dist = None
        self.arr_legs = None
        self.size_map = 6
        self.init_map()

    def create_map(self):
        create_map(port_depart=self.port_depart, arr_legs=self.arr_legs, port_dest=self.port_dist, size=self.size_map)
        self.web.load(QUrl("file:///map.html"))
        self.web.show()

    def item_clicked(self, arg=None):
        if arg is not None:
            self.port_dist = [item for item in self.arr_legs if item["icao_code"] == arg.text()[0:4]][0]
            self.create_map()

    def find_null_ports(self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        ports = community_ikao(self.db)
        QApplication.restoreOverrideCursor()


        self.tableLostPac.setRowCount(len(ports))
        for i, port in enumerate(ports):
            self.tableLostPac.setItem(i, 0, QTableWidgetItem(port[0]))
            self.tableLostPac.setItem(i, 1, QTableWidgetItem(port[1]))

    def show_port_map(self):
        self.find_port_depart()
        self.create_map()
        self.listWidget.clear()

    def init_map(self):
        self.web.setGeometry(QtCore.QRect(400, 10, 651, 591))
        self.create_map()

    def set_aircrafts(self):
        self.crafts = list(self.db['aircrafts'].all())
        self.comboBox.addItems([f'{el["name"]} - {el["len"]} ft.' for el in self.crafts])
        self.len = float(self.crafts[0]["len"])

    def combo_handler(self, text):
        self.len = float(text.split('-')[1][:-4])

    def show_message(self, text):
        msgBox = QMessageBox()
        msgBox.setText(text)
        msgBox.exec_()
        self.fill_my_ports()
        self.fill_fields({})

    def write_edit(self):
        row = self.tableMyPorts.currentItem().row()
        edit_dict = {
            'icao_code': self.tableMyPorts.item(row, 0).text(),
            'name_eng': self.tableMyPorts.item(row, 1).text(),
            'city_eng': self.tableMyPorts.item(row, 2).text(),
            'country_eng': self.tableMyPorts.item(row, 3).text(),
            'iso_code': self.tableMyPorts.item(row, 4).text(),
            'runway_length': self.tableMyPorts.item(row, 5).text(),
            'latitude': self.tableMyPorts.item(row, 6).text(),
            'longitude': self.tableMyPorts.item(row, 7).text(),
            'runway_elevation': self.tableMyPorts.item(row, 8).text(),
            'id': int(self.tableMyPorts.item(row, 9).text()),
        }
        try:
            self.db['my_data'].update(edit_dict, ['id'])
        except Exception as e:
            logger.error(e)

    def del_record(self):
        row = self.tableMyPorts.currentItem().row()
        cell = self.tableMyPorts.item(row, 9).text()
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(f"Реально хотите удалить {self.tableMyPorts.item(row, 0).text()} ?")
        msgBox.setWindowTitle("Удаление")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            try:
                self.db['my_data'].delete(id=cell)
                self.fill_my_ports()
            except Exception as e:
                logger.error(e)

    def setMeter(self):
        self.metr_fut = 1

    def setFut(self):
        self.metr_fut = 3.281

    @staticmethod
    def calc_dist(lat1, lat2, lon1, lon2):
        lon1, lat1, lon2, lat2 = map(math.radians, [float(port) for port in [lon1, lat1, lon2, lat2]])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        dist = 6371 * c / 1.852
        return dist

    def find_rand_port(self):

        list_ports = [port for port in self.ports if float(port["runway_length"]) * 3.281 >= self.len]
        try:
            self.port_depart = random.choice(list_ports)
        except IndexError as e:
            logger.error(e)

        self.fromEdit.setText(self.port_depart['icao_code'])
        self.create_map()
        self.listWidget.clear()

    def find_flights(self):
        self.find_port_depart()

        self.listWidget.clear()
        max_dist = float(self.distEdit.text())
        rez_map = []
        rez = [
            f'FROM {self.port_depart["icao_code"]}  len runway - {float(self.port_depart["runway_length"]) * 3.281} ft',
            "TO:"]
        for port in self.ports:
            dist = IcaoApp.calc_dist(self.port_depart['latitude'], port['latitude'], self.port_depart['longitude'],
                                     port['longitude'])
            if max_dist > dist > 1 and float(port['runway_length']) * 3.281 >= self.len:
                rez.append(
                    f'{port["icao_code"]} dist - {round(dist)} len runway - {float(port["runway_length"]) * 3.281 if port["runway_length"] != "" else 0} ft')
                rez_map.append(port)
        #         sort to distance
        rez = rez[:2] + sorted(rez[2:], key=lambda el: float(el.split()[3]))

        if len(rez) > 2:
            self.listWidget.addItems(rez)
            if max_dist <= 100:
                size_map = 6
            elif max_dist <= 500:
                size_map = 5
            elif max_dist <= 1000:
                size_map = 4
            else:
                size_map = 4
            self.size_map = size_map
            self.arr_legs = rez_map
            self.create_map()
        else:
            self.show_message("Нет портов в доступности!")

    def find_port_depart(self):
        if len(self.fromEdit.text()) > 0:
            temp_port = self.db['my_data'].find_one(icao_code=self.fromEdit.text())
            if temp_port:
                self.port_depart = temp_port
            else:
                self.show_message("Введи правильный порт")

    def calc_coord(self):
        _translate = QtCore.QCoreApplication.translate

        text = self.coordEdit.text()
        coord_list = text.split(' ')
        temp1 = (coord_list[0][:-1], coord_list[1][:-1], coord_list[2][:-1], coord_list[3])
        coord_lat = str(self.calc(temp1))
        temp2 = (coord_list[4][:-1], coord_list[5][:-1], coord_list[6][:-1], coord_list[7])
        coord_long = str(self.calc(temp2))
        self.latEdit.setText(coord_lat)
        self.longEdit.setText(coord_long)

    @staticmethod
    def calc(coord: tuple):
        if coord[-1] == 'N' or coord[-1] == 'E':
            return float(coord[0]) + float(coord[1]) / 60 + float(coord[2].replace(',', '.')) / 3600
        else:
            rez = float(coord[0]) + float(coord[1]) / 60 + float(coord[2].replace(',', '.')) / 3600
            return -rez

    def add_my_port(self):
        try:
            add_dict = {
                'icao_code': self.icaoEdit.text(),
                'name_eng': self.cityEdit.text(),
                'city_eng': self.cityEdit.text(),
                'country_eng': self.countryEdit.text(),
                'iso_code': self.code_countryEdit.text(),
                'latitude': self.latEdit.text(),
                'longitude': self.longEdit.text(),
                'runway_length': str(float(self.runwayEdit.text()) / self.metr_fut),
                'runway_elevation': str(float(self.evevEdit.text()) / self.metr_fut),
            }
        except ValueError as e:
            self.show_message('Заполни все поля!!!')
        else:
            with self.db as tx1:
                tx1['my_data'].insert(add_dict)

            self.show_message('Порт Добавлен')
            self.coordEdit.setText('')

    def find_appinfo(self):
        text = self.icaoEdit.text()
        port = self.db['icao_data'].find_one(icao_code=text)
        if port:
            self.fill_fields(port)

        else:
            self.show_message("Не найдено !!!")

    def find_skyvector(self):
        text = self.icaoEdit.text()
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        port = data_from_skyvector(text)
        QApplication.restoreOverrideCursor()
        if port.get('err', 0):
            self.show_message("Не найдено !!!")
            return
        coord_list = port.get('coordinats').split()
        temp1 = (coord_list[0][:-1], coord_list[1][:-1], coord_list[2][:-1], coord_list[3])
        coord_lat = str(self.calc(temp1))
        temp2 = (coord_list[4][:-1], coord_list[5][:-1], coord_list[6][:-1], coord_list[7])
        coord_long = str(self.calc(temp2))
        port['latitude'] = coord_lat
        port['longitude'] = coord_long
        self.fill_fields(port)

    def fill_fields(self, port):
        self.nameEdit.setText(port.get('name_eng', ''))
        self.cityEdit.setText(port.get('city_eng', ''))
        self.countryEdit.setText(port.get('country_eng', ''))
        self.code_countryEdit.setText(port.get('iso_code', ''))
        self.latEdit.setText(port.get('latitude', ''))
        self.longEdit.setText(port.get('longitude', ''))
        try:
            self.runwayEdit.setText(str(round(float(port.get('runway_length', '0')) * self.metr_fut)))
            self.evevEdit.setText(str(round(float(port.get('runway_elevation', '0')) * self.metr_fut)))
        except ValueError as e:
            self.runwayEdit.setText('0')
            self.evevEdit.setText('0')
            logger.error(e)

    def filter_my_ports(self):
        text = self.icaoEdit.text()
        port = self.db['my_data'].find_one(icao_code=text)
        if port:
            self.tableMyPorts.setRowCount(1)
            self.tableMyPorts.setItem(0, 0, QTableWidgetItem(port['icao_code']))
            self.tableMyPorts.setItem(0, 1, QTableWidgetItem(port['name_eng']))
            self.tableMyPorts.setItem(0, 2, QTableWidgetItem(port['city_eng']))
            self.tableMyPorts.setItem(0, 3, QTableWidgetItem(port['country_eng']))
            self.tableMyPorts.setItem(0, 4, QTableWidgetItem(port['iso_code']))
            self.tableMyPorts.setItem(0, 5, QTableWidgetItem(port['runway_length']))
            self.tableMyPorts.setItem(0, 6, QTableWidgetItem(port['latitude']))
            self.tableMyPorts.setItem(0, 7, QTableWidgetItem(port['longitude']))
            self.tableMyPorts.setItem(0, 8, QTableWidgetItem(port['runway_elevation']))
            self.tableMyPorts.setItem(0, 9, QTableWidgetItem(str(port['id'])))
            self.fill_fields(port)
        else:
            self.show_message("Не найдено !!!")

    def fill_my_ports(self):
        self.ports = list(self.db['my_data'].all())
        self.tableMyPorts.setRowCount(len(self.ports))
        for i, port in enumerate(self.ports):
            self.tableMyPorts.setItem(i, 0, QTableWidgetItem(port['icao_code']))
            self.tableMyPorts.setItem(i, 1, QTableWidgetItem(port['name_eng']))
            self.tableMyPorts.setItem(i, 2, QTableWidgetItem(port['city_eng']))
            self.tableMyPorts.setItem(i, 3, QTableWidgetItem(port['country_eng']))
            self.tableMyPorts.setItem(i, 4, QTableWidgetItem(port['iso_code']))
            self.tableMyPorts.setItem(i, 5, QTableWidgetItem(port['runway_length']))
            self.tableMyPorts.setItem(i, 6, QTableWidgetItem(port['latitude']))
            self.tableMyPorts.setItem(i, 7, QTableWidgetItem(port['longitude']))
            self.tableMyPorts.setItem(i, 8, QTableWidgetItem(port['runway_elevation']))
            self.tableMyPorts.setItem(i, 9, QTableWidgetItem(str(port['id'])))

    def fill_path_find(self):
        self.paths = get_param_from_db(self.db, 'path_to_community')
        self.tablePath.setRowCount(len(self.paths))
        for i, path in enumerate(self.paths):
            self.tablePath.setItem(i, 0, QTableWidgetItem(path))

    def add_patch(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        options |= QFileDialog.ShowDirsOnly
        options |= QFileDialog.DontResolveSymlinks
        # fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
        #                                           "All Files (*);;Python Files (*.py)", options=options)
        fileName = QFileDialog.getExistingDirectory(self, 'Select a directory', "", options=options)
        if fileName:
            self.paths.append(fileName)
            set_param_to_db(self.db, 'path_to_community', self.paths)
            self.fill_path_find()

    def rem_patch(self):
        row = self.tablePath.currentItem().text()
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(f"Реально хотите удалить ?")
        msgBox.setWindowTitle("Удаление")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            try:
                self.paths.remove(row)
                set_param_to_db(self.db, 'path_to_community', self.paths)
                self.fill_path_find()
            except Exception as e:
                logger.error(e)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = IcaoApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
