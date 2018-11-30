import folium
import pandas as pd

data = pd.read_csv('Volcanoes.txt', sep=',')
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles='Mapbox Bright')

fg = folium.FeatureGroup(name="Feature Group")


for i, j, l in zip(lat, lon, elev):
    color ='green'
    if l <= 1000:
        color = 'green'
    elif l > 1000 and l <= 3000:
        color = 'blue'
    else:
        color = 'red'
    fg.add_child(folium.Marker(location=[i, j], popup=str(l), 
    icon=folium.Icon(color=str(color))))



map.add_child(fg)
map.save('Map1.html')
