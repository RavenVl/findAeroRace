import asyncio
import csv
import json
import queue
import re
from collections.abc import Iterable
from itertools import chain
from pathlib import Path

import dataset
import requests
from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession


def get_param_from_db(db_, param_name) -> list:
    table_settings = db_['settings']
    param = json.loads(table_settings.find_one(param=param_name)['content'])
    return param


def set_param_to_db(db_, param_name, content):
    table_settings = db_['settings']
    add_dict = {
        'param': param_name,
        'content': json.dumps(content)
    }
    key = table_settings.find_one(param=param_name)
    if key:
        add_dict['id'] = key['id']
        table_settings.update(add_dict, ['id'])
    else:
        table_settings.insert(add_dict)


async def get_name_port(icao_kod, asession, q):
    url = f'https://skyvector.com/airport/{icao_kod[0]}'
    r = await asession.get(url)
    rez = r.html.find('div.titlebgrighta', first=True)
    if rez:
        q.put(icao_kod)


async def check_sky_vector_icao_codes(icao_codes: Iterable, q):
    asession = AsyncHTMLSession()
    tasks = []
    for el in icao_codes:
        task = asyncio.create_task(get_name_port(el, asession, q))
        tasks.append(task)

    await asyncio.gather(*tasks)


def community_ikao(db_):
    dirs = get_param_from_db(db_, 'path_to_community')
    dirs_path = [list(Path(path_).iterdir()) for path_ in dirs]
    file_list = [elem.stem for elem in chain(*dirs_path)]

    table_my = db_['my_data']
    temp_port_check = set()
    temp_del = set()
    for name in file_list:
        reg_exp = r"-[a-zA-Z]{4}-|^[a-zA-Z]{4}-|-[a-zA-Z]{4}$"
        ikao_kod = re.findall(reg_exp, name)
        for test_name in ikao_kod:
            test_name = test_name.replace('-', '')
            port_my_base = table_my.find_one(icao_code=test_name.upper())
            if port_my_base:
                break
            port_icao_base = db_['ikao_data'].find_one(icao_code=test_name.upper())
            if port_icao_base:
                temp_port_check.add((test_name, name))
            else:
                temp_del.add((test_name, name))

    q = queue.Queue()
    asyncio.run(check_sky_vector_icao_codes(temp_del, q))
    while not q.empty():
        temp_port_check.add(q.get())


    # print(temp_port_check)
    return temp_port_check


def convert_csv():
    db = dataset.connect('sqlite:///data/icao_base.db')
    with open('data/apinfo.ru.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='|', )
        for row in spamreader:
            with db as tx1:
                tx1['icao_data'].insert(dict(icao_code=row[0], name_eng=row[2], city_eng=row[4], country_eng=row[6],
                                             iso_code=row[8], latitude=row[10], longitude=row[12],
                                             runway_length=row[14],
                                             runway_elevation=row[16]))


def data_from_opennav(icao_kod, rez):
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


def data_from_skyvector(icao_kod):
    # OrderedDict([('id', 5676), ('icao_code', 'URMO'), ('name_eng', 'Beslan'), ('city_eng', 'Vladikavkaz'),
    #              ('country_eng', 'Russian Federation'), ('iso_code', 'RU'), ('latitude', '43.205114'),
    #              ('longitude', '44.606642'), ('runway_length', '3000'), ('runway_elevation', '510')])
    rez = {'icao_code': icao_kod}
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
                rez['runway_length'] = float(el.find('td').text.split()[0]) / 3.281
        except IndexError as e:
            rez['runway_length'] = 0
        except ValueError as e:
            rez['runway_length'] = 0
        try:
            if el.find(string='Elevation:'):
                rez['runway_elevation'] = float(el.find('td').text) / 3.281
        except IndexError as e:
            rez['runway_elevation'] = 0
    rez = data_from_opennav(icao_kod, rez)
    return rez


if __name__ == '__main__':
    # community_ikao()
    # print(data_from_skyvector('URM1'))
    # db = dataset.connect('sqlite:///../data/icao_base.db')
    # community_ikao(db)
    pass
