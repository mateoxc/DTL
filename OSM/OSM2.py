import osmnx as ox
import pandas as pd
import time


def out_osm(place,tags,fname):
    ox.config(timeout=1700)
    df = ox.geometries_from_place(place, tags=tags,)
    df.to_csv(fname,encoding='utf8') 
    
    

place = 'Warsaw, PL'
tags = {'amenity': ['bicycle_rental','bicycle_parking','bicycle_repair_station','bus_station']
        ,'building':['train_station','transportation']
        ,'public_transport': ['station','stop_position','platform','station','stop_area']
        ,'highway':['bus_stop']
        ,'railway':['halt','platform','station','tram_stop']}

tags_lines={'highway':['busway','cycleway']
            ,'cycleway':['lane','opposite','opposite_lane','track','opposite_track','share_busway','opposite_share_busway','shared_lane']
            ,'busway	':['lane']
            ,'railway':['light_rail','monorail','rail','subway','tram']
            ,'route	':['bicycle','bus','light_rail','railway','tram']}

start_time = time.time()


out_osm(place,tags,'poi.csv')
out_osm(place,tags_lines,'lines.csv')

print("--- %s seconds ---" % int(time.time() - start_time))