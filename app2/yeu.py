import folium

map = folium.Map(location=[46.7094, -2.3466],
                 zoom_start=14,
                 tiles="Stamen Terrain")
map.save("yeu.html")
