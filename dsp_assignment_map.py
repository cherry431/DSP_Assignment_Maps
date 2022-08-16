# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FWK4jQTxtOnVsp84vsiH9X_LqkDSGMLh
"""

import folium
# define the world map
world_map = folium.Map()

# display world map
world_map

from branca.element import Figure
nuzvid=folium.Map(location=[16.79401908016765, 80.86978828337269])
nuzvid

coords_1=[[16.7850, 80.8488],
[16.6800,80.7852],[16.5062, 80.6480],[16.2379,80.6444],[16.2379,80.6444],[15.5057,80.0499]]

coords_2=[[16.7850, 80.8488],
[16.6800,80.7852],[16.5419,80.8050],[16.5062, 80.6480],[16.0948,80.1656],[15.9938,80.1038],[15.8107,79.9724],[15.7245,80.0189],[15.5057,80.0499]]

coords_3=[[16.7850, 80.8488],
[16.6356,80.9716],[16.5419,80.8050],[16.5062, 80.6480],[16.2356,80.5605],[15.9039,80.4671],[15.5057,80.0499]]

fig1=Figure(height=550,width=750)
map1=folium.Map(location=[16.7850, 80.8488],zoom_start=10,tiles='cartodbpositron')
fig1.add_child(map1)

# Creating feature groups
f1=folium.FeatureGroup("ROOT1")
f2=folium.FeatureGroup("ROOT2")
f3=folium.FeatureGroup("ROOT3")



# Adding lines to the different feature groups
line_1=folium.vector_layers.PolyLine(coords_1,popup='<b>Path of ROOT1</b>',tooltip='ROOT1',color='black',weight=10).add_to(f1)
line_2=folium.vector_layers.PolyLine(coords_2,popup='<b>Path of ROOT2</b>',tooltip='ROOT2',color='yellow',weight=10).add_to(f2)
line_3=folium.vector_layers.PolyLine(coords_3,popup='<b>Path of ROOT3</b>',tooltip='ROOT3',color='purple',weight=10).add_to(f3)

#Adding markers to the map
folium.Marker(location=[16.7850, 80.8488],popup='Default popup Marker1',tooltip='rgukt',icon=folium.Icon(color='red',prefix='fa',icon='fa-building')).add_to(map1)
folium.Marker(location=[15.5057,80.0499],popup='<strong>cab service</strong>',tooltip='<strong> venkata ramana cab service</strong>',icon=folium.Icon(color='aqua',prefix='fa',icon='fa-cab')).add_to(map1)
folium.Marker(location=[16.554288324639046, 80.64542298762802],popup='<h3 style="color:green;">airport</h3>',tooltip='<strong>airport</strong>',icon=folium.Icon(color='purple',prefix='fa',icon='fa-plane')).add_to(map1)

folium.Marker(location=[16.645767012250108, 80.96371798842192],popup='<strong>hospital</strong>',tooltip='<strong>hospital</strong>',icon=folium.Icon(color='white',prefix='fa',icon='fa-plus-circle')).add_to(map1)

folium.Marker(location=[16.25855114531031, 80.62863498653662],popup='<strong></strong>',tooltip='<strong>BUS TOP,GUNTUR</strong>',icon=folium.Icon(color='black',prefix='fa',icon='fa-bus')).add_to(map1)

folium.Marker(location=[16.094025038769146, 80.5481354055485],tooltip='<strong>yuggu MECHANIC WORKS</strong>',icon=folium.Icon(color='blue',prefix='fa',icon='fa-motorcycle')).add_to(map1)
folium.Marker(location=[15.969326093974392, 80.09290522863338],popup='<strong>bank of baroda</strong>',tooltip='<strong>bank of baroda</strong>',icon=folium.Icon(color='brown',prefix='fa',icon='fa-institution')).add_to(map1)
folium.Marker(location=[15.711212405512045, 80.03413423735878],popup='<strong>studio</strong>',tooltip='<strong>Ramana studio</strong>',icon=folium.Icon(color='grey',prefix='fa',icon='fa-camera')).add_to(map1)
folium.Marker(location=[16.52012374725115, 80.60470110918423],popup='<strong>temple</strong>',tooltip='<strong>DURGA MALLESWARA SWAMI TEMPLE</strong>',icon=folium.Icon(color='orange',prefix='fa',icon='fa-ship')).add_to(map1)
map1

f1.add_to(map1)
f2.add_to(map1)
f3.add_to(map1)
folium.LayerControl().add_to(map1)
map1

