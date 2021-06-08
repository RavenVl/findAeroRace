import sys  # sys нужен для передачи argv в QApplication
import dataset
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
import random
import MainWindow  # Это наш конвертированный файл дизайна
import math
from loguru import logger
#TODO process add empty data in add port
logger.add("error.log", level="ERROR", rotation="100 MB", format="{time} - {level} - {message}")


class Validator(QtGui.QValidator):
    def validate(self, string, pos):
        return QtGui.QValidator.Acceptable, string.upper(), pos


class IcaoApp(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.db = dataset.connect('sqlite:///data/icao_base.db')
        self.findButton.clicked.connect(self.filter_my_ports)
        self.findButtonApinfo.clicked.connect(self.find_appinfo)
        self.showAllButton.clicked.connect(self.fill_my_ports)
        self.addButton.clicked.connect(self.add_my_port)
        self.coordButton.clicked.connect(self.calc_coord)
        self.randButton.clicked.connect(self.find_rand_port)
        self.findFlyButton.clicked.connect(self.find_flights)
        self.delButton.clicked.connect(self.del_record)
        self.writeButton_2.clicked.connect(self.write_edit)
        self.ports = None
        self.port_depart = None
        self.fill_my_ports()
        self.metr_fut = 1  # 3.281
        self.radioButtonM.toggled.connect(self.setMeter)
        self.radioButtonF.toggled.connect(self.setFut)
        self.validator = Validator(self)
        self.icaoEdit.setValidator(self.validator)
        self.fromEdit.setValidator(self.validator)

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
            'latitude': self.tableMyPorts.item(row, 5).text(),
            'longitude': self.tableMyPorts.item(row, 6).text(),
            'runway_length': self.tableMyPorts.item(row, 7).text(),
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
        self.port_depart = random.choice(self.ports)
        self.fromEdit.setText(self.port_depart['icao_code'])

    def find_flights(self):
        if self.port_depart is None:
            temp_port = self.db['my_data'].find_one(icao_code=self.fromEdit.text())
            if temp_port:
                self.port_depart = temp_port
            else:
                self.show_message("Введи правильный порт")

        self.listWidget.clear()
        max_dist = float(self.distEdit.text())

        rez = [
            f'FROM {self.port_depart["icao_code"]}  len runway - {float(self.port_depart["runway_length"]) * 3.281} ft',
            "TO:"]
        for port in self.ports:
            dist = IcaoApp.calc_dist(self.port_depart['latitude'], port['latitude'], self.port_depart['longitude'],
                                     port['longitude'])
            if max_dist > dist > 1:
                rez.append(
                    f'{port["icao_code"]} dist - {round(dist)} len runway - {float(port["runway_length"]) * 3.281 if port["runway_length"] != "" else 0} ft')
        if len(rez) > 2:
            self.listWidget.addItems(rez)
        else:
            self.show_message("Нет портов в доступности!")

    def calc_coord(self):
        _translate = QtCore.QCoreApplication.translate

        def calc(coord):
            if coord[-1] == 'N' or coord[-1] == 'E':
                return float(coord[0]) + float(coord[1]) / 60 + float(coord[2].replace(',', '.')) / 3600
            else:
                rez = float(coord[0]) + float(coord[1]) / 60 + float(coord[2].replace(',', '.')) / 3600
                return -rez

        text = self.coordEdit.text()
        coord_list = text.split(' ')
        temp1 = (coord_list[0][:-1], coord_list[1][:-1], coord_list[2][:-1], coord_list[3])
        coord_lat = str(calc(temp1))
        temp2 = (coord_list[4][:-1], coord_list[5][:-1], coord_list[6][:-1], coord_list[7])
        coord_long = str(calc(temp2))
        self.latEdit.setText(coord_lat)
        self.longEdit.setText(coord_long)

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


    def find_appinfo(self):
        text = self.icaoEdit.text()
        port = self.db['icao_data'].find_one(icao_code=text)
        if port:
            self.fill_fields(port)

        else:
            self.show_message("Не найдено !!!")


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


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = IcaoApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
