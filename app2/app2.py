import pandas
import folium

# retrieve data
volcanoes = pandas.read_csv("volcanoes.txt")

# extract latitude, longitude and names from data file. Create lists with them
_latitude = list(volcanoes["LAT"])
_longitude = list(volcanoes["LON"])
_name = list(volcanoes["NAME"])
_elevation = list(volcanoes["ELEV"])


map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6,
                 tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")


def color(elevation):
    if elevation < 3000:
        return 'green'
    else:
        return 'red'


# loop for latitude and longitude over data
for lat, lon, name, elev in zip(_latitude, _longitude, _name, _elevation):
    # print(name, lat, lon)
    fgv.add_child(folium.Marker(
        location=[lat, lon],
        popup=name + ": " + str(elev)+"m",
        icon=folium.Icon(color=color(elev))))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data="geojson.json", style_function=lambda x: {
    'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map1.html")
