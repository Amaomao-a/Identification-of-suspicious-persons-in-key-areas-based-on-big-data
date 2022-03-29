from math import radians, cos, sin, asin, sqrt, fabs

import pandas
from scipy.spatial import Delaunay
import numpy as np
import matplotlib.pyplot as plt

towerList = []


def dataInput():  # 读入基站位置数据并建立基站群
    fileName = 'PekingCells.csv'
    df = pandas.read_csv(fileName, encoding='utf-8', usecols=[0, 1, 2])
    global towerList
    idList = df['cellID'].tolist()
    lonList = df['longitude'].tolist()
    latList = df['latitude'].tolist()
    for i in range(len(idList)):
        towerList.append(tower(idList[i], lonList[i], latList[i]))


class tower:
    def __init__(self, cellID, longitude, latitude):
        self.cellID = cellID        # 基站标识
        self.longitude = longitude  # 经度
        self.latitude = latitude    # 纬度


class area:
    towers = []  # 区域内的基站群
    centerX = 0  # 中心点坐标
    centerY = 0
    radius = 0   # 半径

    def __init__(self, areaTowers):
        self.towers = areaTowers
        self.findCenterOfArea()
        self.getRadius()

    def geoDistance(self, lon1, lat1, lon2, lat2):  # haversine公式计算球面两点间的距离
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])  # 将经纬度转化为弧度
        diffLon = fabs(lon2 - lon1)
        diffLat = fabs(lat2 - lat1)
        h = sin(diffLat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(diffLon / 2) ** 2
        earthRadius = 6371 * 1000
        dist = 2 * earthRadius * asin(sqrt(h))

        return dist

    def findCenterOfArea(self):  # 根据基站群进行Delaunay三角剖分，计算得到中心点及半径
        points = np.zeros((len(self.towers), 2))  # 生成位置信息的点集
        for i in range(len(self.towers)):
            points[i][0] = self.towers[i].longitude
            points[i][1] = self.towers[i].latitude

        tri = Delaunay(points)  # 三角剖分
        # tri.simplices表示剖分后三角形中顶点的索引 point[tri.simplices]表示三角形坐标
        center = (np.sum(points[tri.simplices], axis=1) / 3.0)  # 每个三角形的中心点
        # 根据单个中心点计算出区域中心点坐标
        totalS, totalX, totalY = 0, 0, 0

        for index, sim in enumerate(points[tri.simplices]):
            cx, cy = center[index][0], center[index][1]
            x1, y1 = sim[0][0], sim[0][1]
            x2, y2 = sim[1][0], sim[1][1]
            x3, y3 = sim[2][0], sim[2][1]

            curS = x1 * y2 - x1 * y3 + x2 * y3 - x2 * y1 + x3 * y1 - x2 * y2
            totalS += curS
            totalX += cx * curS
            totalY += cy * curS

        self.centerX, self.centerY = totalX / totalS, totalY / totalS
        print(self.centerX, self.centerY)
        p = np.array([(116.16757295574666, 40.23982176558823)])
        print(tri.find_simplex(p))  # 找出点在哪个三角形中

    def getRadius(self):
        # 求每个基站到中心点坐标的距离均值
        self.radius = 0.0
        for item in self.towers:
            self.radius += self.geoDistance(item.longitude, item.latitude, self.centerX, self.centerY) / len(self.towers)

        print(self.radius)

    def isLocatedArea(self, lon, lat):
        return self.geoDistance(lon, lat, self.centerX, self.centerY) <= self.radius


dataInput()
a1 = area(towerList)

