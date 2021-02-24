# Python地图绘制程序CityMap
## AdminMap
* AdminMap程序用于绘制行政区域地图，可选择将行政区域填色或画出边界轮廓。

* AdminMap(Boundary) 1.0绘制行政区域边界地图。例如：

![边界图](https://github.com/huzaizhou/CityMap/blob/main/image/boundry%20example.png)

* AdminMap(Color Block) 1.0绘制行政区域色块地图。例如：

![色块图](https://github.com/huzaizhou/CityMap/blob/main/image/color%20block%20example.png)

* 使用方法为给draw函数传入行政区域编码列表参数，格式为draw([编码1, 编码2, 编码3, ……])。编码可在AMap_adcode_citycode.xlsx中查询。

## LineMap
* LineMap程序用于绘制公交线路图，可绘制多个城市的多条线路，并标注站点。

* LineMap 1.0版本可以为不同的线路添加不同的颜色，但无法区分不同线路的站点。例如：

![LineMap1.0示例](https://github.com/huzaizhou/CityMap/blob/main/image/LineMap1.0%20example.png)

* LineMap 2.0版本可以为不同线路及其站点添加不同的颜色。例如：

![LineMap2.0示例](https://github.com/huzaizhou/CityMap/blob/main/image/LineMap1.1%20example.png)

* 使用方法为给draw函数同时传入行政区域编码和线路名称列表，格式为draw([编码1, 线路1], [编码2, 线路2],[编码3, 线路3],……)
