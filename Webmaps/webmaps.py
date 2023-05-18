import folium
import pandas

#Generates a map to the specific co-ordinates
#The numbers are the lat and long co-ords.
#For zoom a lower number zoom out a higher number zooms in.
map = folium.Map(location=[38.58, -99.09], zoom_start=7)

#You can have many different groups for diferent things.
#Remember for each child to attach the apppropriate feature group
#It allows for each feature to be its own layer, good for consistency
feature = folium.FeatureGroup(name="MyMap")
f_vol = folium.FeatureGroup(name="Volcanoes")
f_pop = folium.FeatureGroup(name="Population")

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
    f_vol.add_child(
        folium.CircleMarker(
            location=[la, ln],
            popup=folium.Popup(str(ele) + " m", parse_html=True),
            #icon=folium.Icon(color=colour_with_elev(ele)),
            fill_color=colour_with_elev(ele),
            color='grey',
            fill_opacity=0.7,
            radius=6,
        ))

#The values in the [] brackets are from the dataset columns
#In this case the lambda x :{} is a type of functon that can be inserted
#inline to add function to style code so that is can change with data points.
f_pop.add_child(
    folium.GeoJson(
        data=open('world.json', 'r', encoding='utf-8-sig').read(),
        style_function=lambda x: {
            'fillColor':
            'green' if x['properties']['POP2005'] < 10000000 else 'orange'
            if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'
        }))

#Helps to beter organise features and code.
map.add_child(feature)
map.add_child(f_vol)
map.add_child(f_pop)
#Ensure that this is added after you add all the other children and feature groups
map.add_child(folium.LayerControl())
#Saves the map to a html file
map.save("Map.html")
