import folium
import pandas

#Generates a map to the specific co-ordinates
#The numbers are the lat and long co-ords.
#For zoom a lower number zoom out a higher number zooms in.
map = folium.Map(location=[38.58, -99.09], zoom_start=7)

feature = folium.FeatureGroup(name="MyMap")
feature.add_child(
    folium.Marker(location=[38.2, -99.1],
                  popup="Hi I'm here!!",
                  icon=folium.Icon(color='blue')))
feature.add_child(
    folium.Marker(location=[37.2, -97.1],
                  popup="Hi I'm here!!",
                  icon=folium.Icon(color='blue')))
#A better way would be to use a for loop
#Essentially the for loop iterates through the list of co-ords
#plotting them as per the code
for coords in [[38.6, -99.01], [37.2, -97.1], [38.4, -98.7], [37.9, -98.3]]:
    feature.add_child(
        folium.Marker(location=coords,
                      popup="Hi I'm here!!",
                      icon=folium.Icon(color='blue')))

volcano_data = pandas.read_csv("volcanoes.txt")
#The labels in the [] brackets are column labels as they are in the .csv file
lat = list(volcano_data["LAT"])
lon = list(volcano_data["LON"])
elev = list(volcano_data["ELEV"])


def colour_with_elev(elevation):
    if elevation < 1500:
        return 'green'
    elif 1500 <= elevation < 3000:
        return 'orange'
    elif elevation >= 3000:
        return 'red'


for la, ln, ele in zip(lat, lon, elev):
    feature.add_child(
        folium.CircleMarker(
            location=[la, ln],
            popup=folium.Popup(str(ele) + " m", parse_html=True),
            #icon=folium.Icon(color=colour_with_elev(ele)),
            fill_color=colour_with_elev(ele),
            color='grey',
            fill_opacity=0.7,
            radius=6,
        ))

feature.add_child(
    folium.GeoJson(
        data=(open('world.json', 'r', encoding='utf-8-sig').read())))

#Helps to beter organise features and code.
map.add_child(feature)
#Saves the map to a html file
map.save("Map.html")
