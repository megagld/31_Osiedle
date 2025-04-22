#bmystek

import folium
import gpxpy
import os
import webbrowser

map_center = [50.32242, 18.652014]

m = folium.Map(map_center, zoom_start=15)

def add_to_map(folium_map, path, name):

    file_path=os.path.join(path, name)
        
    gpx_file = open(file_path, 'r')

    gpx = gpxpy.parse(gpx_file)

    points = []

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                points.append([point.latitude,point.longitude])


    fg = folium.FeatureGroup()
    fg.add_to(folium_map)

    radius = 20

    for point in points:

        folium.Circle(
            location=point,
            radius=radius,
            color=None,
            weight=1,
            fill_opacity=0.6,
            opacity=1,
            fill_color="green",
            fill=True,  # gets overridden by fill_color
            popup=name,
            tooltip=f"promień {radius}m",
        ).add_to(fg)
    folium_map.keep_in_front(fg)

    my_PolyLine = folium.PolyLine(locations=points,
                                color="green",
                                weight=radius//2,
                                opacity=.6
                                )
    folium_map.add_child(my_PolyLine)



input_dir = os.getcwd()

for path, subdirs, files in os.walk(input_dir):
    for name in files:
        if name.endswith('.gpx'):
            add_to_map(m, path, name)


m.save('testing_map.html')

webbrowser.open('testing_map.html')
