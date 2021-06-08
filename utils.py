from os import path, listdir
import re
import dataset
import csv


def community_ikao():
    DIR_COMMUNYTI = path.join('c:\\users\\raven\\appdata\\roaming\\microsoft flight simulator\\packages\\community\\')
    print(DIR_COMMUNYTI)
    file_list = listdir(DIR_COMMUNYTI)
    db = dataset.connect('sqlite:///data/icao_base.db')
    table_icao = db['icao_data']
    temp = []
    temp_del = set()
    for name in file_list:
        reg_exp = r"[a-zA-Z]{4}"
        ikao_kod = re.findall(reg_exp, name)
        for test_name in ikao_kod:
            port = table_icao.find_one(icao_code=test_name.upper())
            print(port)
            if port:
                with db as tx1:
                    tx1['my_data'].insert(dict(icao_code=port['icao_code'], name_eng=port['name_eng'], city_eng=port['city_eng'],
                                               country_eng=port['country_eng'],
                                                 iso_code=port['iso_code'], latitude=port['latitude'], longitude=port['longitude'],
                                                 runway_length=port['runway_length'],
                                                 runway_elevation=port['runway_elevation']))


    print(len(temp))
    # for name in ikao:
    #     port = table_icao.find_one(icao_code=name.upper())
    #
    #     if port:
    #         # with db as tx1:
    #         #     tx1['my_data'].insert(port)
    #         pass
    #     else:
    #         print(name)

def convert_csv():

    db = dataset.connect('sqlite:///data/icao_base.db')
    with open('data/apinfo.ru.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='|',)
        for row in spamreader:
            with db as tx1:
                tx1['icao_data'].insert(dict(icao_code=row[0], name_eng=row[2], city_eng=row[4], country_eng=row[6],
                              iso_code=row[8], latitude=row[10], longitude=row[12], runway_length=row[14],
                              runway_elevation=row[16]))


if __name__ == '__main__':
    # community_ikao()
    pass


