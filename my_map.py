import folium
from folium.map import Icon
import pandas


map=folium.Map(location=[13.082269, 80.277665],zoom_start=5,tiles="OpenStreetMap")

fgC=folium.FeatureGroup(name="Countries")

data=pandas.read_csv("countries.csv")
latitude=list(data["latitude"])
longitude=list(data["longitude"])
country_name=list(data["name"])

html = """<h4>Information:</h4>
Name: <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a>
"""

for lat,lon,name in zip(latitude,longitude,country_name):
    frame=folium.IFrame(html=html % (name,name),width=200,height=100)
    fgC.add_child(folium.Marker(location=[lat,lon],popup=folium.Popup(frame),icon=folium.Icon(color="red")))

fgP=folium.FeatureGroup(name="Population")
fgP.add_child(folium.GeoJson(open("world.json",encoding = "utf-8-sig").read(),
style_function=lambda x: {"fillColor":"green" if x["properties"]["POP2005"]<10000000 else "yellow" if x["properties"]["POP2005"]>=10000000 and x["properties"]["POP2005"]<20000000 else "red"}))

map.add_child(fgC)
map.add_child(fgP)

map.add_child(folium.LayerControl())
map.save("mymap.html")
