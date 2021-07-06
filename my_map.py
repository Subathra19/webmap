import folium
from folium.map import Icon
import pandas


map=folium.Map(location=[13.082269, 80.277665],zoom_start=5,tiles="OpenStreetMap")

fgC=folium.FeatureGroup(name="Countries")

data=pandas.read_csv("Book1.csv")
latitude=list(data["Capital Latitude"])
longitude=list(data["Capital Longitude"])
country_name=list(data["Country Name"])
capital_name=list(data["Capital Name"])
continent_name=list(data["Continent Name"])

html = """<h4>Information:</h4>

<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a>
<br>
Capital: %s
</br>
Continent: %s
"""

def get_color(continent):
    if(continent=="Asia"):
        return "blue"
    elif(continent=="Africa"):
        return "red"
    elif(continent=="Europe"):
        return "pink"
    elif(continent=="Australia"):
        return "orange"
    elif(continent=="North America"):
        return "darkpurple"
    elif(continent=="South America"):
        return "green"
    else:    
        return "lightgray"


for lat,lon,country,capital,continent in zip(latitude,longitude,country_name,capital_name,continent_name):
    frame=folium.IFrame(html=html % (country,country,capital,continent),width=200,height=100)
    fgC.add_child(folium.Marker(location=[lat,lon],popup=folium.Popup(frame),icon=folium.Icon(color=get_color(continent))))

fgP=folium.FeatureGroup(name="Population")
fgP.add_child(folium.GeoJson(open("world.json",encoding = "utf-8-sig").read(),
style_function=lambda x: {"fillColor":"green" if x["properties"]["POP2005"]<10000000 else "yellow" if x["properties"]["POP2005"]>=10000000 and x["properties"]["POP2005"]<20000000 else "red"}))

map.add_child(fgC)
map.add_child(fgP)

map.add_child(folium.LayerControl())
map.save("mymap.html")
