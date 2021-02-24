import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely import geometry

def origin(city,line):
    url = 'https://restapi.amap.com/v3/bus/linename?s=rsv3&extensions=all&key=4c725e376bc5e51f712f242234ed7420&output=json&city={}&offset=1&keywords={}&platform=JS'.format(city,line)
    r = requests.get(url).text
    rt = json.loads(r)
    route = rt['buslines'][0]['polyline']
    stop = rt['buslines'][0]['busstops']
    return route,stop

def location(city,line):
    route,stop = origin(city,line)
    routel = route.split(';')
    loc = list()
    for i in routel:
        locrow = i.split(',')
        loc.append((float(locrow[0]),float(locrow[1])))
    linedata = geometry.LineString(loc)
    stopname = list()
    stoploc = list()
    for i in stop:
        stopname.append(i['name'])
        stoplocrow = i['location'].split(',')
        stoploc.append((float(stoplocrow[0]),float(stoplocrow[1])))
    stopdata = geometry.MultiPoint(stoploc)
    
    return linedata,stopdata

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1,1,1)
def draw(x):
    ldl = list()
    sdl = list()
    nl = list()
    for i in x:
        a,b = location(i[0],i[1])
        ldl.append(a)
        sdl.append(b)
        nl.append(i[1])
    dfl = pd.DataFrame()
    dfp = pd.DataFrame()
    dfl['line'] = nl
    dfl['geometry'] = ldl
    dfp['line'] = nl
    dfp['geometry'] = sdl
    gdfl = gpd.GeoDataFrame(dfl)
    gdfp = gpd.GeoDataFrame(dfp)
    gdfl.crs = 'EPSG:4326'
    gdfp.crs = 'EPSG:4326'
    gdfl.plot(ax=ax,cmap=plt.cm.tab10)
    gdfp.plot(ax=ax,cmap=plt.cm.tab10)
    plt.show()

#示例
draw([[440400,'B9路'],[440400,'G993路']])
