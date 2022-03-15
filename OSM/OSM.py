# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import osmnx as ox
import pandas as pd



def out_osm(place,tags):
    df = ox.geometries_from_place(place, tags=tags)
    #df = df[df.geom_type == 'Point'][:]
    keys=['name','geometry']
    for key in tags.keys():
        keys.append(str(key))
        #print(keys)
    df=df[keys]
    return df
    

place = 'Warsaw, PL'
tags = {'amenity': 'bicycle_rental','public_transport': 'station','cycleway':'lane'}
df=out_osm(place,tags)
