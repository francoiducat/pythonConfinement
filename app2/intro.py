import folium

map = folium.Map(location=[38.58, -99.09],
                 zoom_start=10,
                 tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="MyMap")

fg.add_child(folium.Marker(
    location=[38.2, -99.1],
    popup="Hi I'm a Folium Marker",
    icon=folium.Icon(color='red')))

map.add_child(fg)

map.save("map1.html")
