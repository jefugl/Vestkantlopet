import inputdata
import folium
from folium.features import DivIcon
import pandas as pd
import webbrowser


def main():

    start = 59.9172, 10.72

    data = pd.DataFrame({
        "lat": inputdata.latitude,
        "lon": inputdata.longitude,
        "name": inputdata.pubname,
        "addr": inputdata.pubaddress,
        "img": [inputdata.sumo, inputdata.fruburums, inputdata.andy, inputdata.victor, inputdata.frognerkino,
                inputdata.forestbrown, inputdata.tiffany, inputdata.enoteca, inputdata.gabler]
    })

    m = folium.Map(location=start, width=750, height=550, zoom_start=15.8, min_zoom=10, max_zoom=18,
                   tiles="Stamen Terrain")

    for i in range(0, len(data)):
        folium.Marker(
            location=[data.iloc[i]["lat"], data.iloc[i]["lon"]],
            popup=data.iloc[i]['addr'],
            icon=DivIcon(html=f"""<div style="font-size: 12pt;font-family: helvetica;
            color: purple">{data.iloc[i]["name"]}</div>""")
        ).add_to(m)

    tooltip = "Klikk på meg"

    for i in range(0, len(data)):
        html = f"""<div>
            <img src={data.iloc[i]["img"]}>
            <br /><span>{data.iloc[i]["name"]}</span>
            <br /><span>{data.iloc[i]["addr"]}</span>
            </div>"""
        iframe = folium.IFrame(html)
        popup = folium.Popup(iframe, min_width=500, max_width=500)
        folium.Marker(
            location=[data.iloc[i]["lat"], data.iloc[i]["lon"]],
            popup=popup,
            icon=folium.Icon(icon="beer", prefix="fa", color="blue"),
            tooltip=tooltip,
        ).add_to(m)

    title = "Vestkantløpet vestkantløpet_2023"
    title_html = """
                 <h3 align="center" style="width:40%;"font-size:22px"><b>{}</b></h3>
                 """.format(title)
    m.get_root().html.add_child(folium.Element(title_html))

    folium.TileLayer('OpenStreetMap').add_to(m)
    folium.TileLayer('Stamen Toner').add_to(m)
    folium.TileLayer('Stamen Water Color').add_to(m)
    folium.TileLayer('cartodbpositron').add_to(m)
    folium.TileLayer('cartodbdark_matter').add_to(m)
    folium.LayerControl().add_to(m)

    m.save("index.html")

    webbrowser.open("vestkantløpet.html")


if __name__ == "__main__":
    main()
