import pandas as pd
import folium
from folium.features import CustomIcon

coordinate_com = pd.DataFrame()
coordinate_yet=pd.DataFrame()
gu_complete = ['광진구', '양천구', '구로구', '영등포구', '서초구', '강남구', '송파구','금천구','마포구','서대문구','용산구','은평구','종로구','중구']
gu_yet = ['강북구', '강서구', '동작구','관악구', '강동구', '성동구', '동대문구', '중랑구','성북구','도봉구','노원구']
for i in gu_complete:
    exercise = pd.read_excel("./구별파일/" + i + ".xlsx", sheet_name='Sheet2')
    while 1:
        if '위도' in list(exercise.columns):
            break
        else:
            exercise.reset_index()
            exercise.columns = list(exercise.iloc[0, :])
            exercise = pd.DataFrame(exercise.iloc[1:, :])
    print(exercise)
    exercise.reset_index()
    exercise = exercise.loc[:, ['위도', '경도']]
    coordinate_com = pd.concat([coordinate_com, exercise], ignore_index=True)

for i in gu_yet:
    exercise = pd.read_excel("./구별파일/" + i + ".xlsx", sheet_name='Sheet2')
    while 1:
        if '위도' in list(exercise.columns):
            break
        else:
            exercise.reset_index()
            exercise.columns = list(exercise.iloc[0, :])
            exercise = pd.DataFrame(exercise.iloc[1:, :])
            print("ok")
    exercise.reset_index()
    exercise = exercise.loc[:, ['위도', '경도']]
    coordinate_yet = pd.concat([coordinate_yet, exercise], ignore_index=True)


for k in range(len(coordinate_com)):
    if coordinate_com.iloc[k, 0] < 100:
        temp = coordinate_com.iloc[k, 0]
        coordinate_com.iloc[k, 0] = coordinate_com.iloc[k, 1]
        coordinate_com.iloc[k, 1] = temp

for k in range(len(coordinate_yet)):
    if coordinate_yet.iloc[k, 0] < 100:
        temp = coordinate_yet.iloc[k, 0]
        coordinate_yet.iloc[k, 0] = coordinate_yet.iloc[k, 1]
        coordinate_yet.iloc[k, 1] = temp

y_com = coordinate_com['위도']
x_com = coordinate_com['경도']
y_yet=coordinate_yet['위도']
x_yet=coordinate_yet['경도']


# 지도 띄우기

m = folium.Map(location=[37.55, 126.98], zoom_start=11.3)

coords_com = []
coords_yet=[]
for i in range(len(coordinate_com)):
    xx = x_com[i]
    yy = y_com[i]
    coords_com.append([xx, yy])
for i in range(len(coordinate_yet)):
    xx = x_yet[i]
    yy = y_yet[i]
    coords_yet.append([xx, yy])

from folium.plugins import MarkerCluster

marker_cluster = MarkerCluster().add_to(m)

for i in range(len(coords_com)):
    folium.Circle(
        location=tuple(coords_com[i]),
        radius=50,
        color='blue',
        fill='crimson',
    ).add_to(marker_cluster)
for i in range(len(coords_yet)):
    folium.Circle(
        location=tuple(coords_yet[i]),
        radius=50,
        color='red',
        fill='crimson',
    ).add_to(marker_cluster)
for i in range(len(coords_com)):
    folium.Circle(
        location=tuple(coords_com[i]),
        radius=50,
        color='blue',
        fill='crimson',
    ).add_to(m)
for i in range(len(coords_yet)):
    folium.Circle(
        location=tuple(coords_yet[i]),
        radius=50,
        color='red',
        fill='crimson',
    ).add_to(m)
m.save("./체육시설위치.html")

print("ㅇㅋ")
