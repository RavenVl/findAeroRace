import gmplot
from settings import SECRET_KEY

def create_map(curent_position = None, arr_legs = None):
    """Create Google map from database"""

    # Create the map plotter:
    apikey = SECRET_KEY
    if curent_position is None:
        gmap = gmplot.GoogleMapPlotter(0, 0, 1, apikey=apikey)
    else:
        gmap = gmplot.GoogleMapPlotter(curent_position[0], curent_position[1], 4, apikey=apikey)
        gmap.marker(curent_position[0], curent_position[1], color='cornflowerblue')
    gmap.draw('map.html')

if __name__ == '__main__':
    create_map()