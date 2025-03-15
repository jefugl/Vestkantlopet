import folium
import pandas

data = pandas.read_csv("vestkantløpet.txt")
lat = list(data["lat"])
lon = list(data["long"])
nm = list(data["name"])
adr = list(data["adresse"])

kart = folium.Map(location=[59.9168, 10.7128], zoom_start=17, tiles="OpenStreetMap")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, nm, adr in zip(lat, lon, nm, adr):
    fg.add_child(folium.Marker(
        location=[lt, ln],
        popup=f"{nm}\n{adr}",
        icon=folium.DivIcon(html=f"""<div style="font-family: courier new; color: blue">{nm}</div>""")))
    kart.add_child(fg)

kart.save("vestkantlopet2022.html")


# "Stamen Terrain"
# "OpenStreetMap"

# kart = folium.Map(location=[59.91469432548203, 10.710102890982766], width='100%', height='100%', left='0%', top='0%',
#                   position='relative', tiles='Stamen Terrain', attr=None, min_zoom=10, max_zoom=17, zoom_start=18,
#                   min_lat=50, max_lat=90, min_lon=50, max_lon=90, max_bounds=False, crs='EPSG3857', control_scale=False,
#                   prefer_canvas=False, no_touch=False, disable_3d=False, png_enabled=False, zoom_control=True)
