from os import path, listdir
import re
import dataset
import csv
import requests
from bs4 import BeautifulSoup, SoupStrainer

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


def data_from_skyvector(icao_kod):
    # OrderedDict([('id', 5676), ('icao_code', 'URMO'), ('name_eng', 'Beslan'), ('city_eng', 'Vladikavkaz'),
    #              ('country_eng', 'Russian Federation'), ('iso_code', 'RU'), ('latitude', '43.205114'),
    #              ('longitude', '44.606642'), ('runway_length', '3000'), ('runway_elevation', '510')])
    rez ={'icao_code': icao_kod}
    url = f'https://skyvector.com/airport/{icao_kod}'
    try:
        response = requests.get(url)
    except ConnectionError as e:
        rez['err'] = e.strerror
        return rez
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        name = soup.find('div', class_='titlebgrighta').text
    except AttributeError as e:
        rez['err'] = e
        return rez
    countries = soup.find_all('a')
    for el in countries:
        if 'Airports in' in el.text:
            rez['country_eng'] = el.text.split()[-1]
            break
    rez['name_eng'] = name
    rez['city_eng'] = name

    arp_data = soup.find_all('tr')
    for el in arp_data:
        try:
            if el.find(string='Dimensions:'):
                rez['runway_length'] = float(el.find('td').text.split()[0])/3.281
        except IndexError as e:
            rez['runway_length'] = 0
        try:
            if el.find(string='Elevation:'):
                rez['runway_elevation'] = float(el.find('td').text)/3.281
        except IndexError as e:
            rez['runway_elevation'] = 0

    url = f'https://opennav.com/airport/{icao_kod}'
    try:
        response = requests.get(url)
    except ConnectionError as e:
        rez['err'] = e
        return rez
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        country_codes = soup.find_all('td', class_='text-darkgray')
    except AttributeError as e:
        rez['err'] = e
        return rez
    try:
        rez['iso_code'] = country_codes[1].text
        rez['coordinats'] = f'{country_codes[-2].text} {country_codes[-1].text}'
    except IndexError as e:
        rez['err'] = e
        return rez
    return rez


if __name__ == '__main__':
    # community_ikao()
    print(data_from_skyvector('URMO'))
    pass


