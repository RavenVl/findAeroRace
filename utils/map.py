import gmplot
from settings import SECRET_KEY

def create_map(port_depart = None, arr_legs = None, size=6):
    """Create Google map from database"""
    # Create the map plotter:
    apikey = SECRET_KEY
    if port_depart is None:
        gmap = gmplot.GoogleMapPlotter(0, 0, 1, apikey=apikey)
    else:
        lat_dep = float(port_depart['latitude'])
        long_dep = float(port_depart['longitude'])
        gmap = gmplot.GoogleMapPlotter(lat_dep, long_dep, size, apikey=apikey)
        gmap.marker(lat_dep, long_dep, color='red', title=port_depart['name_eng'], precision=4, label=port_depart['icao_code'])

    if arr_legs is not None:
        for port in arr_legs:
            try:
                lat = float(port['latitude'])
                long = float(port['longitude'])
            except Exception as e:
                print(e)
            else:
                gmap.marker(lat, long, color='cornflowerblue', title=port['name_eng'], precision=4, label=port['icao_code'])

    gmap.draw('map.html')



if __name__ == '__main__':
    arr_ports = [
                 dict([('id', 9433), ('icao_code', 'UKOO'), ('name_eng', 'Odessa International'), ('city_eng', 'Odessa'), ('country_eng', 'Ukraine'), ('iso_code', 'UA'), ('latitude', '46.426767'), ('longitude', '30.676464'), ('runway_length', '2800'), ('runway_elevation', '52'), ('runway_elevatio', None)]),
                 dict([('id', 9489), ('icao_code', 'UUOB'), ('name_eng', 'Belgorod'), ('city_eng', 'Belgorod'), ('country_eng', 'Russian Federation'), ('iso_code', 'RU'), ('latitude', '50.643764'), ('longitude', '36.590125'), ('runway_length', '2500'), ('runway_elevation', '224'), ('runway_elevatio', None)]),
                 dict([('id', 9812), ('icao_code', 'UMMS'), ('name_eng', 'Minsk'), ('city_eng', 'Minsk'), ('country_eng', 'Belarus'), ('iso_code', 'BY'), ('latitude', '53.882469'), ('longitude', '28.030731'), ('runway_length', '3600.0'), ('runway_elevation', '204.0'), ('runway_elevatio', None)])
                 ]
    cur_pos = dict([('id', 9432), ('icao_code', 'UKLL'), ('name_eng', 'Sknilow'), ('city_eng', 'Lviv'), ('country_eng', 'Ukraine'), ('iso_code', 'UA'), ('latitude', '49.812500'), ('longitude', '23.956111'), ('runway_length', '2510'), ('runway_elevation', '326'), ('runway_elevatio', None)])
    create_map(cur_pos, arr_ports)