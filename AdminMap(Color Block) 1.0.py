import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely import geometry

def origin(dist):
    list1 = list()
    for i in dist:
        url = 'https://restapi.amap.com/v3/config/district?key=ccc8374a42536331fa6047ed5874ebf5&keywords={}&subdistrict=1&page=1&offset=1&extensions=all'.format(i)
        r = requests.get(url).text
        rt = json.loads(r)
        pl = rt['districts'][0]['polyline']
        list1.append(pl)
    return list1

def locations(dist):
    list1 = origin(dist)
    list2 = list()
    n = 0
    for i in list1:
        if '|' in i:
            list3 = i.split('|')
            mloc = list()
            for k in list3:
                loc = list()
                list4 = k.split(';')
                for m in list4:
                    list5 = m.split(',')
                    loc.append((float(list5[0]),float(list5[1])))
                mloc.append(geometry.Polygon(loc))
            list2.append([dist[n],geometry.MultiPolygon(mloc)])
        else:    
            list6 = i.split(';')
            loc = list()
            for m in list6:
                list7 = m.split(',')
                loc.append((float(list7[0]),float(list7[1])))
            list2.append([dist[n],geometry.Polygon(loc)])
    n += 1
    return list2

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1)
def draw(dist):
    data = locations(dist)
    df = pd.DataFrame(data,columns=['name','geometry'])
    gdf = gpd.GeoDataFrame(df)
    gdf.crs = 'EPSG:4326'
    gdf.plot(ax=ax,k=4,cmap=plt.cm.tab10)

#示例
draw([440100,440300,440400,440600,440700,441200,441300,441900,442000,810000,820000])
plt.title('Guangdong-Hong Kong-Macau Great Bay Area')
plt.show()
